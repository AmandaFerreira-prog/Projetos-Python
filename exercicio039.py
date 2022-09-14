from datetime import date
ano=int(input('Ano de nascimento:'))
idade=date.today().year-ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano,idade,date.today().year))
if idade<18:
    tempo=18-idade
    print('Ainda faltam {} anos para seu alistamento'.format(tempo))
    print('Seu alistamento será em {}.'.format(date.today().year + tempo))
elif idade>18:
    tempo=idade-18
    print('Voce ja deveria ter se alistado há {} anos'.format(tempo))
    print('Seu alistamento foi em {}.'.format(date.today().year-tempo))
else:
    print('Voce tem que se alistar IMEDIATAMENTE.')