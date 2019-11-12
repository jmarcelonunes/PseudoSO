import memory

print("Hello World!")
memoria = memory.Memory()
memoria.check_and_allocate(0, 2, 1)
print(memoria)
memoria.check_and_allocate(0, 30, 2)
print(memoria)
memoria.check_and_allocate(0, 32, 3)
print(memoria)
memoria.delete_process(30,2,0)
print(memoria)    