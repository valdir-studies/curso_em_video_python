def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro! Por favor, digite um número inteiro válido')
            continue
        except KeyboardInterrupt:
            print('\nEntrada de dados interrompida pelo usuário')
            break
        else: return n

def linha(tam = 30):
    return '-' * tam

def cabecalho(txt): 
    print(linha())
    print(txt.center(30))
    print(linha())

def menu(lista):
    cabecalho('Menu principal')
    for i,v in enumerate(lista):
        print(f'{i+1} - {v}')
    print(linha())
    return leia_int('Sua opção: ')
    