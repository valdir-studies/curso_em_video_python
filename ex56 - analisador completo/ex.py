# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma = 0
cont_mulheres_novineas = 0
maior_idade = 0

for i in range(1, 5):
    print(f'{i}ª PESSOA')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper().strip()

    #Compara maior idade
    if i == 1 and sexo == 'M':
        maior_idade = idade
        nome_maior_idade = nome
    else: 
        if idade > maior_idade and sexo == 'M':
            maior_idade = idade
            nome_maior_idade = nome
    
    #Calcula média
    soma = soma + idade
    media = soma / 4
    
    #Conta as mulheres com menos de 20 anos
    if sexo == 'F' and idade < 20:
        cont_mulheres_novineas = cont_mulheres_novineas + 1
    
print(f'O homem mais velho tem {maior_idade} anos e se chama {nome_maior_idade}')
print(f'A média de idade do grupo é de {media:.2f} anos')
print(f'Ao todo, temos {cont_mulheres_novineas} mulheres com menos de 20 anos')
