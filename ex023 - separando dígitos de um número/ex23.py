num = int(input('Digite um número de 0 a 9999: ').strip().replace(" ", ""))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Unidades: {u}')
print(f'Dezenas: {d}')
print(f'Centenas: {c}')
print(f'Milhares: {m}')