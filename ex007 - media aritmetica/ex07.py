def media(*args):
    soma = float()
    for n in args:
        soma += n
    
    return soma / len(args)

print(media(10, 20))
