mapa_leds = {
    "1": 2,
    "2": 5,
    "3": 5,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 3,
    "8": 7,
    "9": 6,
    "0": 6,
}

num_testes = int(input())

resultados = []
for n in range(num_testes):
    valor = input()
    qtd_leds = 0
    for c in valor:
        qtd_leds = qtd_leds + mapa_leds[c]
    resultados.append(f"{qtd_leds} leds")

for r in resultados:
    print(r)
