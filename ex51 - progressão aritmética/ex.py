# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

def termos_pa(primeiro, razao):
    decimo = primeiro + 9 * razao
    for primeiro in range(primeiro, decimo + razao, razao):
        print(primeiro)

termos_pa(0, 10)
# 0, 10, 20, 30, 40, 50, 60, 70, 80, 90
