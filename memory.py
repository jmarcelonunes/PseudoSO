'''
Memory Module

Contiguous blocks of memory. Each process have to check if there is memory avaiable before executing.
64 blocks to real-time processes
960 blocks to user processes
'''

class Memory:

    def __init__(self):
        self.memory_real_time = MemoryList(0, 64)
        self.memory_user = MemoryList(64, 960)
        
    def create_process(self, pid, prio, numblock):
  
        #Check process priority
        partition = self.memory_real_time if prio == 0 else self.memory_user
        holes = partition.holes
        processes = partition.processes
        if partition.check_size(numblock):
            raise Exception("Memory too small for the process")
        #Check if there is enough room for the process in the memory
        for hole in holes:
            if(hole['length'] >= numblock): #check if exist an element of the list with sufficient size                  
                #creates the element for the occupied list #alterar para incluir a classe processo
                element = {'pid': pid, 
                           'start': hole['start'], 
                           'length': numblock
                          }
                hole['length'] -= numblock #Updates the free list
                if hole['length'] == 0:
                    holes.remove(hole)  
                else:
                    hole['start'] += numblock #Updates the free list
                for index, process in enumerate(processes):
                    if process['start'] > element['start']:
                        processes.insert(index, element) #append an element to the occupied list
                        return 0
                processes.append(element) 
                return 0

        return -1          

    def delete_process(self, pid, prio):

        partition = self.memory_real_time if prio == 0 else self.memory_user
        holes = partition.holes
        processes = partition.processes   
        
        for process in processes:
            if(process['pid'] == pid): #check what is the element in the list
                new_hole = {'start': process['start'], 'length': process['length']} #creates a new hole element
                processes.remove(process) #deletes the element from the list

                for index,hole in enumerate(holes):
                    if hole['start'] > new_hole['start']:
                        holes.insert(index,new_hole)
                        self.colapse(holes, index)
                        return 0
                holes.append(new_hole)
                self.colapse(holes, len(holes) - 1)
                return 0
        return -1

    def colapse(self, holes, index):
        next_index = index + 1
        previous_index = index - 1
        start = holes[index]['start']
        end = start + holes[index]['length']
        hole = holes[index]
        if next_index < len(holes):
            if holes[next_index]['start'] ==  end:
                hole['length'] += holes[next_index]['length']
                holes.pop(next_index)
        if previous_index >= 0:
            if (holes[previous_index]['start'] + holes[previous_index]['length']) == start:
                holes[previous_index]['length'] += hole['length']
                holes.pop(index)


    def __str__(self):
        print ('----------------------------------------------------------------------------------------------------')
        txt =  'Lista de Livres Tempo real: ' + str(self.memory_real_time.holes) + '\n'
        txt += 'Lista de Ocupados Tempo real: ' + str(self.memory_real_time.processes) + '\n'
        txt += 'Lista de Livres Usuario: ' + str(self.memory_user.holes) + '\n'
        txt += 'Lista de Ocupados Usuario: ' + str(self.memory_user.processes)
        print ('----------------------------------------------------------------------------------------------------')
        return txt

class MemoryList:
    
    def __init__(self, initial_block, final_block):
        self.initial_block = initial_block
        self.final_block = final_block
        self.processes = []
        self.holes = [{'start':initial_block, 'length':final_block}]
        
    def check_size(self,numblock):
        return numblock > (self.final_block - self.initial_block)









