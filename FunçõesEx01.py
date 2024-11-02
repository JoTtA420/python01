def programasInfantis():
    lista1=['Peppa pig, Naruto, Avatar, Pantera cor de Rosa. ' ]   
    print(lista1)
    return
def carros():
    carro=[
        {
        'modelo':'Jeep Renegade',
        'preço':120000
    },
    {   'modelo':'Amarok',
        'preço':350000
    },
    {
        'modelo':'Hb20',
        'preço':'100000'
    },
    {
        'modelo':'Mobi',
        'preço': 70000
    }
    ]
    for c in carro:
        print(f'{c["modelo"]} Preço: R${c["preço"]}')
    return
idade=int(input('Digite sua idade: '))
if (idade>=18):
    carros()
else:
    programasInfantis()

    