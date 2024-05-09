nblivre, nbjour = input().split(' ')
id_livre_emp = {}

def emprunte(nbClient, id_livre_emp, curr_jour):
    for i in range(nbClient):
        i_livre , nb_j_emp = input().split(' ')
        i_livre = int(i_livre)
        nb_j_emp = int(nb_j_emp)
        libre = livre_libre(i_livre, id_livre_emp, curr_jour)
        if len(id_livre_emp) == 0:
            id_livre_emp[i_livre] = nb_j_emp + curr_jour
            print(1)
        elif libre == False:
            id_livre_emp[i_livre] = nb_j_emp + curr_jour
            print(1)
        else:
            print(0)

def livre_libre(i_livre, id_livre_emp, curr_jour):
    result = False
    if i_livre in id_livre_emp:
        if curr_jour < id_livre_emp[i_livre]:
            result = True
        else:
            result = False
    return result


for i in range(int(nbjour)):
    nbClient = int(input())
    emprunte(nbClient, id_livre_emp, i)
