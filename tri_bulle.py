from random import randint
tab = []

for i in range(10):
    tab.append(randint(1, 20))


def tri_a_bulle(tableau):

    print(tableau)

    for i in range((len(tableau)), 1, -1):

        for j in range(0, (i - 1)):

            if tableau[j] > tableau[j + 1]:

                echange = tableau[j]
                tableau[j] = tableau[j + 1]
                tableau[j + 1] = echange

        print(tableau)


tri_a_bulle(tab)

# print(tab)
