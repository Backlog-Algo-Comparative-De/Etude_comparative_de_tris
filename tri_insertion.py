tableau = [15,20,12,3,11,5,2,8,14]
pireDesCas = [10,9,8,7,6,5,4,3,2,1]
meilleurDesCas=[1,2,3,4,5,6,7,8,9,10],
a = (len(tableau))
print(a)
def tri_insertion (tableau):
    for i in range(1,len(tableau)):

        lacase = tableau[i]
        j = i
        while j>0 and tableau[j-1]>lacase:
            tableau[j]=tableau[j-1]
            j=j-1
        tableau[j]= lacase
        print(tableau,i)


tri_insertion(tableau)