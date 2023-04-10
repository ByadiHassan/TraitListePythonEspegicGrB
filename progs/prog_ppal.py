#import fonctions as f
from sys import path
from os import system

system('cls')
#path.append("..\\modules\\pack")
path.append("D:\\Espegic\\Tsdi1\\groupe_b\\gestion_notes\\modules")
import pack.fonctions as f
'''
for p in path:
    print(path)
    system("pause")
'''

choix= 0
notes=[]

while choix !=11:
    system("cls")
    choix=int(input("1. Saisir\n2. Afficher\n3. Tri croissant\n4. Inverser le Tri\n" +
    "5. Admis\n6. Non Admis\n7. Rattrapage\n8. Note Max\n9. Note Min\n10. Nbr Admis\n" +
    "11. Quitter\n Tapez votre choix : "))
    if choix==1:
        nbrNote=int(input("Combien de notes voulez vous saisir ? "))
        f.saisirNotes(notes,nbrNote)
        #system("cls")

    elif choix==2:
        f.afficherNotes(notes)
        system("pause")
        #system("cls")
    elif choix==3:
        f.triCroissant(notes)
        f.afficherNotes(notes)
        system("pause")
        #system("cls")
        
    elif choix==4:
        #notes=f.inverserV1(notes)
        notes=notes[::-1]
        f.afficherNotes(notes)
        system("pause")
        #system("cls")
    elif choix==5:
        pass 
    elif choix==6:
        pass
    elif choix==7:
        pass
    elif choix==8:
        pass
    elif choix==9:
        pass
    elif choix==10:
        pass

