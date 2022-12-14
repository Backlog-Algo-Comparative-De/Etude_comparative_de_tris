tableau = [15,20,12,3,11,5,2]
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
        print(tableau)


tri_insertion(tableau)