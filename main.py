from random import randint
from tri_bulle import tri_a_bulle

def stat(min, max, step, nbr):

    moyenne = 0

    for i in range(min, max + 1, step):

        for j in range(nbr):

            tableau = []

            for k in range (i):

                tableau.append(randint(1, 10))

            moyenne = moyenne + tri_a_bulle(tableau)

        moyenne /= i

        print(f"Taille du tableau : {i}, nombre moyen d'opérations : {moyenne}")


stat(10, 20, 5, 10)
