# Initialisation des valeurs minimale et maximale
min_temperature = float("inf")
max_temperature = float("-inf")

Total = 0  # Initialisation de la valeur de Total

for i in range(31):  # Répéter 31 fois
    temperature = float(input("Veuillez entrer une température : "))  # Demander à l'utilisateur de rentrer la valeur de la température
    Total = Total + temperature  # Additionne la valeur Total et la température

    # Mettre à jour les valeurs minimale et maximale
    if temperature < min_temperature:
        min_temperature = temperature
    if temperature > max_temperature:
        max_temperature = temperature

# Calcule la moyenne
moyenne = Total / 31

# Calcule l'étendue
etendue = max_temperature - min_temperature

print(f"La moyenne des températures est de {moyenne}")
print(f"La température minimale est {min_temperature}")
print(f"La température maximale est {max_temperature}")
print(f"L'étendue des températures est de {etendue}")