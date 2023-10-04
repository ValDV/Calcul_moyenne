# Initialisation des valeurs minimale et maximale en secondes
min_time = float("inf")
max_time = float("-inf")

total_seconds = 0  # Initialisation de la valeur totale en secondes

for i in range(10):  # Répéter 10 fois
    time_input = input("Veuillez entrer un temps (minutes:secondes) : ")  # Demander à l'utilisateur de rentrer le temps

    # Diviser le temps entré en minutes et secondes
    minutes, seconds = map(int, time_input.split(":"))

    # Convertir le temps en secondes
    time_in_seconds = minutes * 60 + seconds

    total_seconds += time_in_seconds  # Additionne la valeur totale et le temps en secondes

    # Mettre à jour les valeurs minimale et maximale
    if time_in_seconds < min_time:
        min_time = time_in_seconds
    if time_in_seconds > max_time:
        max_time = time_in_seconds

# Calcule la moyenne en secondes
average_seconds = total_seconds / 10

# Calcule l'étendue en secondes
range_seconds = max_time - min_time

print(f"La moyenne des temps est de {average_seconds} secondes")
print(f"Le temps minimum est {min_time} secondes")
print(f"Le temps maximum est {max_time} secondes")
print(f"L'étendue des temps est de {range_seconds} secondes")
