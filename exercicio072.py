num=('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','cartoze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
n=int(input('Digite um número entre 0 e 20: '))
while n<0 or n>20:
    print('Tente novamente.',end='')
    n = int(input('Digite um número entre 0 e 20: '))
print(f'Voce digitou o número {num[n]}')

