n=int(input('Digite um número: ')),int(input('Digite outro número: ')),int(input('Digite mais um número: ')),int(input('Digite o ultimo número: '))
print(f'Voce digitou os números: {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3)+1}° posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
par=0
for c in n :
    if c %2==0:
        par+=1
print(f'Voce digitou {par} números pares.')