from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('\033[1;31m-='*10,'VAMOS BRINCAR!!','-='*10)
print('\033[0;33mSuas opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA\033[m')
jogador=int(input('\033[1;31mQual a sua opção? '))
print('\033[1;34mJO')
sleep(1)
print('KEN')
sleep(1)
print('PO !!!\033[m')
print('-=\033[0;31m'*20)
print('\033[0;33mComputador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=\033[0;31m'*20)
if jogador==computador:
    print('\033[1;34mEMPATE!!')
elif computador==0:
    if jogador==1:
        print('\033[1;34mVOCÊ VENCEU!!')
    if jogador==2:
        print('\033[1;34mCOMPUTADOR GANHOU.')
elif computador==1:
    if jogador==0:
        print('\033[1;34mCOMPUTADOR GANHOU!!')
    if jogador==2:
        print('\033[1;34mVOCÊ VENCEU!!')
elif computador==2:
    if jogador==0:
        print('\033[1;34mVOCÊ VENCEU!!')
    if jogador==1:
        print('\033[1;34mCOMPUTADOR GANHOU!!')
