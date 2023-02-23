nome = input('Digite seu nome completo: ').strip()

minusculo = nome.lower()
maiusculo = nome.upper()
tamanho = len(nome.replace(" ", ""))
primeiro_nome = nome.split()[0]

print(f'\nSeu nome com letras em maiúsculo fica: {maiusculo}')
print(f'Seu nome com letras em minúsculo fica: {minusculo}')
print(f'Seu nome tem ao todo {tamanho} letras')
print(f'Seu primeiro nome é {primeiro_nome} e ele tem {len(primeiro_nome)} letras')