'''
Memory Module

Contiguous blocks of memory. Each process have to check if there is memory avaiable before executing.
64 blocks to real-time processes
960 blocks to user processes
'''

class Memory:
    def __init__(self):
        self.initialMemory = 1024 #Check the memory word size?

    def CheckAvailMemory(self, process):
        
        MemReq = process.numBlockMem #Size of the process

        #Check process priority
        if process.prioridade == '0': #Real-time process
            InitialBlock = 0
            FinalBlock = 63
        else:
            InitialBlock = 64
            FinalBlock = 959
        
        #To Do:

        #Check if the process is not too big to fit the blocks 


        #Check if there is enough room for the process in the memory

