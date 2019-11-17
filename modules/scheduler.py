from queue import ProcessesQueue


class Scheduler():

    def __init__(self, resource_manager, memory):
        self.ready = ProcessesQueue()
        self.blocked = []
        self.waiting = []
        self.finished = []
        self.resource_m = resource_manager
        self.mem_m = memory

    def update(self):
        # Aging
        # Na fila de prontos
        # Todo clock aumenta a prioridade dos primeiros processos que estão
        # nas filas de prioridade 2 e 3
        ready.process_aging()

        # Blocked processes
            # Motivos
                # Recurso - Ex: Impressora
                # Recuros do sistema
                    # Memória
                    # Quantidade de processos prontos - 1000
            # Adiciona na lista de prontos

    def send_ready_process(self, processes):
        # Recebe novos processos
        # Adiciona na fila de prontos
        for proc in processes:
            try:
                mem_m.create_process(proc)
                resource_m.allocate(proc)
                ready.add(proc)
            except:
                blocked.append(proc)

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
