import memory
try:
    print("Hello World!")
    memoria = memory.Memory()
    memoria.create_process(1,0,70)
    print(memoria)
    memoria.create_process(2,0,30)
    print(memoria)
    memoria.create_process(3,0,32)
    print(memoria)
    memoria.delete_process(2,0)
    print(memoria)
    memoria.delete_process(1,0)
    print(memoria)
    memoria.delete_process(3,0)
    print(memoria)
except Exception as e: 
    print(e)