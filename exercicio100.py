'''from random import randint
numeros=[]
pares=0


def sorteia(lista):
    print('Sorteando 5 valores da lista:',end=' ')
    for c in range(0,5):
        lista.append(randint(0,10))
    print(lista,'PRONTO!!')


def somapar(num):
    pares=0
    for par in numeros:
        if par % 2 == 0:
            pares += par
    print(f'Somando os valores pares de {numeros}, temos:{pares}.')


sorteia(numeros)
somapar(pares)'''


from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ',end=' ')
    for c in range(0,5):
        n=randint(0,10)
        print(n,end=' ')
        sleep(0.3)
        lista.append(n)
    print('PRONTO!!!')


def somapar(lista):
    pares=0
    for c in lista:
        if c%2==0:
            pares+=c
    print(f'Somando os valores pares de {lista}, temos:{pares}')

numeros=[]
sorteia(numeros)
somapar(numeros)