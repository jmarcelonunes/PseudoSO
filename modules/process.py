"""
	Process module: contains the Process and ProcessManager classes. 
"""

from .parser import read_processes

class Process:
	def __init__(self, init_time, priority, total_exec_time, blocks, \
					printer_cod, scanner, modem, disk_cod, pid = -1):
		self.init_time = init_time
		self.priority = priority
		self.total_exec_time = total_exec_time
		self.blocks = blocks
		self.printer_cod = printer_cod
		self.scanner = scanner
		self.modem = modem
		self.disk_cod = disk_cod
		self.pc = self.total_exec_time + self.init_time
		# pid deve ser atribuído pelo gerenciador de processos
		self.pid = pid
		self.instructions = {}
		self.intructions_pc = 0
		self.running = False # processo está na memória ou não
		
	# Formato textual dos dados atuais do processo. Pode ser utilizado pelo dispatcher.
	def __str__(self):
		txt = '\tPID: ' + str(self.pid) + '\n'
		txt += '\toffset: ' + str(self.init_time) + '\n'
		txt += '\tblocks: ' + str(self.blocks) + '\n'
		txt += '\tpriority: ' + str(self.priority) + '\n'
		txt += '\ttime: ' + str(self.total_exec_time) + '\n'
		txt += '\tprinters: ' + str(self.printer_cod) + '\n'
		txt += '\tscanners: ' + str(self.scanner) + '\n'
		txt += '\tmodems: ' + str(self.modem) + '\n'
		txt += '\tdrivers: ' + str(self.disk_cod) + '\n'
		txt += '\tinstructions: ' + str(self.instructions)
		
		return txt


def load_processes(processes_txt,files_txt):
	processes_dict = read_processes(filename = processes_txt)
	processes = []
	for key, p in enumerate(processes_dict):
		new_process = Process(
			p['init_time'], 
			p['priority'], 
			p['total_exec_time'], 
			p['blocks'],
			p['printer_cod'], 
			p['scanner'], 
			p['modem'], 
			p['disk_cod'],
			pid = key
		)
		processes.append(new_process)
	return load_instructions(files_txt, processes)

def load_instructions(filename, processes):

	with open(filename, 'r') as fp:
		quant_files = fp[1]
		fp = fp[(quant_files + 2):]
		for line in fp:
			# remove \n, \r, \t e espaços que estejam no início ou no fim de cada linha
			line = line.strip()
			data = line.split(',')

			process_id = data[0]
			operation = data[1]
			filename = data[2]
			if len(data) == 5:
				filesize = data[3]
				pc = data[4]
				inst = Instruction(
					operation = operation,
					filename = filename,
					filesize = filesize
				)
			else:
				pc = data[3]
				inst = Instruction(
					operation = operation,
					filename = filename
				)
			processes[process_id].instrutions[pc] = inst

	process_by_init_time = {}
	for p in processes:
		if p.init_time in process_by_init_time:
			process_by_init_time[p.init_time].append(p)
		else:	
			process_by_init_time[p.init_time] = [p]

	return process_by_init_time
class Instruction():
	def __init__(self, operation = -1, filename = None, filesize = -1):
		self.operation = operation
		self.filename = filename
		self.filesize = filesize
	
	def __str__(self):
		string = 'Instrução: '
		if self.operation == -1:
			string += 'CPU'
		elif self.operation == 0:
			string += 'Criar arquivo' + self.filename
		elif self.operation == 1:
			string += 'Deleta arquivo' + self.filename
		else:
			string += 'Operação desconhecida'
		return string

class ProcessManager:
	def __init__(self):
		# tempo de cpu total
		self.clock = 0
		# pid que será atribuído ao próximo processo que será criado
		self.new_pid = 0
		# processo atualmente em execução
		self.running_proc = None
		self.running_pid = 0
		# processos que já foram executados
		self.executed_procs = []

	def create_process(self, proc):
		proc.pid = self.new_pid
		self.new_pid += 1
		# aloca o processo na memoria
		self.memmngr.allocate(proc)
		# alloca os recursos do processo 
		self.resmngr.allocate(proc)
		# o processo é adicionado à fia
		self.qmngr.put(proc)

	def next_process(self):
		return None

