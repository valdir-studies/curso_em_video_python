# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = (
    "Batata", 1,
    "Azeite", 3.50,
    "Carne", 10.90
)
print('=-' * 20)

for posicao in range(0, len(listagem)):
    if posicao % 2 == 0:
        print(f"{listagem[posicao]:.<30} R${listagem[posicao + 1]:>7.2f}")

print('=-' * 20)