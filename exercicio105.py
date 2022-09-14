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
