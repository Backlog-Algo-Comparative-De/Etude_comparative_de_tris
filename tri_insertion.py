import random

tableau = []

for i in range(10):
    tableau.append(random.randint(0,200))

def tri_insertion (tableau):
    comparaison = 0
    affectation = 0
    l = []

    for i in range(1,len(tableau)):

        lacase = tableau[i]
        affectation+=1
        j = i
        affectation+=1

        while j>0 and tableau[j-1]>lacase:
            comparaison+=2

            tableau[j]=tableau[j-1]
            affectation += 1

            j=j-1
            affectation +=1

        tableau[j]= lacase
        affectation+=1

    l.append(tableau)
    l.append(comparaison)
    l.append(affectation)
    return l

print(tri_insertion(tableau))