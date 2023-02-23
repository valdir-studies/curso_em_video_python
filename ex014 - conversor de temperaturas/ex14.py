def celsius_fahren(temp): 
    return temp * 9/5 + 32

celsius = int(input('Digite a temperatura em graus Celsius: '))
print(f'{celsius}°C para Fahrenheit fica {celsius_fahren(celsius)}°F')