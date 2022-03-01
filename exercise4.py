#Créer une fonction prenant trois nombres 
#et retournant la moyenne de leur carré + 1.

#Ensuite, modifier la fonction pour retourner 
#la moyenne de leur cube + 2.

#Finalement retournant la moyenne 
#de la fonction suivante: 
#xx + x + 3, pour les 3 nombres.

def moy(a, b, c):
 n = 3
def cube(n):
  return n**n+n+3

   return (cube(a)+cube(b)+cube(c))/3

  x= 5
  y= 4
  z= 3
  print(moy(x, y, z))