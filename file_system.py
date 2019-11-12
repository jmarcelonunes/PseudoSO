'''
	Módulo do Sistema de Arquivos:
'''

class FileSystem():
	def __init__(self, filename):
		self.files = []
		with open(filename, 'r') as f:
			self.blocks = int(f.readline())
			quant_files = int(f.readline())
			for i in range(quant_files):
				newFileInfo = f.readline().split(',')
				map(str.strip, newFileInfo)
				newFile = {
					'name' : newFileInfo[0],
					'initialBlock' : int(newFileInfo[1]),
					'fileSize' : int(newFileInfo[2])
				}
				if self.hasSpace(newFile):
					self.files.append(newFile)
				else:
					print("Erro, não foi possível iniciar disco")

	def __str__(self):
		txt = ''
		for f in self.files:
			txt += str(f) + '\n'
		return txt

	def hasSpace(self, fileInfo):
		return True