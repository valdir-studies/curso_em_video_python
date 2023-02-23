from math import hypot

cateto1 = int(input('Digite o valor do primeiro cateto: '))
cateto2 = int(input('Digite o valor do segundo cateto: '))
print(f'A hipotenusa vale {hypot(cateto1, cateto2):.2f}')