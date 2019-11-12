'''
Memory Module

Contiguous blocks of memory. Each process have to check if there is memory avaiable before executing.
64 blocks to real-time processes
960 blocks to user processes
'''

class Memory:

    def __init__(self):
        self.allocfreelist_real = [{'start': 0 ,'length':64}]
        self.allocfreelist_user = [{'start': 64 ,'length':960}]
        self.alloc_oc_real = [{'pid': None, 'length': None, 'start': None}]
        self.alloc_oc_user = [{'pid': None, 'length': None, 'start': None}]


    def check_and_allocate(self, prio, numblock, pid):
        
        mem_req = numblock #Size of the process #alterar para incluir a classe processo
        #Check process priority
        if  prio == 0: #Real-time process alterar para incluir a classe processo
            initial_block = 0
            final_block = 63
            list_free_process = self.allocfreelist_real
            list_oc_process = self.alloc_oc_real
        else:                         #User process
            initial_block = 64
            final_block = 959
            list_free_process = self.allocfreelist_user
            list_oc_process = self.alloc_oc_user

        #Test
        print('Inital Block:', initial_block)
        print('Final Block:', final_block)

        #Check if the process is not too big to fit the blocks 
        if mem_req > (final_block - initial_block):
            print("The process is too big to fit our memory")
            return -1

        #Check if there is enough room for the process in the memory
        for key in list_free_process:
            if(key['length'] >= mem_req): #check if exist an element of the list with sufficient size    
                element = {'pid': pid, 'start': key['start'] , 'length': mem_req} #creates the element for the occupied list #alterar para incluir a classe processo
                key['start'] = key['start'] + mem_req #Updates the free list 
                key['length'] = key['length'] - mem_req
                list_oc_process.append(dict(element)) #append an element to the occupied list
                if(prio == 0):#alterar para incluir a classe processo
                    self.allocfreelist_real = list_free_process
                    self.alloc_oc_real = list_oc_process
                else:
                    self.allocfreelist_user = list_free_process
                    self.alloc_oc_user = list_oc_process
                self.adequate_memory()
                return 1 
        print('Error no blocks available')
        return -1 
    
    def adequate_memory(self):  
        for key in self.allocfreelist_real:
            if(key['length'] == 0):
                self.allocfreelist_real.remove(key)
        for key in self.allocfreelist_user:
            if(key['length'] == 0):
                self.allocfreelist_real.remove(key)            

    def delete_process(self, num_block_mem, pid, prio):
        mem_req = num_block_mem #Size of the process #alterar para incluir a classe processo
        
        if  prio == 0: #Real-time process alterar para incluir a classe processo
            initial_block = 0
            final_block = 63
            list_free_process = self.allocfreelist_real
            list_oc_process = self.alloc_oc_real
            print("PROCESSO DE TEMPO REAL")
        else:                         #User process
            initial_block = 64
            final_block = 959
            list_free_process = self.allocfreelist_user
            list_oc_process = self.alloc_oc_user
        
        
        for key in list_oc_process:
             if(key['pid'] == pid): #check what is the element in the list
                start = key['start'] #saves the start position
                length = key['length'] #saves the length
                list_oc_process.remove(key) #deletes the element from the list
                element = {'start': key['start'] , 'lenght': mem_req} #creates the element for the free list
                list_free_process.append(dict(element)) #append an element to the occupied list
                return 1

    def __str__(self):
        print ('----------------------------------------------------------------------------------------------------')
        txt = 'Lista de Livres Tempo real: ' + str(self.allocfreelist_real) + '\n'
        txt += 'Lista de Ocupados Tempo real: ' + str(self.alloc_oc_real) + '\n'
        txt += 'Lista de Livres Usuario: ' + str(self.allocfreelist_user) + '\n'
        txt += 'Lista de Ocupados Usuario: ' + str(self.alloc_oc_user)
        print ('----------------------------------------------------------------------------------------------------')
        return txt









