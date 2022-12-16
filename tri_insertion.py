def tri_insertion (tableau):

    """
    Fonction pour trier un tableau avec le tri insertion
    :param tableau: le tableau qu'on va trier
    :return: le tableau trié et le nombre d'opérations effectuées
    """
    comparaison = 0
    affectation = 0
    l = []

    for i in range(1,len(tableau)):

        lacase = tableau[i]
        affectation+=1
        j = i
        affectation+=1

        comparaison+=2
        while j>0 and tableau[j-1]>lacase:
            

            tableau[j]=tableau[j-1]
            affectation += 1

            j=j-1
            affectation +=1

        tableau[j]= lacase
        affectation+=1

    l.append(tableau)
    l.append(comparaison + affectation)
    return l