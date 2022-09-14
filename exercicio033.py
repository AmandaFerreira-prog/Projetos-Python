'''menor=0
maior=0
n1=int(input('Primeiro número: '))
menor=maior=n1
n2=int(input('Segundo número: '))
if n2<menor:
    menor=n2
else:
    if n2>maior:
        maior=n2
n3=int(input('Terceiro número: '))
if n3<menor:
    menor =n3
else:
    if n3>maior:
        maior=n3
print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))'''

n1=int(input('Primeiro número: '))
n2=int(input('Segundo número: '))
n3=int(input('Terceiro número: '))
menor=maior=n1
if n2<n1 and n2<n3:
    menor=n2
if n3<n1 and n3<n2:
    menor=n3
if n2>n1 and n2>n3:
    maior=n2
if n3>n1 and n3>n2:
    maior=n3
print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))
