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
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')

            print(f'{dado[0]:<20} {dado[1]:>3} anos')
        print(a.read())
    finally: a.close()

def cadastrar(path, nome='desconhecido', idade=0):
    try:
        a = open(path, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        a.write(f'{nome};{idade}\n')
        print('Novo registro adicionado!')
        a.close()