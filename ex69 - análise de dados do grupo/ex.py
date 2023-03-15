# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

add_age = add_men = add_women = 0

while True:
    age = int(input("Idade: "))
    if age >= 18:
        add_age += 1
    sex = ' '
    while sex not in 'MF':
        sex = str(input("Sexo [M / F]: ")).strip().upper()
    if sex == "M":
        add_men += 1
    elif sex == "F":
        if age < 20:
            add_women += 1
    choice = str(input("Continuar? [S / N] ")).strip().upper()
    if choice == "N":
        print(f"Pessoas com mais de 18: {add_age}.")
        print(f"Homens cadastrados: {add_men}")
        print(f"Mulheres com menos de 20 anos: {add_women}")
        break
