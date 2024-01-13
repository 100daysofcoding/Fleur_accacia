print("Veuillez choisir 3 entiers.")
Nombre1 = int(input("Entrer votre premier nombre : "))
Nombre2 = int(input("Entrer votre second nombre : "))
Nombre3 = int(input("Entrer votre dernier nombre : "))

print("--------------------------------------------------------")
print("Menu")
print(" 1-Somme ")
print(" 2-Produit ")
print(" 3-Moyenne")
print("--------------------------------------------------------")

while True:
    somme = Nombre1 + Nombre2 + Nombre3
    produit = Nombre1 * Nombre2 * Nombre3
    moyenne = (Nombre1 + Nombre2 + Nombre3) / 3

    choix_operation = input("Veuillez choisir une opération : ")

    if choix_operation == '1':
        print(f"La somme de vos différents nombres est : {somme}")
    elif choix_operation == '2':
        print(f"Le produit de vos différents nombres saisis est : {produit}")
    elif choix_operation == '3':
        print(f"La moyenne de vos différents nombres saisis est : {moyenne}")
    else:
        print("Choix invalide. Veuillez entrer 1, 2 ou 3.")

    reponse = input("Voulez-vous reprendre l'opération ? (Oui/Non): ").strip().lower()

    if reponse != 'oui':
        break
