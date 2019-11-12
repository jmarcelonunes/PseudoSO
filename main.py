import memory

print("Hello World!")
memoria = memory.Memory()
memoria.CheckAvailMemory(0, 2, 1)
print(memoria)
memoria.CheckAvailMemory(0, 30, 2)
print(memoria)
memoria.CheckAvailMemory(0, 32, 3)
print(memoria)
memoria.cleanMemory(30,2,0)
print(memoria)    