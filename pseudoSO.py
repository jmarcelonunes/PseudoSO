import sys

def main():
    # Obtendo argumentos do terminal
    args_length = len(sys.argv) - 1
    args = sys.argv[1:]

    if args_length != 2:
        print_args_error()
        return 0
    
    process_filename = args[0]
    files_filename = args[1]

    master_clock = 0

    # Inicializar sistemas 
    # processos
        # ler os processos do arquivo de processos
        # ler as requisições de arquivos
    # sistema de arquivos
        # inicializar
        # adicionar dados do arquivo
    # escalonador

    # loop pelo clock até lista de processos gerais ficar vazia
        # timer (clock)
            # retorna processos ou lista de processo
            # pelo clock
        # atualiza escalonador
            # checar bloqueados no escalonador
            # atualizar escalonador (aging)
        # forma pacote de processos
        # envia pacote para o escalonador
        # escalonador retorna processo a ser executado
            # retorna sinal se é pra trocar ou não o processo atual
        # dispatcher
            # alocação de memória
            # se novo processo imprimir informações gerais
            # caso contrário continuar execução

    
def print_args_error():
    pass

if __name__ == '__main__':
    main()