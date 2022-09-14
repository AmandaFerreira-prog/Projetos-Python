times=('Flamengo','Santos','Palmeiras','Gremio','Atletico Paranaense','São Paulo','Internacional','Corinthians','Fortaleza,'
       'Goias ','Bahia', 'Vasco da Gama ','Atletico','Fluminense','Botafogo','Ceara','Cruzeiro','Csa','Chapecoense','Avaí')
primeiros=times[:5]
ultimos=times[15:]
ordem=sorted(times)
poschapeco=times.index('Chapecoense')
print('-=-'*15)
print(f'Lista de times do Brasileirão: {times}')
print('-=-'*15)
print(f'Os 5 primeiros são: {primeiros}')
print('-=-'*15)
print(f'Os 4 ultimos são: {ultimos}')
print('-=-'*15)
print(f'Times em ordem alfabetica: {ordem}')
print('-=-'*15)
print(f'O time da Chapecoense esta na posição {poschapeco+1}°.')