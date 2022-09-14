cont=0
lista=[]
while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    op=input('Quer continuar? [S/N] ' ).upper()
    if op=='N':
        break
print(f'Voce digitou {cont} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista.')
