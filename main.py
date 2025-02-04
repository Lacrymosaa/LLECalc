def calculate_synch_chance(Synch_Base_Chance, current_encounters):
    # Valores fixos
    Porcentagem_Final = 100  # Chance máxima de 100%
    encounters_final = 200000  # 200k encounters para atingir 100%

    # Calcular o aumento percentual progressivo
    proportion_encounters = current_encounters / encounters_final

    # Calcular a chance aumentada pelos encounters
    chance_aumentada = (Porcentagem_Final - Synch_Base_Chance) * proportion_encounters

    # Calcular a chance total
    chance_total = Synch_Base_Chance + chance_aumentada

    return chance_total, chance_aumentada

# Exemplo de uso:
Synch_Base_Chance = 30  # Pode ser ajustada para 26 ou 30%
current_encounters = 75654  # Quantidade atual de encounters

# Chamar a função
chance_total, chance_aumentada = calculate_synch_chance(Synch_Base_Chance, current_encounters)

print(f"Chance total: {chance_total:.2f}%")
print(f"Chance aumentada pelos encounters: {chance_aumentada:.2f}%")