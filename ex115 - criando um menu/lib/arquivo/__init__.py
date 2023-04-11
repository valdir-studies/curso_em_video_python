from lib.interface import *

def arquivo_existe(path):
    try:
        a = open(path, 'rt')
        a.close()
    except FileNotFoundError: return False
    else: return True

def criar_arquivo(path):
    try:
        a = open(path, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {path} criado com sucesso!')

def ler_arquivo(path):
    try:
        a = open(path, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('Pessoas cadastradas')
        print(a.read())