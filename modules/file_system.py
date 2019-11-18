# -*- coding: utf-8 -*-
'''
	Módulo do Sistema de Arquivos
'''

'''
	Classe FileSystem
'''
from modules import process

class FileSystem():
    def __init__(self, filename):
        self.disk = []
        self.ftable = {}
        with open(filename, 'r') as f:
			# Leitura de parâmetros do sistema de arquivos
            disk_size = int(f.readline())
            self.disk =  disk_size * [None]

			# Criação dos arquivos iniciais
            quant_files = int(f.readline())
            for _ in range(quant_files):
                # Obtém informações de cada arquivo
                new_file_info = f.readline().split(',')
                map(str.strip, new_file_info)
                new_file = File(
                    new_file_info[0], # Nome do arquivo
                    int(new_file_info[2]), # Tamanho do arquivo
                    start = int(new_file_info[1]) # Primeiro bloco
                )

                # Adiciona no sistema
                self.__add_file(new_file)

    # Cria a estrutura de arquivo e adiciona no sistema
    def create_file(self, instruction, process):
        name = instruction.filename
        size = instruction.filesize
        if(name in self.ftable):
            raise Exception("Arquivo com nome inválido")
        else:
            if not self.__add_file(File(name, size, process)):
                raise Exception("O processo %d não pode criar o arquivo %c por falta de espaço" %(process.pid, name))
            file = self.ftable[name]
            return file
    # Deleta um arquivo do sistema pelo nome
    # Além de verificar as permissões de acesso
    def delete_file(self, instruction, process): 
        name = instruction.filename
        if(name not in self.ftable):
            raise Exception("Arquivo não encontrado")
        file = self.ftable[name]
        if( process.priority != 0 and
            file.process != process):
            raise Exception("Processo %d não possui permissão de acesso" % process.pid)
        if not self.__remove_file(file):
            raise Exception("Erro ao remover arquivo %d", name)

    # Adiciona um arquivo no sistema
    def __add_file(self, file):
        if(file.start is None):
            idx = self.__find_space(file.size)
            if idx is not None:
                file.set_start(idx)
            else:
                return False
        
        self.disk[file.start : file.end] =  file.size * file.name
        self.ftable[file.name] = file
        return True

    # Remove um arquivo do sistema
    def __remove_file(self, file):
        if(file.name not in self.ftable):
            return False
        self.disk[file.start : file.end] =  file.size * [None]
        del self.ftable[file.name]
        return True

    # Obtém posição inicial de bloco refêrente a um
    # espaço no disco de determinado tamanho
    def __find_space(self, size):
        space_count = 0
        for idx, f in enumerate(self.disk):
            if f is None:
                space_count += 1
                if space_count == size:
                    return idx - (size - 1)
            else:
                space_count = 0
        return None

    def __str__(self):
        string = 'Mapa de ocupação do disco\n'
        string += '|'
        for idx, block in enumerate(self.disk):
            if idx % 10 == 0:
                string += '\n|'
            if block is None:
                string += ' |'
            else:
                string += block + '|'

        string += '\n'
        return string

class File():
	
    def __init__(self, name, size, process = None, start = None):
        self.name = name
        self.start = start
        self.size = size
        self.process = process
        if start is None:
            self.end = None
        else:
            self.end = start + size

    def set_start(self, idx):
        self.start = idx
        self.end = self.start + self.size