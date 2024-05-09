nbp = int(input())

for i in range(nbp):
    nom_prenom = input()
    prenom_nom = nom_prenom.split(' ')
    print(prenom_nom[0]+' ' + prenom_nom[1])