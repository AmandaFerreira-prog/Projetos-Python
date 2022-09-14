n=cont=soma=maior=menor=0
per=str
while per!='N':
    n=int(input('Digite um número: '))
    per=input('Quer continuar? [S/N] : ').upper()
    cont+=1
    soma+=n
    if cont==1:
        maior=n
        menor=n
    if cont>1:
        if n>maior:
            maior=n
        elif n<menor:
            menor=n
media=soma/cont
print('Voce digitou {} números e a media foi {}.'.format(cont,media))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior,menor))

