lista=[]
soma=0
for i in range(10):
    lista.append(int(input('Digite um número: ')))
    soma+=lista[i]
print(f'Soma: {soma}, Média: {soma/len(lista)}')