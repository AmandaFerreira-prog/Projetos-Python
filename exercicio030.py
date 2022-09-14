n=int(input('\033[0;35mMe diga um número qualquer: \033[m'))
if n%2==0:
    print('O número {} é \033[0;34mPar\033[m'.format(n))
else:
    print('O número {} é \033[34mImpar'.format(n))