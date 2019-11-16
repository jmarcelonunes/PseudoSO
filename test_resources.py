"""
	Some tests of the resources.py module
"""


from resources import ResourceManager
from process import Process

def original_procs():
	return [{'priority': 0, 'printer_cod': 0, 'scanner': 0, 'modem': 0, 'disk_cod': 0}, \
					{'priority': 1, 'printer_cod': 1, 'scanner': 0, 'modem': 0, 'disk_cod': 0}]

procs_descr = original_procs()
resmngr = ResourceManager()

# Teste do método resources_availability()
for i, proc in enumerate(procs_descr):
	print('Verificação de disponibilidade de recursos do processo {i}...')
	assert resmngr.resources_availability(proc) == []

# Processo com prioridade 0 (de tempo real) tentando utilizar scanner
procs_descr[0]['scanner'] = 1
print('\nVerificação de disponibilidade de recursos do processo 0, prioridade 0, scanner 1...')
err_msgs = resmngr.resources_availability(procs_descr[0])
assert len(err_msgs) == 1
print(err_msgs)
procs_descr = original_procs()
err_msgs = []

# Processo com prioridade 0 (de tempo real) tentando utilizar impressora 1
procs_descr[0]['printer_cod'] = 1
print('\nVerificação de disponibilidade de recursos do processo 0, prioridade 0, printer 1...')
err_msgs = resmngr.resources_availability(procs_descr[0])
assert len(err_msgs) == 1
print(err_msgs)
procs_descr = original_procs()
err_msgs = []

# Ambos os processos de usuário, processo 1 com modem, impressora 1 e disco 2 alocados e o processo 0
# verificando se pode alocar o modem e o disco 2
err_msgs = []
procs_descr[0]['priority'] = 3
procs_descr[0]['modem'] = 1
procs_descr[0]['disk_cod'] = 2
process1 = Process(priority=1, printer_cod=1, scanner=0, modem=1, disk_cod=2, init_time=0, total_exec_time=0, blocks=0)
resmngr.allocate(process1)
print("\nVerificação de disponibilidade do modem e do disco para o processo 0...")
err_msgs = resmngr.resources_availability(procs_descr[0])
assert len(err_msgs) == 2
print(err_msgs)
err_msgs = []

# Teste do método free()
resmngr.free(process1)
print("\nVerificação de disponibilidade do modem e do disco para o processo 0 depois de chamar free()...")
err_msgs = resmngr.resources_availability(procs_descr[0])
assert len(err_msgs) == 0
print(err_msgs)

