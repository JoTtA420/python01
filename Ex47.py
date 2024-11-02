pessoas=[]
for i in range(10):
        nome=input(f"Digite o nome {i+1} pessoas: ")
        telefone=input(f"Digite o telefone da {i+1} pessoa:")
        cidade=input(f"Digite a cidade da {i+1} pessoa: ")
        pessoas.append({"nome": nome, "telefone": telefone, "cidade": cidade})

print("\n--- Pessoas que moram em Campo Grande ---")
for pessoa in pessoas:
        if pessoa["cidade"]=="Campo Grande":
            print(f"Nome: {pessoa['nome']}, Telefone: {pessoa['telefone']}")
            