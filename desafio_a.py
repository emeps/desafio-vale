# Ler quantidade de valores
# loop for sob a quantidade de valores
# Testa o valor e separa os pares e impares em duas listas
# ordena crescente os pares
# ordena decrescente os impares
# print dos pares
# print dos impares

even_values = []
odd_values = []
num_values = int(input())

for i in range(num_values):
    value = int(input())
    if value % 2 == 0:
        even_values.append(value)
    else:
        odd_values.append(value)

even_values.sort()
odd_values.sort(reverse=True)

for v in even_values:
    print(v)
for v in odd_values:
    print(v)
