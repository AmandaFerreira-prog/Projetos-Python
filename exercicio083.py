exp=input('Digite a expressão: ')
abertos=exp.count('(')
fechados=exp.count(')')
if abertos==fechados:
    print('Sua exressão esta válida!')
else:
    print('Sua expressão está errada...')