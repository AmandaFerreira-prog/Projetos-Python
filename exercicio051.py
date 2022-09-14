print('='*30)
print('10 Primeiros termos de uma PA.')
print('='*30)
p1=int(input('Primeiro termo:'))
r=int(input('Razão: '))
an=p1+(10-1)*r
for c in range (p1,an+1,r):
    print(c,'-> ',end='')
print('ACABOU')