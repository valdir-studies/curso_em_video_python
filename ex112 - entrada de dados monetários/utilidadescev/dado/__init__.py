def leia_dinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'Erro! \"{entrada}\" é um preço inválido!')
        else: 
            valido = True
            return float(entrada)
        