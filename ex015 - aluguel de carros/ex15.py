# Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
# Adaptação -> O usuário pode decidir quais são os custos

def aluguel_valor(custo_dia, custo_km, qtd_dias, qtd_km):
    return custo_dia * qtd_dias + custo_km * qtd_km

custo_dia = float(input('Digite o custo por dia em reais: R$'))
custo_km = float(input('Digite o custo por km em reais: R$'))
qtd_dias = int(input('Quantos dias foram alugados? '))
qtd_km = int(input('Quantos km foram rodados? '))

print(f'O custo para esse aluguel foi de R${aluguel_valor(custo_dia, custo_km, qtd_dias, qtd_km):.2f}')
