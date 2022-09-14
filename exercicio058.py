from random import randint
computador=randint(0,10)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que consegue adivinhar qual foi? ')
palpite=int
tent=0
while palpite!=computador:
    palpite=int(input('Qual o seu palpite? '))
    tent+=1
    if palpite<computador:
        print('Mais... Tente mais uma vez.')
    if palpite>computador:
        print('Menos.. Tente mais uma vez.')
print('Acertou com {} tentativas. Parabens!'.format(tent))