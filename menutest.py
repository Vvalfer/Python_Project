import string
def chiffrement_cesar(texte, decalage):
    alpha = string.ascii_lowercase + string.ascii_uppercase + ' .'
    code = ''
    for caractere in texte:
        if caractere in alpha:
            indice = alpha.index(caractere)
            code += alpha[(indice + decalage) % len(alpha)]
        else:
            code += caractere
    return code

def dechiffrement_cesar(texte, decalage):
    return chiffrement_cesar(texte, -decalage)

def brute_force1(pin):
    for i in range(10000):
        code_essai = str(i).zfill(4)
        print(f"Essai : {code_essai}") 
        if code_essai == pin:
            return code_essai.zfill(4)
    return None

def brute_force2(mot_a_trouver, nom_fichier):
    try:
        with open(nom_fichier, 'r') as fichier:
            for mot in fichier:
                mot = mot.strip()
                print(f"Essai: {mot}")
                if mot == mot_a_trouver:
                    print(f"Fruit trouvé : {mot}")
                    return True  
        print("Fruit introuvable dans le dictionnaire.")
        return False

    except FileNotFoundError:
        print("Le fichier spécifié est introuvable.")
        return False

def menu():
    while True:
        print("\nMenu:")
        print("1. Chiffrement / Déchiffrement")
        print("2. Brute force")
        print("3. Quitter")
        choix = input("Quelle option choisissez-vous ? ")

        if choix == "1":
            sous_menu1()
        elif choix == "2":
            sousmenu2()
        elif choix =="3":
            print("Vous nous quittez déjà ?")
            break
        else:
            print("Choix invalide. Veuillez une option entre 1 et 3.")

def sous_menu1():
    print("\nSous-menu:")
    print("A. Chiffrer")
    print("B. Déchiffrer")
    choix = input("Souhaitez-vous chiffrer ou déchiffrer ? ")

    if choix.upper() == "A":
        texte = input("Entrez le texte à chiffrer : ")
        while not texte.replace(' ', '').isalpha():
            texte = input("Veuillez entrer uniquement des caractères alphabétiques : ")

        decalage = int(input("Entrez la rotation de chiffrement : "))
        texte_code = chiffrement_cesar(texte, decalage)
        print ("                       MESSAGE CODEE                    ")
        print ("------------------------------------------------------\n")
        print("Message chiffré :", texte_code)
        print ("\n------------------------------------------------------")

    elif choix.upper() == "B":
        texte = input("Entrez le texte à déchiffrer : ")
        decalage = int(input("Entrez la rotation de déchiffrement : "))
        texte_decode = dechiffrement_cesar(texte, decalage)
        print ("                      MESSAGE DECODEE                   ")
        print ("------------------------------------------------------\n")
        print("Message déchiffré :", texte_decode)
        print ("\n------------------------------------------------------")

    else:
        print("Choix invalide. Veuillez entrer A pour chiffrer ou B pour déchiffrer.")

def sousmenu2():
    print("\nSous-menu:")
    print("A. Exhaustive")
    print("B. Dictionnaire")
    choix = input("Souhaitez-vous utiliser la manière Exhaustive ou un Dictionnaire ?")

    if choix.upper() == "A":
        code_pin = input("Entrez un code PIN à 4 chiffres : ")
    
        if len(code_pin) != 4 or not code_pin.isdigit():
            print("Le code PIN doit être composé de 4 chiffres.")
            return
    
        print("Recherche du code PIN en cours...")
        resultat = brute_force1(code_pin)

        if resultat:
            print(f"Le code PIN est : {resultat}")
        else:
            print("Le code PIN n'a pas été trouvé.")

    if choix.upper() == "B":
        nom_fichier = input("Entrez le nom du fichier : ")
        mot_a_chercher = input("Entrez le fruit à chercher dans le fichier : ")
        brute_force2(mot_a_chercher, nom_fichier)

    else:
        print("Choix invalide. Veuillez entrer A pour la manière exhaustive ou B pour le dictionnaire. ")
menu()
