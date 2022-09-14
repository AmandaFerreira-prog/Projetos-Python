'''from datetime import date


def voto(dado):
    idade=atual-dado
    print(f'Com {idade} anos:',end=' ')
    if 70>idade>=18:
        print('VOTO OBRIGATÓRIO')
    elif 18>idade>=16 or idade>=70:
        print('VOTO OPCIONAL')
    elif idade<16:
        print('VOTO NEGADO.')


atual=date.today().year
print('-'*20)
voto(int(input('Em que ano você nasceu? ')))'''


def voto(ano):
    from datetime import date
    atual=date.today().year
    idade=atual-nasc
    if idade<16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif 70>idade>=18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'


nasc=int(input('Em que ano você nasceu? '))
print(voto(nasc))