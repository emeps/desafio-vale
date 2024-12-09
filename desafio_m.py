resultados = []
while True:
    try:
        enunciado = input()
        palavras = enunciado.split()
        comprimentos = []
        for palavra in palavras:
            len_palavra = 0
            for c in palavra:
                if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
                    len_palavra = len_palavra + 1
                elif (c >= '0' and c <= '9') or c == '.':
                    comprimentos.append(len_palavra)
                    len_palavra = 0
            if len_palavra > 0:
                comprimentos.append(len_palavra)

        comprimento_medio = sum(comprimentos)//len(comprimentos)
        if comprimento_medio <= 3:
            resultados.append(250)

        elif comprimento_medio >= 4 and comprimento_medio <= 5:
            resultados.append(500)

        elif comprimento_medio >= 6:
            resultados.append(1000)
    except:
        break

for r in resultados:
    print(r)
