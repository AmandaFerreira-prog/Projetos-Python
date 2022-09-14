import random
primeiro=input('Primeiro aluno: ')
segundo=input('Segundo Aluno: ')
terceiro=input('Terceiro Aluno: ')
quarto=input('Quarto aluno: ')
lista=[primeiro, segundo, terceiro, quarto]
print('O aluno escolhido foi {}'.format(random.choice(lista)))