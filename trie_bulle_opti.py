def tri_bulle_opti(tab):
    estTrie = True

    while(estTrie):
        estTrie = False
        for i in range(len(tab) - 1):
            if tab[i] > tab[i+1]:
                tab[i], tab[i+1] = tab[i+1], tab[i]
                estTrie = True

    return tab
    
tab = [3,45,234,234,3234,32,2343,1]

print(tri_bulle_opti(tab))
