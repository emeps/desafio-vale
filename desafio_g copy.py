from collections import defaultdict

# Leitura dos valores iniciais
ginasio = list(map(int, input().split()))
ip_ginasio = ginasio[0]
num_tentativas = ginasio[1]

# Dicionário para armazenar a quantidade de anlogimons por faixa de poder de combate
faixa_anlogimons = defaultdict(int)

# Contador para o número total de anlogimons no ginásio
total_anlogimons = 0

for _ in range(num_tentativas):
    # Leitura do anlogimon
    anlogimon_pc, anlogimon_na = map(int, input().split())

    # Calcular a quantidade de anlogimons na faixa permitida
    qnt_anlogimon = sum(
        faixa_anlogimons[pc]
        for pc in range(anlogimon_pc - ip_ginasio, anlogimon_pc + ip_ginasio + 1)
    )

    # Se a quantidade estiver no limite, adicionamos o anlogimon
    if qnt_anlogimon <= anlogimon_na:
        faixa_anlogimons[anlogimon_pc] += 1
        total_anlogimons += 1

# Imprime o número final de anlogimons no ginásio
print(total_anlogimons)
