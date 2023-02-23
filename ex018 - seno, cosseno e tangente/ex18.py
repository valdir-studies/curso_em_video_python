from math import tan, sin, cos, radians

angulo = float(input('Digite o ângulo: '))

print(f'O seno de {angulo}° é {sin(radians(angulo)):.2f}, o cosseno é {cos(radians(angulo)):.2f} e a tangente é {tan(radians(angulo)):.2f}')