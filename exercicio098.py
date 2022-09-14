def contagem(i,f,p):
    if p<0:
        p*=-1
    if p==0:
        p=1
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    if i <= f:
        for c in range(i,f+1,p):
            print(c,end=' ')
            sleep(0.5)
            c += 1
    else:
        c=i
        while c>=f:
            print(c,end=' ')
            sleep(0.5)
            c-=p
    print('Fim!')


from time import sleep
print('-=-'*15)
print('Contagem de 1 até 10 de 1 em 1')
for c in range(1,11):
    print(c,end=' ')
    sleep(0.5)
    c+=1
print('FIM!')
print('-=-'*15)
print('Contagem de 10 até 0 de 2 em 2.')
for c in range(10,-1,-2):
    print(c,end=' ')
    sleep(0.5)
    c+=1
print('FIM!')
print('-=-'*15)
print('Agora é a sua vez de personalizar a contagem!!')
inicio=int(input('Início: '))
fim=int(input('Fim: '))
passo=int(input('Passo: '))
print('-=-'*15)
contagem(inicio,fim,passo)

