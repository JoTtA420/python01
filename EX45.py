alunos=[]
medias=[]
def preencheLista():
    for i in range(10):
        alunos.append(input(f'Digite o nome do {i+1} aluno: '))
        medias.append(float(input(f'Digite a média do {i+1} aluno: ')))
        return
def retornaMaiores():
    for i in range(10):
        if(medias[i]>=6):
            print(f'aluno{alunos[i]} com média {medias[i]}')
            return
preencheLista()
retornaMaiores()