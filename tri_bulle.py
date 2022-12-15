from random import randint
tab = []

for i in range(10):
    tab.append(randint(1, 200))

"""# tableau parfait
for i in range(10):
    tab.append(i)
    
# tableau inversé
for i in range(10):
    tab.append(10 - i)"""


def tri_a_bulle(tableau):

    comparaisons = 0
    affectations = 0

    print(tableau)

    for i in range((len(tableau)), 1, -1):

        for j in range(0, (i - 1)):

            comparaisons += 1
            if tableau[j] > tableau[j + 1]:

                echange = tableau[j]
                tableau[j] = tableau[j + 1]
                tableau[j + 1] = echange
                affectations += 3

        print(tableau)
    print(comparaisons)
    print(affectations)


tri_a_bulle(tab)

# print(tab)
