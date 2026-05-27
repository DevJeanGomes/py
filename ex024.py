cidade = input("\nDigite o nome de uma cidade: ").strip()

resultado = cidade.upper().startswith("SANTO")

if resultado:
    print("\nA cidade COMEÇA com o nome 'SANTO'.\n")
else:
    print("\nA cidade NÃO começa com o nome 'SANTO'.\n")