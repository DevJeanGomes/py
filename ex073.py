from rich import print

times_brasileirao = (
    "Flamengo",       # 0º[cite: 1]
    "Palmeiras",      # 1º[cite: 1]
    "Athletico-PR",   # 2º[cite: 1]
    "Bahia",          # 3º[cite: 1]
    "Fluminense",     # 4º[cite: 1]
    "Cruzeiro",       # 5º[cite: 1]
    "Atlético-MG",    # 6º[cite: 1]
    "Coritiba",       # 7º[cite: 1]
    "Bragantino",     # 8º[cite: 1]
    "Santos",         # 9º[cite: 1]
    "Botafogo",       # 10º[cite: 1]
    "São Paulo",      # 11º[cite: 1]
    "EC Vitória",     # 12º[cite: 1]
    "Corinthians",    # 13º[cite: 1]
    "Mirassol",       # 14º[cite: 1]
    "Grêmio",         # 15º[cite: 1]
    "Vasco da Gama",  # 16º[cite: 2]
    "Internacional",  # 17º[cite: 2]
    "Remo",           # 18º[cite: 2]
    "Chapecoense"     # 19º[cite: 2]
)

#A) Apenas os 5 primeiros colocados
print(times_brasileirao[0:5])
#B) Os últimos 4 colocados da tabela.
print(times_brasileirao[15:19])
#C) Uma lista com os times em ordem alfabética.
print(sorted(times_brasileirao))
#D) Em que posição na tabela está o time da Chapecoense
indice = times_brasileirao.index("Chapecoense")
posicao_tabela = indice + 1
print(f"A Chapecoense está na {posicao_tabela}ª posição.")

