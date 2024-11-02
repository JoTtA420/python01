numeros=[]
for i in range(5):
    numero=int(input('Digite um número: '))
    numeros.append(numero)
    numeros.sort()
    print(f'Os números em ordem crescente são: {numeros}')