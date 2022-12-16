def tri_a_bulle(tableau):
    """
    Fonction pour trier un tableau avec le tri à bulles
    :param tableau: le tableau qu'on va trier
    :return: le tableau trié et le nombre d'opérations effectuées
    """

    comparaisons = 0
    affectations = 0
    l = []

    for i in range((len(tableau)), 1, -1):

        for j in range(0, (i - 1)):

            # On vérifie si j est plus grand que j+1
            comparaisons += 1
            if tableau[j] > tableau[j + 1]:

                # Si j est plus grand que j+1, on inverse les valeurs
                echange = tableau[j]
                tableau[j] = tableau[j + 1]
                tableau[j + 1] = echange
                affectations += 3

    l.append(tableau)
    l.append(comparaisons + affectations)
    return l
