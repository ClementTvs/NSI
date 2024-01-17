from random import randint

def minimum(tab):
    mini=tab[0]
    for i in range(1,len(tab)):
        if (tab[i]< mini):
            mini=tab[i]
    return mini

t=[1,18,32,-3]
print(minimum(t))

def maximum(tab):
    maxi=tab[0]
    for i in range(1,len(tab)):
        if (tab[i]> maxi):
            maxi=tab[i]
    return maxi

t=[1,18,32,-3]
print(maximum(t))  

def genere_tab_alea(n,maxi):
    tab=[randint(0,maxi) for i in range (n)]
    return tab

def tri_par_selection(tab):
    for i in range(len(tab)):
        imin=i
        for j in range(i+1, len(tab)):
            if (tab[j] < tab[imin]):
                imin=j
        tmp = tab[i]
        tab[i]=tab[imin]
        tab[imin]=tmp

t=genere_tab_alea(10,100)
print(t)
tri_par_selection(t)
print(t)

tab=[3,2,4,1]

for i in range(1,len(tab)):
    tmp=tab[i]
    j=i
    while (j > 0) and (tab[j-1] > tmp):
        tab[j]=tab[j-1]
        j=j-1
    tab[j]=tmp
    print(tab)


def genere_tab_alea(n,maxi):
    tab=[randint(0,maxi) for i in range (n)]
    return tab

def tri_par_insertion(tab):
    for i in range(1,len(tab)):
        tmp=tab[i]
        j=i
        while (j > 0) and (tab[j-1] > tmp):
            tab[j]=tab[j-1]
            j=j-1
        tab[j]=tmp

t=genere_tab_alea(10,100)
print(t)
tri_par_insertion(t)
print(t)

tab=[3,2,4,1]

for i in range(1 ,len(tab)):
    tmp=tab[i]
    j=i
    while (j > 0) and (tab[j-1] > tmp):
        tab[j]=tab[j-1]
        j=j-1
    tab[j]=tmp
    print(i)
    print(tab)

def genere_tab_alea(n,maxi):
    tab=[randint(-1000,maxi) for i in range (n)]
    return tab

def tri_par_insertion(tab):
    for i in range(1,len(tab)):
        tmp=tab[i]
        j=i
        while (j > 0) and (tab[j-1] > tmp):
            tab[j]=tab[j-1]
            j=j-1
        tab[j]=tmp

t=genere_tab_alea(50,100)
print(t)
tri_par_insertion(t)
print(t)
