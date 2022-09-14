print('Gerador de PA')
print('-='*15)
p1=int(input('Primeiro termo: '))
razao=int(input('Razão da PA: '))
print(p1, '-> ',end='')
n=1
a1=p1
total=0
mais=10
while mais!=0:
    total= total+mais
    while n!=total:
        a1=a1+razao
        n+=1
        print(a1,'-> ',end='')
    print('PAUSA')
    mais=int(input('Quantos termos a mais você quer mostrar? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))