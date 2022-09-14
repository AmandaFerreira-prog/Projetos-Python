jogador={}
jogadores=[]
gols=[]
while True:
    jogador['Nome']=input('Nome do jogador: ')
    Partidas=int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for c in range(1,Partidas+1):
        gols.append(int(input(f'    Quantos gols na partida {c}? ')))
        jogador['Gols'] =gols[:]
    jogador['Total']=sum(gols)
    jogadores.append(jogador.copy())
    op=input('Quer continuar? [S/N] ').upper()
    if op=='N':
        break
    gols.clear()
print('-=-'*30)
print('cod   Nome              Gols         Total')
print('-'*45)
for p,c in enumerate(jogadores):
    print(f'{p:<4}',end='')
    for d in c.values():
        print(f'{str(d):<18}',end='')
escolha=int
while True:
    escolha=int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if escolha==999:
        break
    if escolha>=len(jogadores):
        print(f'ERRO, Nã existe jogador com o codigo {escolha}!')
    else:
        print(f'Levamtamento do jogador {jogadores[escolha]["Nome"]}.')
        



