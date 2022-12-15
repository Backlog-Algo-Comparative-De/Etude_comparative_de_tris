def tri_selection(tab):

    l = []
    
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

    l.append(tab)
    l.append(comparaisons + affectations)

    return l




