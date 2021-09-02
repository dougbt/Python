def ler():
    print("Responda apenas 'S' ou 'N'")
    telefonou = input('Telefonou para a vítima? ')
    esteve = input('Esteve no local do crime? ')
    mora = input('Mora perto da vítima? ')
    devia = input('Devia para a vítima? ')
    trabalhou = input('Trabalhou com a vítima? ')
    return telefonou, esteve, mora, devia, trabalhou

def resposta(telefonou):
    if telefonou==esteve==mora==devia=trabalhou:
        print('Você é o Assassino')
        
