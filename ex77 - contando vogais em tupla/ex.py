# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Papibaquígrafo',
            'Celular',
            'Katy Perry',
            'Casa',
            'Python',
            'Api',
            'Café',
            'Jogar',
            'Socorro',
            'Livro',
            'Matemática',
            'Sorrir'
)
print('As vogais das palavras da lista são: ')
for i in palavras:
    print(f'\nNa palavra {i.upper()} temos: ', end='')
    for j in i:
        if j.lower() in 'aáãâêéeíiôóoúu':
            print(j, end=' ')
