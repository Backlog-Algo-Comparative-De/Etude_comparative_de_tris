tab = [111, 34, 22, 55, 4, 2, 1, 77]

def tri_selection(tab):

    for i in range(0,len(tab)-1):
        min = i
        for j in range(i+1,len(tab)):
            if tab[j]<tab[min]:
                min = j
        if (min != i):
            tmp = tab[i]
            tab[i] = tab[min]
            tab[min] = tmp
    print(tab)


tri_selection(tab)