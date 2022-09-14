'''def fatorial(a,show=False):
    """
    -> Calcula o Fatorial de um número.
    :param a: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta
    :return: O fatorial de um número a.
    """
    tot=1
    if op=='S':
        for c in range(a, 0, -1):
            if c==a:
                print(f'{a}={a}',end='')
            else:
                print(f'X{c}', end='')
            tot *= c
        return f'={tot}'
    else:
        for c in range(a,0,-1):
            tot*=c
    return f'{tot}'


n=int(input('Digite um Número: '))
op=input('Mostrar o Cálculo? [S/N]').upper()
print(fatorial(n,op))
help(fatorial)'''


def fatorial(a,show=False):
    """
    -> Calcula o Fatorial de um número.
    :param a: Número a ser calculado.
    :param show: Mostrar ou não o cálculo
    :return: Mostrar o fatorial de um número a.
    """
    tot=1
    for c in range(a,0,-1):
        if show:
            print(c,end='')
            if c>1:
                print('x',end='')
            else:
                print('=',end='')
        tot*=c
    print(tot)


fatorial(5,show=True)
help(fatorial)