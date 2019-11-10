'''
	Módulo de Processos: carregamento dos dados do arquivo processes.txt e 
	disponibilização em forma textual de cada processo.

	Exemplos de uso deste módulo:

	1) Carregar de um arquivo os dados dos processos:
		1.1) processos = read_processes()
		1.2) processos = read_processes('/home/aluno/SO/dados_processos.txt')

	2) Recuperar em forma textual as informações de um processo e impressão via console:
		print(processos[0])
'''

import re

# Classe que contém todos os dados de um processo
class Processo():
	def __init__(self, tempoInit, prioridade, tempoProcessar, numBlockMem, \
					codImpressora, reqScanner, reqModem, codDisco):
		self.tempoInit = tempoInit
		self.prioridade = prioridade
		self.tempoProcessar = tempoProcessar
		self.numBlockMem = numBlockMem
		self.codImpressora = codImpressora
		self.reqScanner = reqScanner
		self.reqModem = reqModem
		self.codDisco = codDisco
	# Formato textual dos dados atuais do processo. Pode ser utilizado pelo dispatcher.
	def __str__(self):
		txt = 'offset: ' + str(self.tempoInit) + '\n'
		txt += 'blocks: ' + str(self.numBlockMem) + '\n'
		txt += 'priority: ' + str(self.prioridade) + '\n'
		txt += 'time: ' + str(self.tempoProcessar) + '\n'
		txt += 'printers: ' + str(self.codImpressora) + '\n'
		txt += 'scanners: ' + str(self.reqScanner) + '\n'
		txt += 'modems: ' + str(self.reqModem) + '\n'
		txt += 'drivers: ' + str(self.codDisco)
		return txt


# Retorna uma lista com a instância de todos os Processos do arquivo .txt informado.
# Cada linha do arquivo deve seguir o padrão: int, int, int, int, int, int, int, int
# Sendo que, em ordem, cada valor int representa: <tempo de inicialização>, <prioridade>, 
# <tempo de processador>, <blocos em memória>, <número-código da impressora requisitada>, 
# <requisição do scanner>, <requisição do modem>, <número-código do disco>
def read_processes(filename='processes.txt'):
	processes = []
	with open(filename, 'r') as arquivo:
		line = re.sub('(\n|\r|\t| )*', '', arquivo.readline()) # Removemos \n, \r, \t e espaços de cada linha
		d = line.split(',') # d: dados de um processo. Nome suscinto de variável, mas prático para a operação seguinte.
		processes.append(Processo(int(d[0]), int(d[1]), int(d[2]), int(d[3]), int(d[4]), int(d[5]), int(d[6]), int(d[7])) )
	return processes

