qnt_testes = int(input())

resultados = []

def output(tabela_hash):
    i = 0
    out = []
    for ln in tabela_hash:
        out.append(f'{i} -> {" -> ".join(ln)}{" -> " if len(ln) > 0 else ""}\\')
        i = i + 1
    return "\n".join(out)

for t in range(qnt_testes):
    parametros = [int(p) for p in input().split(" ")]
    elementos = [int(e) for e in input().split(" ")]

    tabela_hash = [[] for k in range(parametros[0])]
    for e in elementos:
        tabela_hash[e%parametros[0]].append(str(e))
    resultados.append(output(tabela_hash))


print("\n\n".join(resultados))