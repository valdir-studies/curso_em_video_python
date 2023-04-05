"""
Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

– Quantidade de notas
─ A maior nota
─ A menor nota
─ A média da turma
– A situação (opcional)
"""

def notas(*notas, sit=True):
    """
    -> Retorna um dicionário com a situação de um aluno da escola
    :param *notas: As notas do aluno, podem ser inseridas várias
    :param sit (opcional): Informa se a situação do aluno deve ser retornada (REPROVADO/EM RECUPERAÇÃO/APROVADO)
    """
    bol = dict()
    bol['qtd_notas'] = len(notas)
    bol['maior_nota'] = max(notas)
    bol['menor_nota'] = min(notas)
    bol['media'] = sum(notas) / bol['qtd_notas']

    if sit:
        if bol['media'] < 5: bol['sit'] = 'REPROVADO'
        elif bol['media'] <= 7: bol['sit'] = 'EM RECUPERAÇÃO'
        else: bol['media'] = 'APROVADO'
    return bol

print(notas(5,3,2,10,10, sit=True))
