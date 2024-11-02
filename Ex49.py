def validar_media(media):
    return 0<media<10
def main():
    medias_validas=[]
    for i in range(5):
        nome=input(f"Digite o nome do aluno {i+1}: ")
        while True:
            try:
                media=float(input(f"Digite a média do aluno {nome}: "))
                medias_validas(media):
                break
    else:
                    print("Média inválida. A média deve estar entre 0 e 10. ")
                            except ValueError:
                                    print("Entrada inválida. Digite um número válido. ")

print("\nMédias válidas: ")
for media in medias_validas:
    print(f"Média: {media:.2f}")
    
