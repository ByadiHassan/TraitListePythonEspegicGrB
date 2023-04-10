def saisirNotes(liste,nbr):
    for i in range(nbr):
        liste.append(float(input("Tapez la note numéro "+str(i+1)+" :")))
def afficherNotes(liste):
    #print(liste)
    for item in liste:
        #print(item ,end= " ")
        print(item)
    print()
def triCroissant(liste):
    for _ in range(len(liste)-1):
        for i in range(len(liste)-1):
            if liste[i]>liste[i+1]:
                liste[i],liste[i+1]=liste[i+1],liste[i]

def inverser(liste):
    for i in range(len(liste)//2):
        liste[i],liste[-1-i]=liste[-1-i],liste[i]
        #liste[i],liste[len(liste)-1-i]=liste[len(liste)-1-i],liste[i]

def inverserV1(liste):
    return liste[::-1]