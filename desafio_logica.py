lista_de_herois = [
    {"nome": "Aragorn", "xp": 8500},
    {"nome": "Gandalf", "xp": 12000},
    {"nome": "Legolas", "xp": 6200},
    {"nome": "Frodo", "xp": 1500},
    {"nome": "Sam", "xp": 3000},
    {"nome": "Gimli", "xp": 7500},
    {"nome": "Merry", "xp": 9500},
    {"nome": "Pippin", "xp": 1000},
    {"nome": "Elrond", "xp": 15000}
]

for heroi in lista_de_herois:
    nome_heroi = heroi["nome"]
    xp_heroi = heroi["xp"]
    nivel_heroi = ""

    if xp_heroi <= 1000:
        nivel_heroi = "Ferro"
    elif 1001 <= xp_heroi <= 2000:
        nivel_heroi = "Bronze"
    elif 2001 <= xp_heroi <= 5000:
        nivel_heroi = "Prata"
    elif 5001 <= xp_heroi <= 7000:
        nivel_heroi = "Ouro"
    elif 7001 <= xp_heroi <= 8000:
        nivel_heroi = "Platina"
    elif 8001 <= xp_heroi <= 9000:
        nivel_heroi = "Ascendente"
    elif 9001 <= xp_heroi <= 10000:
        nivel_heroi = "Imortal"
    else:
        nivel_heroi = "Radiante"

    print(f"O Herói de nome {nome_heroi} está no nível de {nivel_heroi}")
