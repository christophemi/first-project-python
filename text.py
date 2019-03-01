ageUser = input("Quel age as-tu ?")


try:
    ageUser = int(ageUser)
except:
    print("l'age est correct !!")
else:
    print("Tu as", ageUser, "ans")
finally:
    print("Fin du programe !")
