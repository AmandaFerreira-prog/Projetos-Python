import random
print('\033[0;34mVou pensar em um número de 0 a 5. Tente advinhar...\033[m')
computador=random.randint(0,5)
n=int(input('Em que número eu pensei?  '))
if n==computador:
    print('PROCESSANDO...')
    print('PARABÉNS! Voce conseguiu me vencer')
else:
    print('PROCESSANDO...')
    print('GANHEI! Eu escolhi o número {} não o {}'.format(computador, n))