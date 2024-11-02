def ordenar_alfabeticamente():
    pessoas=[]
    for i in range(10):
        nome=input(f"Digite o nome da {i+1} pessoa: ")
        bairro=input(f"Digite o bairro da {i+1} pessoa: ") 
        pessoas.append({"nome": nome, "bairro": bairro})
        pessoas.sort(key=lambda pessoa: pessoa["nome"])
        
        print("\n--- Pessoas ordenadas alfabeticamente ---")   
        for pessoa in pessoas:
            print(f"Nome: {pessoa['nome']}, Bairro: {pessoa:['bairro']}")
            