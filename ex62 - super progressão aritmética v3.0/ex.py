# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro = int(input('Digite o primeiro termo de uma P.A: '))
razao = int(input('Agora, informe a razão: '))
termo = primeiro
cont = 1
adicional = 10
total = 0
while adicional != 0:
    total = total + adicional
    while cont <= total:
        print(termo, end=' -> ')
        termo += razao
        cont += 1
    print('PAUSA')
    adicional = int(input('\nQuantos termos você quer mostrar a mais? '))

print(f'Progressão finalizada com {total} termos')
