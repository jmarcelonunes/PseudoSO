"""
	Resources Module

	Module related to I/O devices, especifically 1 scanner, 2 printers, 
	1 modem and 2 SATA disks. Only user processes can have access to these 
	services. Mutual exclusion between the processes is implemented.
"""

class ResourceManager:

	def __init__(self):
		# A resource with value of 0 means it's free, otherwise it's being used
		self.resources = {'scanner': 0, 'printers': [0, 0], 'modem': 0, 'disks': [0, 0]}

	def resources_availability(self, proc_descr):
		"""
			Verifies if the process has permission to allocate the resources (if it's 
			a real-time or not) and if the resources are available or not, returning 
			error messages.
			returns:
				err_msgs ('list') error messages
		"""
		err_msgs = []

		# Check if it is a real-time process trying to allocate a resource
		if proc_descr['priority'] == 0 and (proc_descr['scanner'] or proc_descr['modem'] \
						or proc_descr['printer_cod'] or proc_descr['disk_cod']):
			err_msgs.append('Processos de tempo real não podem alocar recursos.')
			return err_msgs

		# Since it's not a real-time process, let's verify the resources availability
		proc_printer_idx = proc_descr['printer_cod'] -1
		proc_disk_idx = proc_descr['disk_cod'] -1
		if proc_descr['scanner'] and self.resources['scanner']:
			err_msgs.append('Scanner ocupado, não foi possível alocar este recurso.')
		if proc_descr['modem'] and self.resources['modem']:
			err_msgs.append('Modem ocupado, não foi possível alocar este recurso.')
		if proc_descr['printer_cod'] and self.resources['printers'][proc_printer_idx]:
			err_msgs.append(f'Impressora {proc_descr["printer_cod"]} ocupada, não foi possível alocar este recurso.')
		if proc_descr['disk_cod'] and self.resources['disks'][proc_disk_idx]:
			err_msgs.append(f'Disco {proc_descr["disk_cod"]} ocupado, não foi possível alocar este recurso.')
		return err_msgs

	def allocate(self, process):
		"""
			Allocates all the resources the process is requesting. It's assumed
			that the resources_availability() was already called.
			Args:
				process ('obj') a Process.
		"""
		proc_printer_idx = process.printer_cod -1
		proc_disk_idx = process.disk_cod -1
		self.resources['scanner'] = process.scanner
		self.resources['modem'] = process.modem
		if process.printer_cod > 0:
			self.resources['printers'][proc_printer_idx] = 1
		if process.disk_cod > 0:
			self.resources['disks'][proc_disk_idx] = 1

	def free(self, process):
		"""
			Deallocates every resource used by the process.
		"""
		if process.scanner:
			self.resources['scanner'] = 0
		if process.modem:
			self.resources['modem'] = 0
		if process.printer_cod > 0:
			self.resources['printers'][process.printer_cod -1] = 0
		if process.disk_cod > 0:
			self.resources['disks'][process.disk_cod -1] = 0

