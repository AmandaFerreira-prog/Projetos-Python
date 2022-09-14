def area(largura,comprimento):
    tam=largura*comprimento
    print(f'A área de um terreno {largura}X{comprimento} é de {tam}m2.')


print('Controle de Terrenos')
print('-'*30)
area(float(input('Largura (m): ')),
     float(input('Comprimento (m): ')))
