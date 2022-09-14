print('-'*25)
print('Sequencia de Fibonacci')
print('-'*25)
termos=int(input('Quantos termos você quer mostrar? '))
print('~~'*20)
a1=0
a2=1
cont=2
if termos==1:
    print(a1,'-> ',end='')
elif termos==2:
    print(a1,'-> ',a2,'->',end='')
elif termos>2:
    print(a1,'-> ',a2,'-> ',end='')
    while cont!=termos:
        a3 = a1 + a2
        print(a3,'-> ',end='')
        a1=a2
        a2=a3
        cont+=1
print('FIM')
print('~~'*20)
