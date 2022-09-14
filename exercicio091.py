from random import randint
from operator import itemgetter
from time import sleep
print('Valores sorteados:')
jogadores={'jogador1':randint(1,6),'jogador2':randint(1,6),'jogador3':randint(1,6),'jogador4':randint(1,6)}
for c,a in jogadores.items():
    print(f'{c} tirou {a} no dado.')
    sleep(0.5)
print('-=-'*30)
print('   == RANKING DOS JOGADORES ==')
ranking=[]
ranking=sorted(jogadores.items(),key=itemgetter(1),reverse=True)
for c,v in enumerate(ranking):
    print(f'  {c+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)

