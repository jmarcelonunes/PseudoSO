# -*- coding: utf-8 -*-
from modules.queue import ProcessesQueue, BloquedQueue

class Scheduler():

    def __init__(self, resource_manager, memory):
        
        self.ready = ProcessesQueue()
        self.blocked = BloquedQueue(resource_manager)
        self.waiting = []
        self.finished = []
        self.resource_m = resource_manager
        self.mem_m = memory
        self.running = None
        
    def update(self):
        # Aging
        # Na fila de prontos
        # Todo clock aumenta a prioridade dos primeiros processos que estão
        # nas filas de prioridade 2 e 3
        self.ready.process_aging()

        # Blocked processes
        ready = self.bloqued.pop_ready()
        self.send_ready_process(ready)
        # Motivos
            # Recurso - Ex: Impressora
            # Recuros do sistema
            # Quantidade de processos prontos - 1000
            # Adiciona na lista de prontos

    def send_ready_process(self, processes):
        # Recebe novos processos
        # Adiciona na fila de prontos
        for proc in processes:
            try:  
                self.mem_m.create_process(proc)
            except:
                self.waiting.append(proc)
                continue
            try:
                self.resource_m.allocate(proc)
                self.ready.add(proc)
            except:
                self.bloqued.push(proc)

    def pop_waiting(self):
        # Recebe novos processos
        # Adiciona na fila de prontos
        for proc in self.waiting:
            try:
                self.resource_m.allocate(proc)
                self.mem_m.create_process(proc)
                self.ready.add(proc)
            except:
                self.waiting.append(proc)


    def get_process_to_execute(self, running_process):
        # verifica tempo de CPU do atual
        is_running = running_process.running
        prio = running_process.priority
        if not is_running:
            self.mem_m.delete_process(running_process)
            self.bloqued.pop_ready()
        #loop - enquanto filas n estiverem vazia
        next = self.ready.get_next()
        while(next is not None):
            # acha melhor candidato
            # Tempo n acabou
            # se tiver prioridade maior
            if is_running:
                if prio != 0 and prio <= next.priority:  
                    # verifica recurso de memória
                    next = verify_requirements(next)
                    if  next is not None:
                        return next
                else:
                    return running_process
            else: # Tempo de CPU acabou
                next = verify_requirements(next)
                if  next is not None:
                    return next # retorna melhor candidato
            next = self.ready.get_next()
         # retorna IDLE
        return None

    def verify_requirements(self, next):
        try:
            self.mem_m.create_process(next)
            return self.ready.next()
        except:
            blocked_process = self.ready.next()
            self.blocked.append(blocked_process)
            return None