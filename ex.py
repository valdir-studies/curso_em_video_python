lista_num = []

def persistence(n):
    lista_num.append(n)
    if len(str(n)) == 1:
        print(lista_num)
        return len(lista_num)
    else:
        mult = 1
        for i in str(n):
            mult = mult * int(i)
        return persistence(mult)

print(persistence(4612146))