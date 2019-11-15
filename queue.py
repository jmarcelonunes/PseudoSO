"""
	Queue module
	
	Priority queues to store ready processes. The limit is 1000 processes, 
	FIFO scheduling, real-time processes have 0 priority, which is the highest. 
	User processes have 3 priority queues (1, 2 and 3), with refeed. To avoid 
	starvation it's used the aging technique.
"""

from process import Process


class ProcessesQueue():
	'''Ready processes queue'''

	def __main__(self, processes : list):
		# Max number of processes
		self.max_procs = 1000
		# Queue where the keys are the processes priorities and the values are
		# lists of processes, one list per key
		self.queue = _list_to_queue(processes[:self.max_procs])

	def _is_queue_free(self, priority):
		"""
			Verifies if the queue has a slot for the process. For internal use.

			Returns:
				isFree ('bool')
		"""
		return len(self.queue[priority]) < self.max_procs

	def add(self, process):
		"""
			Adds a process at the end of the queue according to it's priority.

			Returns:
				added ('bool')
		"""
		if(is_queue_free(process.priority)):
			self.queue[process.priority].append(process)
			return True
		return False

	# Retorna e remove da Fila o próximo processo a ser executado.
	# Armazena dados estatísticos para saber quantas vezes este
	# processo foi executado. <-------------
	def next(self):
		"""
			The next process of the queue according to the priority. Processes 
			with priority 0 first, then 1 until 3. The process is removed from
			the queue and returned to the caller block.

			Returns:
				Process ('obj') next Process with the highest priority in the queue
				or None if there is no process.
		"""
		for k in self.queue.keys():
			if len(self.queue[k]) == 0:
				continue
			return self.queue[k].pop(0)
		return None


	def aging(self):
		"""
			TODO
			Technique to avoid starvation. The older the process is, more priority
			it takes. Every 7 clocks the user processes that were not executed will
			gain 1 more priority level until they have priority 1, the maximum for
			a user process.
		"""

def _list_to_queue(processes : list):
	"""
		Takes a list of processes and transforms into a dictionary, which is 
		the own queue. For internal use. The processes are ordered by init_time
		attribute, in an ascending order. It takes the first 1000 processes from
		the list and ignores the rest.
	"""
	dic = {0: [], 1: [], 2: [], 3: []}
	for proc_descr in processes[:1000]:
		dic[proc_descr['priority']].append(proc_descr)
	# Sort the processes by their initialization time, ascending order.
	for k in dic.keys():
		dic[k].sort(key=lambda process: process['init_time'])
	return dic


