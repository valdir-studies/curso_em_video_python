# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

preco = float(input('Qual é o preço das compras? R$'))
opcao_pag = int(input('\nFORMAS DE PAGAMENTO\n\n1- À vista com dinheiro/cheque\n2- À vista no cartão\n3- 2x no cartão\n4- 3x ou mais no cartão\n\nInsira a opção correspondente: '))

match opcao_pag:
    case 1:
        novo_preco = preco * 0.9
    case 2:
        novo_preco = preco * 0.95
    case 3:
        novo_preco = preco
        qtd_parcelas = 2
        parcela = novo_preco / qtd_parcelas
    case 4:
        novo_preco = 1.2 * preco
        qtd_parcelas = int(input('\nQuantas parcelas? '))
        parcela = novo_preco / qtd_parcelas
    case _:
        print('A opção inserida não é válida!')
        exit()

print(f'\nO novo valor será de R${novo_preco:.2f}', end='')

if parcela: 
    print(f' em {qtd_parcelas}x de R${parcela:.2f}')