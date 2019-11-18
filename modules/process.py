# -*- coding: utf-8 -*-
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
		self.exec_time = total_exec_time #contador do tempo de cpu
		self.blocks = blocks
		self.printer_cod = printer_cod
		self.scanner = scanner
		self.modem = modem
		self.disk_cod = disk_cod
		# pid deve ser atribuído pelo gerenciador de processos
		self.pid = pid
		self.instructions = {}
		self.intructions_pc = 0
		self.running = False # processo está na memória ou não
		self.new = True
		
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
	processes = {}
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
		processes[key] = new_process
	return load_instructions(files_txt, processes)

def load_instructions(filename, processes):

	with open(filename, 'r') as fp:
		fp.readline()
		quant_files = int(fp.readline())
		for _ in range(quant_files):
			next(fp)
		for line in fp:
			line = line.strip()
			data = line.split(',')
			process_id = int(data[0])
			operation = int(data[1])
			filename = data[2].strip()
			if len(data) == 5:
				filesize = int(data[3])
				pc = int(data[4])
				inst = Instruction(
					operation = operation,
					filename = filename,
					filesize = filesize
				)
			else:
				pc = int(data[3])
				inst = Instruction(
					operation = operation,
					filename = filename
				)
			if process_id in processes:
				processes[process_id].instructions[pc] = inst
	return processes

def processes_by_init_time(processes):
	process_by_init_time = {}
	for key in processes.keys():
		p = processes[key]
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

