ginasio = [int(e) for e in input().split(" ")]
ip_ginasio = ginasio[0]
num_tentativas = ginasio[1]

anlogimons_ginasio = []
for tentativas in range(num_tentativas):
    anlogimon = [int(e) for e in input().split(" ")]

    anlogimon_pc = anlogimon[0]
    anlogimon_na = anlogimon[1]

    qnt_anlogimon = len([a for a in anlogimons_ginasio
        if
            a[0] >= anlogimon_pc - ip_ginasio and
            a[0] <= anlogimon_pc + ip_ginasio
    ])
    if qnt_anlogimon <= anlogimon_na:
        anlogimons_ginasio.append(anlogimon)

print(len(anlogimons_ginasio))
