# cette définition permet d'utiliser des bases b ≤ 36
# rajouter des symboles si besoin
CHIFFRES = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NOMBRES = {c : n for (n, c) in enumerate(CHIFFRES)}

def chiffre(n):
    return CHIFFRES[n]

def nombre(ch):
    return NOMBRES[ch]
