"""
	Carregamento dos dados do arquivo processes.txt.

	Exemplos de uso deste módulo:

	1) Carregar de um arquivo os dados dos processos:
		1.1) processos = read_processes() # Assume que o arquivo 'processes.txt' está no diretório corrente
		1.2) processos = read_processes('/home/aluno/SO/dados_processos.txt')
"""

from processos import Process


def read_processes(filename='processes.txt'):
	"""Lê o txt informado e transforma em uma lista de processos.
		Cada linha do arquivo deve seguir o padrão: int, int, int, int, int, int, int, int
		sendo que, em ordem, cada valor int representa: <tempo de inicialização>, <priority>, 
		<tempo de processador>, <blocos em memória>, <número-código da impressora requisitada>, 
		<requisição do scanner>, <requisição do modem>, <número-código do disco>

		Args:
			filename ('string') Nome/caminho do arquivo texto para ser carregado
		Returns:
			Process ('list')
	"""
	processes = []
	with open(filename, 'r') as fp:
		for i, line in enumerate(fp):
			# remove \n, \r, \t e espaços que estejam no início ou no fim de cada linha
			line = line.strip()
			# d: dados de um processo. Nome suscinto de variável, mas prático para a operação seguinte.
			d = line.split(',')
			processes.append(Process(int(d[0]), int(d[1]), int(d[2]), \
					int(d[3]), int(d[4]), int(d[5]), int(d[6]), int(d[7])) )
	return processes

