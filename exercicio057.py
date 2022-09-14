sexo = input('Informe seu sexo [M/F]: ').strip().upper()[0]
while sexo!='M' and sexo!='F':
        sexo=input(('Dados invalidos. Por favor, informe o seu Sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))

