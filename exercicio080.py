'''lista=[]
maior=menor=0
for c in range (0,5):
    n=(int(input('Digite um valor:')))
    lista.append(n)
    if c==0:
        maior=menor=n
        print('Adicionado ao final da lista...')
    if c>0:
        if n>maior:
            print('Adicionado ao final da lista...')
        if n<menor:
            print('Adicionado a posição 0 da lista...')
        if n>menor and n <maior:
            print('Adicionado a posição 1 da lista...')
    c+=1
print('-=-'*20)
lista.sort()
print(f'Os valores digitados foram {lista}')'''

'''lista=[]
maior=menor=0
for c in range(0,5):
    n=int(input('Digite um valor: '))
    if c==0:
        lista.append(n)
        print('Adicionado ao final da lista...')
        maior=menor=n
    elif c>0 and n>maior:
        maior = n
        lista.insert(4,n)
        print('Adicionado ao final da lista...')
    elif c>0 and  n<menor:
        menor = n
        print('Adicionado a posição 0 da lista...')
        lista.insert(0,n)
    else:
        print('Adicionado a posição 1 da lista...')
        lista.insert(1,n)
    c+=1
print('-=-'*20)
print(f'Os valores digitados foram {lista}'''

lista=[]
for c in range(0,5):
    n=int(input('Digite um valor: '))
    if c==0 or n>lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        p=0
        while p<len(lista):
            if n<=lista[p]:
                lista.insert(p,n)
                print(f'Adicionado a posição {p} da lista...')
                break
            p+=1
print('-=-'*20)
print(f'Os valores digitados foram {lista}')
