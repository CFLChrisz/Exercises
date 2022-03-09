n1 = int(input("entrer un nombre pair"))
    
n2 = int(input("entrer un nombre impair"))
    
if n1%2== 0:
        if n2%2== 0:
            print("erreur: le deuxieme nombre est pair")
            #ici n1 est pair et n2 est pair
        else:
            print(n1,n2)
            #ici n1 est pair et n2 est impair
            
else:
        if n2%2== 0:
            print("Erreur: Le premier nombre est impair")
            #ici n1 est impair et n2 est pair
        else:
            print("Erreur: Les deux nombres sont impaires")
            #ici n1 est impair et n2 est impair