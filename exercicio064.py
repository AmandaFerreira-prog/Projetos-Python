'''n = int(input('Digite um número [999 para parar]: '))
cont=1
soma=n
while n<999:
    n=int(input('Digite um número: [999 para parar] '))
    soma+=n
    cont+=1
    if n==999:
        soma-=999
        cont-=1
print('Voce digitou {} números e a soma deles é igual a {}.'.format(cont,soma))'''

cont=soma=0
n=int(input('Digite um número [999 para parar]: '))
while n!=999:
    cont+=1
    soma+=n
    n = int(input('Digite um número [999 para parar]: '))
print('Voce digitou {} números e a soma deles é igual a {}.'.format(cont,soma))


