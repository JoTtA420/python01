numeros=[]
cont=0
for i in range(10):
    numeros.append(int(input('Digite um número: ')))
    if(numeros[i]>10):
        cont+=1
print(cont)