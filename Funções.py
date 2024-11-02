def media(n1,n2,n3,n4):
    media=(n1+n2+n3+n4)/4
    if(media>7):
        return "APROVADO"
    elif(media<7 and media>4):
        return "RECUPERAÇÃO"
    else:
        return "REPROVADO"

def DefineMedia(nome):
    notas=[]
    for i in range(4):
        notas.append(float(input(f'Digite a {i+1} nota: ')))
    print(f'O aluno {nome} está: {media(notas[0], notas[1], notas[2], notas[3])}')

for i in range(5):
        nomeAluno=input('Digite o nome do aluno: ')
        DefineMedia(nomeAluno)