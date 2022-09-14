from time import sleep
opcao=0
maior=0
while opcao!=5:
    n1=int(input('Primeiro valor: '))
    n2=int(input('Segundo valor: '))
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    opcao=int(input('>>>>>> Qual é a sua opção? '))
    if opcao!=1 and opcao!=2 and opcao!=3 and opcao!=4 and opcao!=5:
        print('Opção inválida. Tente novamente.')
        opcao = int(input('>>>>>> Qual é a sua opção? '))
    if opcao==1:
        print('A soma entre {} + {} é {}.'.format(n1,n2,n1+n2))
    elif opcao==2:
        print('A multiplicação entre {} X {} é {}.'.format(n1,n2,n1*n2))
    elif opcao==3:
        if n1>n2:
            maior=n1
        elif n2>n1:
            maior=n2
        print('O maior número entre {} e {} é {}'.format(n1,n2,maior))
    elif opcao==4:
        print('Informe seus números novamente.')
    print('-=='*15)
print('Finalizando...')
print('-=='*15)
sleep(0.5)
print('Fim do programa, volte sempre!!')