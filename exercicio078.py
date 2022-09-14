'''v=[int(input('Digite um valor para a posição 0: ')),int(input('Digite um valor para a posição 1: ')),
    int(input('Digite um valor para a posição 2: ')),int(input('Digite um valor para a posição 3: ')),int(input('Digite um valor para a posição 4: '))]
print('-=-'*20)
print(f'Voce digitou os valores: {v}')
maior=menor=cont=0
for n in v:
    if cont==0:
        maior=menor=n
    elif n>maior:
        maior=n
    elif n<menor:
        menor=n
    cont+=1
print(f'O maior valor digitado foi {maior} e esta na posição  ',end='')
for i,c in enumerate(v):
    if c==maior:
        print(f'{i}...',end=' ')
print(f'\nO menor valor digitado foi {menor}  e esta na posição',end=' ')
for p,c in enumerate(v):
    if c==menor:
        print(f'{p}...',end=' ')'''

maior=menor=0
lista=[]
for n in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {n}: ')))
    if n==0:
        maior=menor=n
    else:
        if lista[n]>maior:
            maior=lista[n]
        elif lista[n]<menor:
            menor=lista[n]
print(f'Voce digitou os valores: {lista}')
print(f'O maior valor digitado foi {maior} e ele esta na posição ',end=' ')
for p,v in enumerate(lista):
    if v==maior:
        print(f'{p}...',end=' ')
print(f'\nO menor valor digitado foi {menor} e ele esta na posição ',end=' ')
for p,v in enumerate(lista):
    print(f'{p}...',end=' ')
