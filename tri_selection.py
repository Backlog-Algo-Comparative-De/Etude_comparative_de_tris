tab = [111, 34, 22, 55, 4, 2, 1, 77, 90, 17]

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