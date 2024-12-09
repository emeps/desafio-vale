qtd_testes = int(input())
resultados = []
for teste in range(qtd_testes):
    texto = input()
    texto_criptografado = []
    for c in texto:
        valor_ascii_c = ord(c)
        if (valor_ascii_c >= 65 and valor_ascii_c <= 90) or \
           (valor_ascii_c >= 97 and valor_ascii_c <= 122):
            valor_ascii_c = valor_ascii_c + 3
            texto_criptografado.append(chr(valor_ascii_c))
        else:
            texto_criptografado.append(c)

    texto_criptografado.reverse()
    len_texto = len(texto_criptografado)
    for i in range(len_texto//2, len_texto):
        c = texto_criptografado[i]
        valor_ascii_c = ord(c)
        texto_criptografado[i] = chr(valor_ascii_c-1)
    resultados.append("".join(texto_criptografado))

for r in resultados:
    print(r)