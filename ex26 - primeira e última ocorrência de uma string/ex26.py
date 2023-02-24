# Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
# Adaptação -> O usuário pode escolher a string monitorada

frase = input('Digite uma frase: ').strip()
caractere = input('Digite uma string a ser monitorada: ').strip()

qtd_ocorrencias = frase.count(caractere)
primeira_ocorrencia = frase.find(caractere) + 1
ultima_ocorrencia = frase.rfind(caractere) + 1

print(f'A string {frase} possui {qtd_ocorrencias} ocorrências do caractere {caractere}')
print(f'A primeira ocorrência é na posição {primeira_ocorrencia} e a última é na {ultima_ocorrencia}')
    