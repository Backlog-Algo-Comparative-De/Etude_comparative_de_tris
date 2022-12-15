#[1, 38, 111, 4, 17, 47, 86, 55, 77, 90,]

tab = []


# décommenter ceci pour faire un tableau parfait

""" for i in range (10):
    tab.append(i) """
    
# décommenter ceci pour faire un tableau qui pu la merde
    
for i in range (10):
    tab.append(10 - i)

def tri_selection(tab):
    
    affectations = 0
    comparaisons = 0

    for i in range(0,len(tab)-1):
        min = i
        affectations += 1
        for j in range(i+1,len(tab)):
            comparaisons += 1
            if tab[j]<tab[min]:
                min = j
                affectations += 1
        comparaisons += 1       
        if (min != i):
            tmp = tab[i]
            tab[i] = tab[min]
            tab[min] = tmp
            affectations += 3
    print(tab)
    print(comparaisons, affectations)


tri_selection(tab)