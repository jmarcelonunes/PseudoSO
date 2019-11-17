# -*- coding: utf-8 -*-
"""
	Queue module
	
	Priority queues to store ready processes. The limit is 1000 processes, 
	FIFO scheduling, real-time processes have 0 priority, which is the highest. 
	User processes have 3 priority queues (1, 2 and 3), with refeed. To avoid 
	starvation it's used the aging technique.
"""

from modules.process import Process


class ProcessesQueue():
	'''Ready processes queue'''

	def __init__(self):
		# Max number of processes
		self.max_procs = 1000
		# Total number of processes in the queue
		self.queue_size = 0
		# Queue where the keys are the processes priorities and the values are
		# lists of processes, one list per key
		self.queue = {0:[], 1:[], 2:[], 3:[]}

	def _is_queue_free(self):
		"""
			Verifies if the queue has a slot for the process. For internal use.

			Returns:
				isFree ('bool')
		"""
		return self.queue_size < self.max_procs

	def add(self, process):
		"""
			Adds a process at the end of the queue according to it's priority.

			Returns:
				added ('bool')
		"""
		if(self._is_queue_free()):
			self.queue[process.priority].append(process)
			self.queue_size += 1
			return True
		return False

	def remove(self, process):
		pass

	def process_aging(self):
		"""
			Updates the priority of the processes at index 0 in the lists of
			priority 2 and 3.
		"""
		if len(self.queue[2]) > 0:
			proc = self.queue[2].pop(0)
			proc.priority -= 1
			self.add(proc)
		if len(self.queue[3]) > 0:
			proc = self.queue[3].pop(0)
			proc.priority -= 1
			self.add(proc)

	def get_next(self):
		"""
			The next process of the queue according to the priority. Processes 
			with priority 0 first, then 1 until 3. The process is returned and
			the queue stays unchanged.

			Returns:
				Process ('obj') next Process with the highest priority in the queue
				or None if there is no process.
		"""
		for k in self.queue.keys():
			if len(self.queue[k]) == 0:
				continue
			return self.queue[k][0]
		return None

	def next(self):
		for k in self.queue.keys():
			if len(self.queue[k]) == 0:
				continue
			self.queue_size -= 1
			return self.queue[k].pop(0)
		return None

class BlockedQueue():

	def __init__(self, resources):
		self.blocked = []
		self.resources = resources

	def push(self, process):
		self.blocked.append(process)

	def pop(self):
		if len(self.blocked) > 0:
			return self.blocked.pop(0)
		else:
			return None

	def pop_ready(self):
		ready = []
		for idx, b in enumerate(self.blocked):
			try:
				self.resources.allocate(b)
				ready.append(b)
				self.blocked[idx] = None
			except:
				continue
		self.blocked = [b for b in self.blocked if b is not None]
		return ready