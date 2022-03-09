
jour_fete = int(input("entrex votre jour de fète en chiffre! ")) 
mois_fete = int(input("entrer vore mois en chiffre! "))

if jour_fete==7 and mois_fete==3:
    print("bonne fête!! ")
else:
    print("mission failed, we`ll get `em next time!")
if 1<= mois_fete <=2:

     print("ta tu fret? t`es née en hiver ")

if 4<=mois_fete <=5:
    print("hey! tu es née au printemps ")

if 7<=mois_fete <=8:

    print("tu es née en été! ")

if 10<=mois_fete <=11:

    print("tu es née en automne! ")

if mois_fete == 3:
    if jour_fete <= 20:
        
        print("tu est en hiver")
    else:
        print("hey! tu es née au printemps ")

if mois_fete == 6:
    if jour_fete <= 20:
        
        print("tu est en printemps")
    else:
        print("hey! tu es née au été ")

if mois_fete == 9:
    if jour_fete <=20:
        print("hey! tu es née au été ")
    else:
        print("tu es née en automne! ")

if mois_fete == 12:
    if jour_fete <=20:
        print("hey! tu es née automne!  ")
    else:
        print("tu es née en hiver! ")

