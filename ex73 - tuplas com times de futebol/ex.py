""" Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense. """

times = ('Palmeiras', 'Atlético-MG', 'Fortaleza', 'Bragantino', 'Flamengo',
                    'Athletico-PR', 'Ceará', 'Santos', 'Atlético-GO', 'Bahia',
                    'Corinthians', 'Fluminense', 'Juventude', 'Internacional', 'Cuiabá',
                    'São Paulo', 'Sport', 'América-MG', 'Grêmio', 'Chapecoense')

print(f'\nOs cinco primeiros times são {times[:5]}')
print(f'\nOs últimos 4 colocados são {times[-4:]}')
print(f'\nOs times em ordem alfabética são {sorted(times)}')
print(f'\nO Chapecoense está na {times.index("Chapecoense") + 1}ª posição')