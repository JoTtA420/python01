pessoa=[]
for i in range(5):
    nome=input('Digite seu nome: ')
    idade=int(input('Digite sua idade: '))
    pessoa.append({"nome": nome, "idade":idade})
def buscar():
    i=0
    menor=0
    while(i<5):
        if(pessoa[i]["idade"]<pessoa[menor]["idade"]):
            menor=i
        else:
            menor=menor
            i+=1
            return menor
        print(f'{pessoa[buscar()]}')