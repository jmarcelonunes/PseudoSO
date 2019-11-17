import sys
from modules.process import load_processes
from modules.file_system import FileSystem
from modules.scheduler import Scheduler
from modules.memory import Memory
from modules.resources import ResourceManager
def main():
    # Obtendo argumentos do terminal
    args_length = len(sys.argv) - 1
    args = sys.argv[1:]

    if args_length != 2:
        print_args_error()
        return 0
    
    process_filename = args[0]
    files_filename = args[1]

    clock = 0

    # Inicializar sistemas 

    # processos
        # ler os processos do arquivo de processos
        # ler as requisições de arquivos
    processes = load_processes(process_filename, files_filename)

    # memória
    memory = Memory()

    # sistema de arquivos
        # inicializar
        # adicionar dados do arquivo
    filesys = FileSystem(files_filename)

    # escalonador
    scheduler = Scheduler()

    #recursos
    resources = ResourceManager()

    # processo em execução
    process_running = None 

    # loop pelo clock até lista de processos gerais ficar vazia
    while scheduler.waiting_is_filled():
        # timer (clock)
            # retorna processos ou lista de processo
            # pelo clock
        proc_list = process_launcher(clock, processes)

        # atualiza escalonador
            # checar bloqueados no escalonador
            # atualizar escalonador (aging)
        scheduler.update()
        # forma pacote de processos
        # envia pacote para o escalonador
        scheduler.send_ready_process(proc_list)
        # escalonador retorna processo a ser executado
            # retorna sinal se é pra trocar ou não o processo atual
        process_running = scheduler.get_process_to_execute()
        # dispatcher
        dispatch(process_running, memory, filesys, resources)
        clock += 1

def process_launcher(clock, processes):
    if clock in processes:
        return processes[clock]
    return []

def dispatch(process, memory, filesys, resources):
    # se novo processo imprimir informações gerais
    if process.new:
        process.new = False
        print("Dispatcher =>")
        print("\tPID: %d", process.pid)
        print("\toffset: %d", memory.get_process_offset(process))
        print("\tblocks: %d", process.blocks)
        print("\tpriority: %d", process.priority)
        print("\ttime: %d", process.total_exec_time)
        print("\tprinters: %d", process.printer_cod)
        print("\tscanners: %d", process.scanner)
        print("\tmodems: %d", process.modem)
        print("\tdrives: %d", process.disk_cod)
    
    if(process.total_exec_time > 0): #Ainda tem tempo de CPU disponivel
        print("\tprocess %d", process.pid)
        print("\tP%d STARTED", process.pid)
        if process.intructions_pc in process.instructions:
            if(process.instructutions[process.intructions_pc].operation == 0): #criacao de arquivo
                try:
                    f = filesys.create_file(process.instructutions[process.intructions_pc], process)
                    filename = f.name
                    start = f.start
                    end = f.end
                    print("\tO processo %d criou o arquivo %c (blocos %d e %d).", process.pid, filename, start, end)
                except Exception as e:
                    print("\tP%d instruction %d – FALHA", process.pid, process.intructions_pc)
                    print(e)

            if(process.instructutions[process.intructions_pc].operation == 1): #deletar arquivo
                try:
                    filesys.delete_file(process.instructutions[process.intructions_pc], process)
                    filename = process.instructutions[process.intructions_pc].filename
                    print("\tO processo %d deletou o arquivo %c (blocos 3 e 4).", process.pid, filename)
                except Exception as e:
                    print("\tP%d instruction %d – FALHA", process.pid, process.intructions_pc)
                    print(e)
                
        else:
            print("\tP%d instruction %d – SUCESSO CPU", process.pid, process.intructions_pc)
        
        process.intructions_pc += 1
        process.exec_time -= 1
        process.running = True
 
    else:
        memory.delete_process(process)
        resources.free(process)
        print("\tP%d instruction %d – FALHA", process.pid, process.intructions_pc)
        print("O processo %d esgotou o seu tempo de CPU!" , process.pid) 
        process.running = False

    
 
def print_args_error():
    pass

if __name__ == '__main__':
    main()