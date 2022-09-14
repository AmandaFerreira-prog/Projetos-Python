num=int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] CONVERTER PARA BINÁRIO')
print('[ 2 ] CONVERTER PARA OCTAL')
print('[ 3 ] CONVERTER PARA HEXADECIMAL')
opcao=int(input("Sua opção: "))
if opcao==1:
    print('{} convertido para BINARIO é igual a {}'.format(num,bin(num)[2:]))
elif opcao==2:
    print('{} convertido para OCTAL é igual a {}'.format(num,oct(num)[2:]))
elif opcao==3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num,hex(num)[2:]))
else:
    print('OPÇÃO INVALIDA')