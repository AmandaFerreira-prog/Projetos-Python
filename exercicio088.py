'''print('-'*30)
print('JOGAR NA MEGA-SENA')
print('-'*30)
from random import randint
from time import sleep
n=int(input('Quantos jogos você quer que eu sorteie?'))
print(f'-=-=-=SORTEANDO {n} JOGOS-=-=-=')
jogo=[]
for c in range(1,n+1):
    jogo=[randint(0,60),randint(0,60),randint(0,60),randint(0,60),randint(0,60),randint(0,60)]
    print(f'Jogo {c}: {jogo}')
    sleep(0.5)
print('-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')'''


'''print('-'*30)
print('     JOGAR NA MEGA-SENA     ')
print('-'*30)
from random import randint
from time import sleep
n=int(input('Quantos jogos você quer que eu sorteie?'))
print(f'-=-=-=SORTEANDO {n} JOGOS-=-=-=')
jogo=[]
numeros=[]
cont=0
for c in range(1,n+1):
    while True:
        num=randint(0,60)
        if num not in numeros:
            numeros.append(num)
            cont+=1
        if cont==6:
            break
    print(f'Jogo {c}: {numeros}')
    numeros.clear()
    c+=1
print('-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')'''
