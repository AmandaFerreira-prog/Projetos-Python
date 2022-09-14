print('-=-'*10)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=-'*10)
from random import randint
computador= randint(0,11)
v=0
while True:
    jogador=int(input('Digite um valor: '))
    opcao=input('Par ou Impar: [P/I]? ').upper()
    print('-'*30)
    soma=jogador+computador
    if soma%2==0:
        res='DEU PAR'
    else:
        res='DEU IMPAR'
    print(f'Voce jogou {jogador} e o computador {computador}. Total de {soma} {res}')
    print('-'*30)
    if opcao=='P' and soma%2==0 or opcao=='I' and soma%2==1:
        print('Voce VENCEU!')
        print('Vamos jogar novamente...')
        v+=1
    elif (opcao=='P' and soma%2==1) or (opcao=='I' and soma%2==0):
        break
    print('-=-' * 10)
print('Voce PERDEU.')
print('-=-'*10)
print(f'GAME OVER! Você venceu {v} vezes.')