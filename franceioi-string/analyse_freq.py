nb_ligne_mot = input()
nb_ligne, nb_mot = nb_ligne_mot.split(' ')

list_mo_char = {}
old = 0
for i in range(int(nb_ligne)):
    phrase = input()
    list_mot = phrase.split(' ')
    for j in range(len(list_mot)):
        if len(list_mot[j]) not in list_mo_char:
            list_mo_char[len(list_mot[j])] = 1
        else:
            list_mo_char[len(list_mot[j])] = list_mo_char[len(list_mot[j])] + 1

keysList = sorted(list(list_mo_char.keys()))
for i in range(len(keysList)):
    print(str(keysList[i]) + ' : ' + str(list_mo_char[keysList[i]]))