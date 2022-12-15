from random import *

tab = []

for i in range(10):
    tab.append(randint(0,200))


def tri_bulle_opti(tab):
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
    liste1.append(compteurComparaison)
    liste1.append(compteurAffectation)

    return liste1
    

print(tri_bulle_opti(tab))
