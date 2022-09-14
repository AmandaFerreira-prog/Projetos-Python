'''def notas (*n,sit=False):
    """
    -> Função para analisar notas e situações de vário alunos.
    :param n: Uma ou mais notas dos alunos,(aceita várias).
    :param sit: Valor opcional,indicando se deve mostrar ou não a situação do aluno.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    turma={}
    maior=menor=tot=0
    turma['Total']=len(n)
    cont=1
    for c in n:
        tot+=c
        if cont==1:
            maior=menor=c
        else:
            if c>=maior:
                maior=c
            if c<=menor:
                menor=c
        cont+=1
    media=tot/len(n)
    turma['Maior nota']=maior
    turma['Menor nota']=menor
    turma['Média da turma']=media
    if sit==True:
        if media<6:
            turma['Situação']='Ruim'
        if media>7:
            turma['Situação'] ='Boa'
        if 7>media>=6:
            turma['Situação'] ='Razoavél'
    return turma


resp=notas(5.5,3,sit=True)
help(notas)
print(resp)'''


def notas (*n,sit=False):
    """
    -> Função para analisar notas e situações de vário alunos.
    :param n: Uma ou mais notas dos alunos,(aceita várias).
    :param sit: Valor opcional,indicando se deve mostrar ou não a situação do aluno.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    turma={}
    turma['Total']=len(n)
    turma['Maior nota'] = max(n)
    turma['Menor nota'] = min(n)
    turma['Média da turma'] = sum(n)/len(n)
    if sit == True:
        if turma['Média da turma']< 6:
            turma['Situação'] = 'Ruim'
        if turma['Média da turma']> 7:
            turma['Situação'] = 'Boa'
        if 7 > turma['Média da turma'] >= 6:
            turma['Situação'] = 'Razoavél'
    return turma


resp = notas(5.5, 3, sit=True)
help(notas)
print(resp)
