
#Importer le module PIL pour manipuler des images
from PIL import Image, ImageFilter
#Importer le module matplotlib.pyplot pour afficher des images
import matplotlib.pyplot as plt

# Fonction pour charger une image à partir de son emplacement
def charger_image(chemin):
    #Ouvrir l'image avec la méthode open du module Image
    return Image.open(chemin)

# Fonction pour appliquer le filtre noir et blanc à l'image
def noir_et_blanc(image):
    #Convertir l'image en mode noir et blanc (binaire) avec la méthode convert du module Image
    #Le paramètre '1' indique la conversion en noir et blanc (binaire)
    return image.convert('1')

# Fonction pour mettre le filtre de flou à l'image
def flou(image):
    #Appliquer le filtre de flou à l'image avec la méthode filter du module Image
    #Le paramètre ImageFilter.BLUR indique le type de filtre à utiliser
    return image.filter(ImageFilter.BLUR)

# Fonction pour mettre les bordures à l'image
def renforcement_bords(image):
    #Appliquer le filtre de renforcement des bords à l'image avec la méthode filter du module Image
    #Le paramètre ImageFilter.EDGE_ENHANCE_MORE indique le type de filtre à utiliser
    return image.filter(ImageFilter.EDGE_ENHANCE_MORE)

# Fonction pour afficher une image avec un titre
def afficher_image(image, titre):
    #Afficher l'image avec la fonction imshow du module matplotlib.pyplot
    #Le paramètre cmap='gray' indique le mode de couleur à utiliser (gris)
    plt.imshow(image)
    #Ajouter un titre à l'image avec la fonction title du module matplotlib.pyplot
    plt.title(titre)
    #Montrer l'image avec la fonction show du module matplotlib.pyplot
    plt.show()

def main():
    #Charger l'image à partir de son emplacement avec la fonction charger_image
    image_originale = charger_image("day6/Butterfly.jpg")

    #Afficher le titre du programme
    print("***********Programme de modification d'image**************")
    #Créer une boucle infinie pour le menu du programme
    while True:
        #Afficher le menu avec les options possibles
        print("Menu :")
        print("1 - Afficher l'image originale")
        print("2 - Noir et Blanc")
        print("3 - Flou")
        print("4 - Bordures")

        #Demander à l'utilisateur de choisir une option
        choix = input("Choisissez une option (1/2/3/4) : ")

        #Exécuter une action en fonction de l'option choisie
        if choix == '1':
            #Afficher l'image originale avec la fonction afficher_image
            afficher_image(image_originale, "Image Originale")
        elif choix == '2':
            #Appliquer le filtre noir et blanc à une copie de l'image originale avec la fonction noir_et_blanc
            #La méthode copy du module Image permet de créer une copie de l'image sans modifier l'originale
            image_filtree = noir_et_blanc(image_originale.copy())
            #Afficher l'image filtrée avec la fonction afficher_image
            afficher_image(image_filtree, "Image en noir et blanc")
        elif choix == '3':
            #Appliquer le filtre de flou à une copie de l'image originale avec la fonction flou
            image_filtree = flou(image_originale.copy())
            #Afficher l'image filtrée avec la fonction afficher_image
            afficher_image(image_filtree, "Image floutée")
        elif choix == '4':
            #Appliquer le filtre de renforcement des bords à une copie de l'image originale avec la fonction renforcement_bords
            image_filtree = renforcement_bords(image_originale.copy())
            #Afficher l'image filtrée avec la fonction afficher_image
            afficher_image(image_filtree, "Bordures")
        else:
            #Afficher un message d'erreur et demander à l'utilisateur de choisir une option valide
            print("Choix invalide. Choisissez entre 1/2/3/4.")

        #Demander à l'utilisateur s'il veut effectuer une autre opération
        reponse = input("Voulez-vous effectuer une autre opération ? (Oui/Non) : ").strip().lower()
        #Si la réponse n'est pas 'oui', sortir de la boucle
        if reponse != 'oui':
            break

#Si le fichier est exécuté comme script principal
if __name__ == "__main__":
    #Appeler la fonction main
    main()
