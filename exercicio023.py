n=int(input('Informe um numero: '))
print('Analisando seu numero...')
u=n//1%10
d=n//10%10
c=n//100%10
m=n//1000%10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar:{}'.format(m))
