def ficha(nome='Desconhecido',gols=0):
    if nome=='':
        nome='Desconhecido'
    return f'O jogador {nome} fez {gols} gols no campeonato.'


jogador=input('Nome do jogador: ')
gol=str(input('Número de gols: '))
if gol.isnumeric():
    gol=int(gol)
else:
    gol=0
print(ficha(jogador,gol))