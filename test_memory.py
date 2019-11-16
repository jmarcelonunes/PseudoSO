"""
	Tests for the memory module
"""
from modules import memory
import unittest
class TestMemory(unittest.TestCase):
	
	#Test create_process method
	def test_create_real_time_process(self):	
		mem_test = memory.Memory()
		self.assertEqual(mem_test.create_process(1,0,30), 0, "Should return 0")
		self.assertCountEqual(mem_test.memory_real_time.holes, [{'start': 30, 'length': 34}])
		self.assertCountEqual(mem_test.memory_real_time.processes, [{'start': 0, 'length': 30, 'pid': 1}])
	
	def test_big__real_time_process(self):	
		mem_test = memory.Memory()
		with self.assertRaises(Exception): mem_test.create_process(1,0,70)
		self.assertCountEqual(mem_test.memory_real_time.holes, [{'start': 0, 'length': 64}])
		self.assertEqual(str(mem_test.memory_real_time.processes), "[]")
	
	def test_limit_allocation_real_time(self):
		mem_test = memory.Memory()
		mem_test.create_process(1,0,2)
		mem_test.create_process(1,0,30)
		mem_test.create_process(1,0,32)
		self.assertEqual(str(mem_test.memory_real_time.holes), '[]', "Should be all allocated")
	
	def test_allocation_and_free_real_time(self):
		mem_test = memory.Memory()
		self.assertEqual(mem_test.create_process(1,0,2), 0, "Should return 0")
		self.assertEqual(mem_test.create_process(2,0,30), 0, "Should return 0")
		self.assertEqual(mem_test.create_process(3,0,32), 0, "Should return 0")
		self.assertEqual(mem_test.delete_process(2,0), 0, "Should return 0")
		self.assertEqual(mem_test.delete_process(1,0), 0, "Should return 0")
		self.assertEqual(mem_test.delete_process(3,0), 0, "Should return 0")
		self.assertCountEqual(mem_test.memory_real_time.holes, [{'start': 0, 'length': 64}])
		self.assertCountEqual(mem_test.memory_real_time.processes, [])
	
	def test_create_user_process(self):
		mem_test = memory.Memory()
		self.assertEqual(mem_test.create_process(1,3,100), 0, "Should return 0")
		self.assertCountEqual(mem_test.memory_user.holes, [{'start': 164, 'length': 924}])
		self.assertCountEqual(mem_test.memory_user.processes, [{'start': 64, 'length': 100, 'pid': 1}])

	def test_big_user_process(self):	
		mem_test = memory.Memory()
		with self.assertRaises(Exception): mem_test.create_process(1,2,961)
		self.assertCountEqual(mem_test.memory_user.holes, [{'start': 64, 'length': 1024}])
		self.assertEqual(str(mem_test.memory_user.processes), "[]")

	def test_limit_allocation_user(self):
		mem_test = memory.Memory()
		self.assertEqual(mem_test.create_process(1,2,500), 0, "Should return 0")
		self.assertEqual(mem_test.create_process(2,2,500), 0, "Should return 0")
		self.assertEqual(mem_test.create_process(3,1,24), 0, "Should return 0")
		self.assertEqual(str(mem_test.memory_user.holes), '[]', "Should be all allocated")
	
	def test_allocation_and_free_user(self):
		mem_test = memory.Memory()
		self.assertEqual(mem_test.create_process(1,1,2), 0, "Should return 0")
		self.assertEqual(mem_test.create_process(2,1,30), 0, "Should return 0")
		self.assertEqual(mem_test.create_process(3,3,32), 0, "Should return 0")
		self.assertEqual(mem_test.delete_process(2,1), 0, "Should return 0")
		self.assertEqual(mem_test.delete_process(1,1), 0, "Should return 0")
		self.assertEqual(mem_test.delete_process(3,3), 0, "Should return 0")
		self.assertCountEqual(mem_test.memory_user.holes, [{'start': 64, 'length': 1024}])
		self.assertCountEqual(mem_test.memory_user.processes, [])

if __name__ == '__main__':
    unittest.main()
