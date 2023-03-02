# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

altura = float(input('Digite sua altura (em m): ').replace(',', '.'))
massa = float(input('Digite seu peso (em kg): '))

imc = massa / (altura * altura)

if imc > 40:
    situacao = 'Obesidade mórbida'
elif 40 >= imc > 30:
    situacao = 'Obesidade'
elif 30 >= imc > 25:
    situacao = 'Sobrepeso'
elif 25 >= imc >= 18.5:
    situacao = 'Peso Ideal'
else: 
    situacao = 'Abaixo do peso'

print(f'Pesando {massa}kg com {altura}m, seu IMC é de {imc:.1f} - Portanto, você está na faixa {situacao.upper()}!')
