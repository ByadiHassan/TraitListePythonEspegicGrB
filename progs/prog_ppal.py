#import fonctions as f
from sys import path
from os import system

system('cls')
path.append(".\\modules")
#path.append("D:\\Espegic\\Tsdi1\\groupe_b\\gestion_notes\\modules")
import pack.fonctions as f
'''
for p in path:
    print(path)
    system("pause")
'''

choix= 0
notes=[]

while choix !=15:
    system("cls")
    choix=int(input("1. Saisir\n2. Afficher\n3. Tri croissant\n4. Inverser le Tri\n" +
    "5. Admis\n6. Non Admis\n7. Rattrapage\n8. Note Max\n9. Note Min\n10. Nbr Admis\n" +
    "11. Enregistrer\n12. Charger\n13. Ajouter\n14. Nbr de fois\n15. Quitter\n Tapez votre choix : "))
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
        f.afficherNotes(f.getAdmis(notes))
        system("pause")
    elif choix==6:
        f.afficherNotes(f.getNonAdmis(notes))
        system("pause")
    elif choix==7:
        pass
    elif choix==8:
        print("La plus grande note est :",f.getMax(notes))
        system("pause")
    elif choix==9:
        print("La plus petite note est :",f.getMin(notes))
        system("pause")
    elif choix==10:
        pass
    elif choix==11:
        f.enregistrer(notes)
    elif choix==12:
        notes=f.charger()
    elif choix==13:
        notes.append(float(input("Tapez la note à ajouter ?")))
    elif choix==14:
        print("cette note existe ",notes.count(float(input("Tapez une note à chercher ? "))),"fois")
        system("pause")