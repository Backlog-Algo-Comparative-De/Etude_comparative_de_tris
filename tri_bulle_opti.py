def tri_bulle_opti(tab):

    """
    Fonction pour trier un tableau avec le tri à bulle opti
    :param tab: le tableau qu'on va trier
    :return: le tableau trié et le nombre d'opérations effectuées
    """

    # Initialisation des compteurs et de la liste qui va etre return a la fin
    compteurAffectation = 0
    compteurComparaison = 0
    liste1 = []


    estTrie = False
    compteurAffectation +=1

    compteurComparaison +=1
    while(not estTrie):
        

        estTrie = True
        compteurAffectation +=1 

        for i in range(len(tab) - 1):

            compteurComparaison += 1
            if tab[i] > tab[i+1]:
                
                tab[i], tab[i+1] = tab[i+1], tab[i]
                compteurAffectation += 3

                estTrie = False
                compteurAffectation += 1
    
    liste1.append(tab)
    liste1.append(compteurComparaison + compteurAffectation)

    return liste1
    
