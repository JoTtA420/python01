p1=["",0]
p2=["",0]
p3=["",0]
p1[0]=input('Digite o nome: ')
p1[1]=int(input('Digite a idade: '))
p2=p1
p3=p1
for i in range(4):
    p1=input('Digite o nome: ')
    p1=int(input('Digite a idade: '))
    if(p3[1]>p1[1] or p3[1]>p2[1]):
        if(p1[1]<p2[1]):
            p3[0]=p1[0]
            p3[1]=p1[1]
    else:
            p3[0]=p2[0]
            p3[1]=p2[1]
print(p3)