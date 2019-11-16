import sys
from modules.process import load_processes
from modules.file_system import FileSystem
from modules.scheduler import Scheduler
from modules.memory import Memory
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
        dispatch(process_running)

def process_launcher(clock, processes):
    if clock in processes:
        return processes[clock]
    return []

def dispatch(process):
    # alocação de memória
    # se novo processo imprimir informações gerais
    # caso contrário continuar execução
    pass

def print_args_error():
    pass

if __name__ == '__main__':
    main()