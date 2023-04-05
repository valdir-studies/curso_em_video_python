# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(msg):
    print('~' * (len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4))


escreva('Bom dia!')
escreva('Esse é um print especial e muito necessário!')
escreva('Bruna, eu sei que você não me quer, mas eu te amo! :(')
