print('Gerador de PA')
print('-='*15)
p1=int(input('Primeiro termo: '))
razao=int(input('Razão da PA: '))
print(p1, '-> ',end='')
n=1
a1=p1
while n!=10:
    a1=a1+razao
    n+=1
    print(a1,'-> ',end='')
print('Fim')