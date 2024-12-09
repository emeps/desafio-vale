# Ler quantidade de valores
# loop for sob a quantidade de valores
# contar numero de <
# contar numero de >
# retornar menor dos dois casos

num_tests = int(input())
results = []
for i in range(num_tests):
    value = input()
    lt_occurences = 0
    gt_occurences = 0
    for c in value:
        if c == "<":
            lt_occurences = lt_occurences + 1
        if c == ">":
            if lt_occurences > gt_occurences:
                gt_occurences = gt_occurences + 1

    results.append(gt_occurences)

for r in results:
    print(r)