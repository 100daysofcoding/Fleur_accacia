import os
import shutil

def main():
    while True:
        print("1. Créer un dossier")
        print("2. Créer un fichier")
        print("3. Ouvrir un dossier")
        print("4. Ouvrir un fichier")
        print("5. Supprimer un dossier")
        print("6. Supprimer un fichier")

        choix = input("Entrez le numéro de l'opération que vous souhaitez effectuer : ")

        if choix == '1':
            nom_dossier = input("Entrez le nom du dossier à créer : ")
            try:
                os.mkdir(nom_dossier)
                print(f"Dossier {nom_dossier} créé avec succès.")
            except:
                print(f"Le dossier {nom_dossier} existe déjà.")
        
        elif choix == '2':
            print("A. Créer dans un dossier existant")
            print("B. Créer à l'extérieur d'un dossier")
            
            choix_creation = input("Entrez l'opération que vous souhaitez effectuer : ").strip().lower()

            if choix_creation == 'a':
                nom_dossier = input("Entrez le nom du dossier où créer le fichier : ")
                nom_fichier = input("Entrez le nom du fichier à créer : ")
                contenu_fichier = input("Entrez le contenu du fichier : ")
                chemin_complet = os.path.join(nom_dossier, nom_fichier)
            
            elif choix_creation == 'b':
                nom_fichier = input("Entrez le nom du fichier à créer : ")
                contenu_fichier = input("Entrez le contenu du fichier : ")
                chemin_complet = nom_fichier
            else:
                print("Choix invalide.")
                continue

            with open(chemin_complet, 'w') as fichier:
                fichier.write(contenu_fichier)
                print(f"Fichier {nom_fichier} créé avec succès.")
        
        elif choix == '3':
            nom_dossier = input("Entrez le nom du dossier à ouvrir : ")
            try:
                os.startfile(nom_dossier)
            except:
                print(f"Le dossier {nom_dossier} n'existe pas.")
        
        elif choix == '4':
            print("A. Ouvrir un fichier à l'intérieur d'un dossier")
            print("B. Ouvrir un fichier à l'extérieur d'un dossier")
            
            choix_ouverture = input("Entrez l'opération que vous souhaitez effectuer : ").strip().lower()

            if choix_ouverture == 'a':
                nom_dossier = input("Entrez le nom du dossier où se trouve le fichier : ")
                nom_fichier = input("Entrez le nom du fichier à ouvrir : ")
                chemin_complet = os.path.join(nom_dossier, nom_fichier)
            elif choix_ouverture == 'b':
                nom_fichier = input("Entrez le nom du fichier à ouvrir : ")
                chemin_complet = nom_fichier
            else:
                print("Choix invalide.")
                continue

            try:
                os.startfile(chemin_complet)
            except:
                print(f"Le fichier {nom_fichier} n'existe pas.")
        
        elif choix == '5':
            nom_dossier = input("Entrez le nom du dossier à supprimer : ")
            try:
                shutil.rmtree(nom_dossier)
                print(f"Dossier {nom_dossier} supprimé avec succès.")
            except FileNotFoundError:
                print(f"Le dossier {nom_dossier} n'existe pas.")
        
        elif choix == '6':
            print("A. Supprimer un fichier à l'intérieur d'un dossier")
            print("B. Supprimer un fichier à l'extérieur d'un dossier")
            
            choix_suppression = input("Entrez l'opération que vous souhaitez effectuer : ").strip().lower()

            if choix_suppression == 'a':
                nom_dossier = input("Entrez le nom du dossier où se trouve le fichier : ")
                nom_fichier = input("Entrez le nom du fichier à supprimer : ")
                chemin_complet = os.path.join(nom_dossier, nom_fichier)
            elif choix_suppression == 'b':
                nom_fichier = input("Entrez le nom du fichier à supprimer : ")
                chemin_complet = nom_fichier
            else:
                print("Choix invalide.")
                continue

            try:
                os.remove(chemin_complet)
                print(f"Fichier {nom_fichier} supprimé avec succès.")
            except:
                print(f"Le fichier {nom_fichier} n'existe pas.")
        
        else:
            print("Choix invalide.")
        
        reponse = input("Voulez-vous effectuer une autre opération ? (Oui/Non) : ").strip().lower()
        if reponse != 'oui':
            break

if __name__ == "__main__":
    main()
