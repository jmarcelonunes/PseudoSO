"""
	Tests for the memory module
"""
import memory #descobrir como funciona
import unittest
class TestMemory(unittest.TestCase):
	
	#Test create_process method
	def test_create_process(self):	
		mem_test = memory.Memory()
		self.assertEqual(mem_test.create_process(1,0,30), 0, "Should return 0")
		self.assertCountEqual(mem_test.memory_real_time.holes, [{'start': 30, 'length': 34}])
		self.assertCountEqual(mem_test.memory_real_time.processes, [{'start': 0, 'length': 30, 'pid': 1}])
	
	def test_big_process(self):	
		mem_test = memory.Memory()
		with self.assertRaises(Exception): mem_test.create_process(1,0,70)
		self.assertCountEqual(mem_test.memory_real_time.holes, [{'start': 0, 'length': 64}])
		self.assertEqual(str(mem_test.memory_real_time.processes), "[]")
	
	def test_limit_allocation(self):
		mem_test = memory.Memory()
		mem_test.create_process(1,0,2)
		mem_test.create_process(1,0,30)
		mem_test.create_process(1,0,32)
		self.assertEqual(str(mem_test.memory_real_time.holes), '[]', "Should be all allocated")
	
	def test_allocation_and_free(self):
		mem_test = memory.Memory()
		self.assertEqual(mem_test.create_process(1,0,2), 0, "Should return 0")
		self.assertEqual(mem_test.create_process(2,0,30), 0, "Should return 0")
		self.assertEqual(mem_test.create_process(3,0,32), 0, "Should return 0")
		self.assertEqual(mem_test.delete_process(2,0), 0, "Should return 0")
		self.assertEqual(mem_test.delete_process(1,0), 0, "Should return 0")
		self.assertEqual(mem_test.delete_process(3,0), 0, "Should return 0")
		self.assertCountEqual(mem_test.memory_real_time.holes, [{'start': 0, 'length': 64}])
		self.assertCountEqual(mem_test.memory_real_time.processes, [])


if __name__ == '__main__':
    unittest.main()
