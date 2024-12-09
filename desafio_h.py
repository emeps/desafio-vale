resultados = []
while True:
    try:
        num_reclamacoes = int(input())
        output = "vai ter copa!" if num_reclamacoes == 0 else "vai ter duas!"
        resultados.append(output)
    except:
        break

for r in resultados:
    print(r)