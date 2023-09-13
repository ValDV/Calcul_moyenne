Total = 0
for i in range(31):
    temperature = float(input("Veuillez entrer une température : "))
    Total = Total + temperature
Moyenne = Total/31
print(f"La moyenne des températures est de {Moyenne}")