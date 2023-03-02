# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

a = int(input('Me informe o comprimento de uma reta A: '))
b = int(input('Agora o B: '))
c = int(input('Finalmente o C: '))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        tipo_triangulo = 'EQUILÁTERO'
    elif a != b != c != a:
        tipo_triangulo = 'ESCALENO'
    else: 
        tipo_triangulo = 'ISÓSCELES'
    print(f'É possível formar um triângulo {tipo_triangulo} com essas retas')
else:
    print('Não é possível formar um triângulo com essas retas')