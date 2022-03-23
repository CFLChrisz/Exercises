#Créer un dictionnaire possédant les cours que vous suivez cette session et leur enseignant respectif. Par exemple:
#Keven Presseau-St-Laurent - Concepts de programmation 1
#Ensuite, afficher un menu à la console présentant les 3 cours et offrant à
#l'utilisateur d'en sélectionner 1. Lorsque l'utilisateur à fait sa sélection,
#afficher le nom de l'enseignant et le nom du cours à l'écran.

def diction():
    cours_hiver_2022 = {   
        "Keven PresseauSt-Laurent":"Concepts de programmation 1",
        "Emma Parent Senez":"Logique mathématique pour les professionnels de l'informatiqe",
        "Jean-Pierre Fiset":"SYSTÈMES D'EXPLOITATION"
        }
    print(cours_hiver_2022.get(kevin))
    return None
diction()