meu_dicionario = {'nome': 'João', 'idade': 30}


dicionario={'Pagiantion': 1, 'result':[
    {'title':'Flash'},{'title':'Huck'}
]}

result = dicionario.get('result','Nao tem valores')

print([x for x in result])
for res in result:
    r = res.get('title')
    print(r)