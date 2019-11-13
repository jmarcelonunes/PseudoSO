"""
	Módulo de Processos: contém as classes Process e ProcessManager
"""


class Process:
	def __init__(self, init_time, priority, total_exec_time, blocks, \
					print_cod, req_scanner, req_modem, disk_cod, pid=-1):
		self.init_time = init_time
		self.priority = priority
		self.total_exec_time = total_exec_time
		self.blocks = blocks
		self.print_cod = print_cod
		self.req_scanner = req_scanner
		self.req_modem = req_modem
		self.disk_cod = disk_cod
		self.pc = self.total_exec_time + self.init_time
		# pid deve ser atribuído pelo gerenciador de processos
		self.pid = pid
	# Formato textual dos dados atuais do processo. Pode ser utilizado pelo dispatcher.
	def __str__(self):
		txt = '\tPID: ' + str(self.pid) + '\n'
		txt += '\toffset: ' + str(self.init_time) + '\n'
		txt += '\tblocks: ' + str(self.blocks) + '\n'
		txt += '\tpriority: ' + str(self.priority) + '\n'
		txt += '\ttime: ' + str(self.total_exec_time) + '\n'
		txt += '\tprinters: ' + str(self.print_cod) + '\n'
		txt += '\tscanners: ' + str(self.req_scanner) + '\n'
		txt += '\tmodems: ' + str(self.req_modem) + '\n'
		txt += '\tdrivers: ' + str(self.disk_cod)
		return txt


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

