'''from time import sleep


def ajuda(m):
    sleep(0.3)
    print('\033[30;44m~'*40)
    print(f'Acessando o manual do comando {m}')
    print(f'{"~"*40}')
    sleep(1)
    print(f'{help(m)}')


print('\033[1;30;42m-'*30)
print('SISTEMA DE AJUDA PyHELP')
print('-'*30)
while True:
    r= input('\033[mFunção ou Biblioteca: ').lower()
    if r=='fim':
        break
    else:
        ajuda(r)
        print('\033[1;30;42m-' * 30)
        print('SISTEMA DE AJUDA PyHELP')
        print('-' * 30)
print('\033[30;41~'*30)
print('VOLTE SEMPRE!!!')
print('~'*30)'''


from time import sleep
c=('\033[m','\033[0;30;41m','\033[0;30;42m','\033[0;30;43m','\033[0;30;44m','\033[0;30;45m','\033[7;30m')


def ajuda(m):
    titulo(f'Acessando o manual do comando {m}',4)
    print(c[6],end='')
    help(m)
    print(c[0],end='')
    sleep(1)


def titulo(msg,cor=0):
    tam=len(msg)+4
    print(c[cor],end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0],end='')
    sleep(1)

while True:
    titulo('SISTEMA DE AJUDA PyHELP',2)
    r= input('Função ou biblioteca: ').lower()
    if r=='fim':
        break
    else:
        ajuda(r)
titulo('VOLTE LOGO!!!',1)