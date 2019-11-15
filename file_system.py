'''
	Módulo do Sistema de Arquivos
'''

'''
	Classe FileSystem
'''
class FileSystem():
	def __init__(self, filename):
		self.files = []
		with open(filename, 'r') as f:
			self.blocks = int(f.readline())
			quant_files = int(f.readline())
			for _ in range(quant_files):
				new_file_info = f.readline().split(',')
				map(str.strip, new_file_info)
				newFile = {
					'name' : new_file_info[0],
					'initialBlock' : int(new_file_info[1]),
					'fileSize' : int(new_file_info[2])
				}
				if self.has_space(newFile):
					self.files.append(newFile)
				else:
					print("Erro, não foi possível iniciar disco")

	def __str__(self):
		txt = ''
		for f in self.files:
			txt += str(f) + '\n'
		return txt

	def has_space(self, fileInfo):
		return True

class File():

	def __init__(self,name,initialBlock,fileSize, permission):
		self.name = name
		self.initialBlock = initialBlock
		self.fileSize = fileSize
		self.permission = permission