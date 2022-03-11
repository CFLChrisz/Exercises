#Créer une calculatrice d'IMC demandant à l'utilisateur sa grandeur(en mètres), son poids(en kg). 
#Retournez ensuite la catégorie dans laquelle se trouve la personne.

def calculatrice():

    kg = float(input("ecrivé votre poid en kilogramme!"))

    m = float(input("écrivé votre en mètre!"))

    imc=kg/m**2

    if imc < 18.5:
        print("votre indice est bas!")
    elif 18.5 <= imc < 25:
        print("votre indece est au niveau suggéré!")
    elif 25 <= imc <= 30:
        print("votre indice est haut!")
    else:
        print("votre indice est trops elevé!")
    return None

calculatrice()


