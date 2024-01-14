from PIL import Image, ImageFilter #importe les classes Image et ImageFilter du module PIL (Pillow). 
#Image est utilisé pour représenter et manipuler des images, et ImageFilter contient divers filtres que vous pouvez appliquer aux images.

import matplotlib.pyplot as plt #importe la sous-bibliothèque pyplot de Matplotlib sous le nom plt. 
#Matplotlib est utilisé ici pour afficher les images.

# Fonction pour charger une image à partir de son emplacement
def charger_image(chemin):
    return Image.open(chemin)

# Fonction pour appliquer le filtre noir et blanc à l'image
def noir_et_blanc(image):
    return image.convert('L') #'L' indique la conversion en noir et blanc.

# Fonction pour mettre le filtre de flou à l'image
def flou(image):
    return image.filter(ImageFilter.BLUR) #ImageFilter.BLUR est une constante de la bibliothèque Pillow représentant le filtre de flou.

# Fonction pour mettre les bordures à l'image
def renforcement_bords(image):
    return image.filter(ImageFilter.EDGE_ENHANCE_MORE) #ImageFilter.EDGE_ENHANCE_MORE est une constante de la bibliothèque Pillow représentant le filtre de renforcement des bords

# Fonction pour afficher une image avec un titre
def afficher_image(image, titre):
    plt.imshow(image) #plt.imshow() pour afficher l'image
    plt.title(titre) #plt.title() pour ajouter un titre a l'image
    plt.show()


def main():
   
    #chemin_image = "day6/Butterfly.jpg"
    
    
    image = charger_image("day6/Butterfly.jpg")
    
    print("***********Programme de modification d'image**************")
    while True:
       
        print("Menu :")
        print("1 - Afficher l'image originale")
        print("2 - Noir et Blanc")
        print("3 - Flou")
        print("4 - Bordures")

       
        choix = input("Choisissez une option (1/2/3/4) : ")

      
        if choix == '1':
            afficher_image(image, "Image Originale")

        
        elif choix == '2':
            image = noir_et_blanc(image)
            afficher_image(image, "Image en blanc-noir")
        elif choix == '3':
            image = flou(image)
            afficher_image(image, "Image flouter")
        elif choix == '4':
            image = renforcement_bords(image)
            afficher_image(image, "Bordures")
        else:
            print("Choix invalide.Choisissez entre 1/2/3/4.")

       
        reponse = input("Voulez-vous effectuer une autre opération ? (Oui/Non) : ").strip().lower()
        if reponse != 'oui':
            break

   


if __name__ == "__main__":
    main()
