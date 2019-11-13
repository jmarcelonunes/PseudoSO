"""
	Carregamento dos dados do arquivo processes.txt.

	Exemplos de uso deste módulo:

	1) Carregar de um arquivo os dados dos processos:
		1.1) processos = read_processes() # Assume que o arquivo 'processes.txt' está no diretório corrente
		1.2) processos = read_processes('/home/aluno/SO/dados_processos.txt')
"""


def read_processes(filename='processes.txt'):
	"""Lê o txt informado e transforma em uma lista de descrição de processos.
		Cada linha do arquivo deve seguir o padrão: int, int, int, int, int, int, int, int
		sendo que, em ordem, cada valor int representa: <tempo de inicialização>, <priority>, 
		<tempo de processador>, <blocos em memória>, <número-código da impressora requisitada>, 
		<requisição do scanner>, <requisição do modem>, <número-código do disco>

		Args:
			filename ('string') Nome/caminho do arquivo txt para ser carregado
		Returns:
			processes_descr ('list') descrição dos processos em uma lista de dicionários
	"""
	processes_descr = []
	attrs = ['init_time', 'priority', 'total_exec_time', 'blocks', 'printer_cod', \
				'req_scanner', 'req_modem', 'disk_cod']
	with open(filename, 'r') as fp:
		for i, line in enumerate(fp):
			# remove \n, \r, \t e espaços que estejam no início ou no fim de cada linha
			line = line.strip()
			data = line.split(',')
			process_info = {k: int(v) for k, v in zip(attrs, data)}
			processes_descr.append(process_info)
	return processes_descr

