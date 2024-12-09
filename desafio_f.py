num_matrizes = int(input())


def output(n, m, matriz):
    matriz_string = [
        [str(matriz[l][c]) for c in range(m)]
        for l in range(m)
    ]

    # Máximo do comprimento de cada coluna
    largura_coluna = [
        max(
            [len(matriz_string[l][c]) for l in range(m)]
        )
        for c in range(m)
    ]

    matriz_string = [
        [matriz_string[l][c].rjust(largura_coluna[c]) for c in range(m)]
        for l in range(m)
    ]

    return (
        f"Quadrado da matriz #{n}:\n" +
        "\n".join([" ".join(matriz_string[l]) for l in range(m)])
    )


resultados = []
for n in range(num_matrizes):
    matriz = []
    num_linhas = int(input())

    for ln in range(num_linhas):
        linha = input().split(" ")
        matriz.append([int(n)**2 for n in linha])

    resultado = output(n+4, num_linhas, matriz)
    resultados.append(resultado)

print("\n\n".join(resultados))