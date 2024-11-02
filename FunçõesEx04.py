def saudacao(nome, cidade):
    if cidade == "Rio de Janeiro":
        return f"Seja Bem-vindo {nome} à Cidade Maravilhosa!"
    else:
        return f"Olá {nome}, de {cidade}! "
    
nome=input("Digite seu nome: ")
cidade=input("Digite sua cidade: ")
saudacao_personalizada = saudacao(nome, cidade)
print(saudacao_personalizada)