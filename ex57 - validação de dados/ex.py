#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input('Informe seu sexo: ').upper().strip()
while sexo not in 'MF':
    print('O sexo informado não está nas opções, seu burro!')
    sexo = input('Corrija com M para masculino ou F para feminino: ').upper().strip()

print(f'Sexo {sexo} registrado com sucesso!')
