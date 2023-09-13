Total = 0 #Initialisation de la valeur Total

for i in range(31): #Répéter 31 fois
    
    temperature = float(input("Veuillez entrer une température : ")) #Demande à l'utilisateur de rentrer une valeur
    
    Total = Total + temperature #Additionne la valeur Total et la Température
    
Moyenne = Total/31 #Calcule la moyenne

print(f"La moyenne des températures est de {Moyenne}") #Affiche le résultat de la moyenne