class Scheduler():

    def __init__(self):
        self.ready = []
        self.blocked = []
        self.waiting = []
        self.finished = []
        pass

    def update(self):
        # Aging
            # Na fila de prontos
            # Todo clock aumenta a prioridade de todos
        # Blocked processes
            # Motivos
                # Recurso - Ex: Impressora
                # Recuros do sistema
                    # Memória
                    # Quantidade de processos prontos - 1000
            # Adiciona na lista de prontos
        pass

    def send_ready_process(self, process):
        # Recebe novos processos
        # Adiciona na fila de prontos
        pass

    def get_process_to_execute(self):
        # verifica tempo de CPU do atual
        #loop - enquanto filas n estiverem vazia
            # acha melhor candidato
            # Tempo n acabou
                # se tiver prioridade maior
                    # verifica recurso de memória
                    # verifica recurso de IO
                        # retorna novo processo
            # Tempo de CPU acabou
                # retorna melhor candidato
        # retorna IDLE
        pass

    def waiting_is_filled(self):
        # Retorna True ou False se ainda há processos que não
        # foram executados
        pass