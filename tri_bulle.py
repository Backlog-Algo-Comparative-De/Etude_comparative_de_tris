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
    l.append(comparaisons + affectations)
    return l
