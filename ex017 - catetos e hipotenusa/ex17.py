from math import pow, sqrt

def calc_hipotenusa(c1, c2):
    hipotenusa = sqrt(pow(c1, 2) + pow(c2, 2))
    return hipotenusa

cateto1 = int(input('Digite o valor do primeiro cateto: '))
cateto2 = int(input('Digite o valor do segundo cateto: '))
print(f'A hipotenusa vale {calc_hipotenusa(cateto1, cateto2):.2f}')