from random import randint
from tri_bulle import tri_a_bulle
from tri_insertion import tri_insertion
from tri_selection import tri_selection
from tri_bulle_opti import tri_bulle_opti


def stat(min, max, step, nbr):

    moyenne = 0

    tri = int(input("Quel tri ? "))

    for i in range(min, max + 1, step):

        for j in range(nbr):

            tableau = []

            for k in range(i):

                tableau.append(randint(1, 10))

            if tri == 1:
                moyenne = moyenne + tri_selection(tableau)[1]
            if tri == 2:
                moyenne = moyenne + tri_insertion(tableau)[1]
            if tri == 3:
                moyenne = moyenne + tri_a_bulle(tableau)[1]
            if tri == 4:
                moyenne = moyenne + tri_bulle_opti(tableau)[1]

        moyenne = moyenne / i

        print(f"Taille du tableau : {i}, nombre moyen d'opérations : {moyenne}")


stat(10, 20, 5, 10)

# générations aléatoires de tableaux et appelez la fonction de tri

def tri_a_bulle(tableau):

    comparaisons = 0
    affectations = 0
    l = []


    for i in range((len(tableau)), 1, -1):

        for j in range(0, (i - 1)):

            comparaisons += 1
            if tableau[j] > tableau[j + 1]:

                echange = tableau[j]
                tableau[j] = tableau[j + 1]
                tableau[j + 1] = echange
                affectations += 3

    l.append(tableau)
    l.append(comparaisons)
    l.append(affectations)
    
    return l
