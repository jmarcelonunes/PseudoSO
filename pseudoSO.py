# -*- coding: utf-8 -*-
import sys
from modules.process import load_processes, processes_by_init_time
from modules.file_system import FileSystem
from modules.scheduler import Scheduler
from modules.memory import Memory
from modules.resources import ResourceManager

GLOBAL_processes = {}
GLOBAL_clock = 0

def main():
    # Obtendo argumentos do terminal
    args_length = len(sys.argv) - 1
    args = sys.argv[1:]

    if args_length != 2:
        print_args_error()
        return 0
    
    process_filename = args[0]
    files_filename = args[1]


    # Inicializar sistemas 
    global GLOBAL_clock
    global GLOBAL_processes
    GLOBAL_processes = load_processes(process_filename, files_filename)
    processes = processes_by_init_time(GLOBAL_processes)
    memory = Memory()

    # sistema de arquivos
        # inicializar
        # adicionar dados do arquivo
    filesys = FileSystem(files_filename)

    #recursos
    resources = ResourceManager()

    # escalonador
    scheduler = Scheduler(resources, memory)

   
    process_running = None 
    print(GLOBAL_clock)
    # loop pelo clock ate lista de processos gerais ficar vazia
    while GLOBAL_processes:
        # timer (clock)
            # retorna processos ou lista de processo
            # pelo clock
        proc_list = process_launcher(GLOBAL_clock, processes)

        # atualiza escalonador
            # checar bloqueados no escalonador
            # atualizar escalonador (aging)
        scheduler.update(process_running)
        # forma pacote de processos
        # envia pacote para o escalonador
        scheduler.send_ready_process(proc_list)
        # escalonador retorna processo a ser executado
            # retorna sinal se eh pra trocar ou nao o processo atual
        process_running = scheduler.get_process_to_execute(process_running)
        # dispatcher
        dispatch(process_running, memory, filesys, resources)
        
        GLOBAL_clock += 1
        #print(GLOBAL_clock)
    print(filesys)

def process_launcher(clock, processes):
    if clock in processes:
        return processes[clock]
    return []

def dispatch(process, memory, filesys, resources):
    # print(GLOBAL_clock)
    # Não há processo a ser enviado a CPU
    if process is None:
        return
    # se novo processo imprimir informacoes gerais
    if process.new:
        process.new = False
        print("Dispatcher =>")
        print("\tPID: %d" % process.pid)
        print("\toffset: %d" % memory.get_process_offset(process))
        print("\tblocks: %d" % process.blocks)
        print("\tpriority: %d" % process.priority)
        print("\ttime: %d" % process.total_exec_time)
        print("\tprinters: %d" % process.printer_cod)
        print("\tscanners: %d" % process.scanner)
        print("\tmodems: %d" % process.modem)
        print("\tdrives: %d" % process.disk_cod)
        print("process %d => " % process.pid)
        print("P%d STARTED" % process.pid)
    
    if(process.exec_time > 0): #Ainda tem tempo de CPU disponivel
       
        if process.intructions_pc in process.instructions:
            if(process.instructions[process.intructions_pc].operation == 0): #criacao de arquivo
                try:
                    f = filesys.create_file(process.instructions[process.intructions_pc], process)
                    filename = f.name
                    start = f.start
                    end = f.end
                    print("P%d instruction %d – SUCESSO" % (process.pid, process.intructions_pc))
                    print("O processo %d criou o arquivo %c (blocos %d e %d)." % (process.pid, filename, start, (end-1)))
                except Exception as e:
                    print("P%d instruction %d – FALHA" % (process.pid, process.intructions_pc))
                    print(e)

            if(process.instructions[process.intructions_pc].operation == 1): #deletar arquivo
                try:
                    filesys.delete_file(process.instructions[process.intructions_pc], process)
                    filename = process.instructions[process.intructions_pc].filename
                    print("P%d instruction %d – SUCESSO" % (process.pid, process.intructions_pc))
                    print("O processo %d deletou o arquivo %c." % (process.pid, filename))
                except Exception as e:
                    print("P%d instruction %d – FALHA" % (process.pid, process.intructions_pc))
                    print(e)
                
        else:
            print("P%d instruction %d – SUCESSO CPU" % (process.pid, process.intructions_pc))
        
        process.intructions_pc += 1
        process.exec_time -= 1
        process.running = True
 
    else:
        print("P%d instruction %d – FALHA" % (process.pid, process.intructions_pc))
        print("O processo %d esgotou o seu tempo de CPU!" % process.pid) 
        process.running = False
        del GLOBAL_processes[process.pid]

    
 
def print_args_error():
    pass

if __name__ == '__main__':
    main()