'''
Memory Module

Contiguous blocks of memory. Each process have to check if there is memory avaiable before executing.
64 blocks to real-time processes
960 blocks to user processes
'''

class Memory:
    def __init__(self):
        self.initialMemory = [None]*1024 #1024 blocks with null values

    def CheckAvailMemory(self, process):
        
        MemReq = process.numBlockMem #Size of the process

        #Check process priority
        if process.prioridade == '0': #Real-time process
            InitialBlock = 0
            FinalBlock = 63
        else:                         #User process
            InitialBlock = 64
            FinalBlock = 959

        #Check if the process is not too big to fit the blocks 
        if MemReq > (FinalBlock - InitialBlock):
            print("The process is too big to fit our memory")
            return -1

        #Check if there is enough room for the process in the memory
        y = 0
        for x in range(InitialBlock, FinalBlock + 1):
            
            if self.initialMemory[x] == None: #Not occupied
                
                for y in range(x, FinalBlock + 1): 
                    AvailSize = (y - x) 
                    
                    if y == FinalBlock: #If there is not enough space
                        print("No sufficient memory")
                        return -1

                    if AvailSize == MemReq: #Check if the size is sufficient
                        FinalBlockValue = y #Set the final allocation block
                        break
                    
            if AvailSize == MemReq:
                return FinalBlockValue
            
            if x == FinalBlock: #If there is none blank space
                print("No sufficient memory")
                return -1
                        
    def allocateMemory(self, process, FinalBlockValue):
        InitialBlockValue = FinalBlockValue - process.numBlockMem
        
        for x in range(InitialBlockValue, FinalBlockValue):
            self.initialMemory[x] = 1
        
        self.initialMemory[x + 1] = 1
        
        return 1

    # TO DO:
    #Clean memory
    #Run this code and debug (Especially Check Avail Memory)
    



        
                
            
        

