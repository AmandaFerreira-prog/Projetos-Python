jogador={}
gols=[]
jogador['Nome']=input('Nome do jogador: ')
ptds=int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
#tot=0
for c in range(0,ptds):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
    #gol=int(input(f'Quantos gols na partida {c}? '))
    #tot+=gol
    #gols.append(gol)
    #jogador['Gols']=gols
jogador['Gols']=gols[:]
jogador['Total']=sum(gols)
print('-=-'*20)
print(jogador)
print('-=-'*20)
for c,v in jogador.items():
    print(f'O campo {c} tem o valor {v}')
print('-=-'*20)
print(f'O jogador {jogador["Nome"]} jogou {ptds} partidas.')
for c,v in enumerate(gols):
    print(f'  => Na partida {c}, fez {v} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')
