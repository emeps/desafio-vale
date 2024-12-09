from math import gcd

qnt_testes = int(input())

resultados = []
for t in range(qnt_testes):
    dados = input().split(" ")
    n1 = int(dados[0])
    d1 = int(dados[2])
    n2 = int(dados[4])
    d2 = int(dados[6])
    if dados[3] == '+':
        nr = n1*d2 + n2*d1
        dr = d1*d2
    elif dados[3] == '-':
        nr = n1*d2 - n2*d1
        dr = d1*d2
    elif dados[3] == '*':
        nr = n1*n2
        dr = d1*d2
    elif dados[3] == '/':
        nr = n1*d2
        dr = n2*d1

    divisor_comum = gcd(nr, dr)
    nr_simplificado = nr // divisor_comum
    dr_simplificado = dr // divisor_comum
    resultados.append(f"{nr}/{dr} = {nr_simplificado}/{dr_simplificado}")

for r in resultados:
    print(r)