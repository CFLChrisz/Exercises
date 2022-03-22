#Créer une liste contenant tous les nombres premiers entre 2 et 20. Ensuite, 
#demander à l'utilisateur d'écrire un nombre entre 2 et 20 (bien vérifier si c'est le cas)
#et vérifier si ce nombre est premier à l'aide de votre liste en affichant le résultat à la console.

def liste():
    chiffre = [2, 3, 5, 7, 11, 13, 17, 19]
    input("tapper un nombre entre 2 et 20. :")
    if chiffre in chiffre:
        print("ce chiffre est un nombre premier!")
    else:
        print("ce chiffre n`est pas un nombre premier.")
    return None
liste()