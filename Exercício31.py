numeros=[]
for i in range(8):
    numeros.append(int(input('Digite um número: ')))
    numeros.sort()
print(f'O maior é: {numeros[len(numeros)-1]} e o menor é: {numeros[0]}')