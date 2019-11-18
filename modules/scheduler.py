# -*- coding: utf-8 -*-
from modules.queue import ProcessesQueue, BlockedQueue

class Scheduler():

    def __init__(self, resource_manager, memory):
        
        self.ready = ProcessesQueue()
        self.blocked = BlockedQueue(resource_manager)
        self.waiting = []
        self.finished = []
        self.resource_m = resource_manager
        self.mem_m = memory
        self.running = None
        
    def update(self, running_process):
        # Aging
        # Na fila de prontos
        # Todo clock aumenta a prioridade dos primeiros processos que estão
        # nas filas de prioridade 2 e 3
        if running_process is not None:
            if not running_process.running:
                self.mem_m.delete_process(running_process)
                self.resource_m.free(running_process)
        # Blocked processes
        ready = self.blocked.pop_ready()
        for p in ready:
            self.ready.add(p)
        # Motivos
            # Recurso - Ex: Impressora
            # Recuros do sistema
            # Quantidade de processos prontos - 1000
            # Adiciona na lista de prontos
        self.pop_waiting()
        self.ready.process_aging()


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
                self.blocked.push(proc)

    def pop_waiting(self):
        # Recebe novos processos
        # Adiciona na fila de prontos
        if self.waiting:
            proc = self.waiting[0]
            try:  
                self.mem_m.create_process(proc)
                self.waiting.pop(0)
            except:
                return
            try:
                self.resource_m.allocate(proc)
                self.ready.add(proc)
            except:
                self.blocked.push(proc)

    def get_process_to_execute(self, running_process):
        # verifica tempo de CPU do atual
        if running_process is not None:
            is_running = running_process.running
            prio = running_process.priority
            if not is_running:
                running_process = None
        else:
            is_running = False
        #loop - enquanto filas n estiverem vazia
        next = self.ready.get_next()
        while(next is not None):
            # acha melhor candidato
            # Tempo n acabou
            # se tiver prioridade maior
            if is_running:
                if prio != 0 and prio >= next.priority:
                    self.ready.add(running_process)
                    return self.ready.next()
                else:
                    return running_process
            else: # Tempo de CPU acabou
                return self.ready.next() # retorna melhor candidato
            
            next = self.ready.get_next()
         # retorna IDLE
        return running_process
        