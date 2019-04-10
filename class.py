chaine = str() # Crée une chaîne vide
# On aurait obtenu le même résultat en tapant chaine = ""

while chaine.lower() != "c":
    print("Tapez 'C' pour quitter...")
    chaine = input()

print("Merci Batard !")