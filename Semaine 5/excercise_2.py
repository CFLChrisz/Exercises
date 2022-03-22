#Créer une liste de 5 éléments : [1, 2, 5, 3, 4]. 
#Ensuite, créer deux copies de cette liste, une copie en surface et une copie profonde intitulée respectivement surface et profonde. 
#Finalement, demander à l'utilisateur d'entrer un mot, 
#modifier le 2e élément de la liste «surface» et le 3e élément de la liste «profonde» et imprimer les trois listes à la console.

def element():
    liste = ["sharklado", "myntz", "runtz", "backpackboyz", "cookies"]
    surface = liste[:]
    profonde = liste[:]
    mot = input("écrivez un mot de votre choix? ")
    surface[2] = mot
    profonde[3] = mot
    print(liste, surface, profonde)
    return None
element()

