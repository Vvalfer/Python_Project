from cryptography.fernet import Fernet


def generer_cle():
    return Fernet.generate_key()


def chiffrer_fichier(nom_fichier, cle):
    with open(nom_fichier, 'rb') as file:
        data = file.read()

    cipher = Fernet(cle)
    encrypted_data = cipher.encrypt(data)

    with open(f'{nom_fichier}.encrypted', 'wb') as file:
        file.write(encrypted_data)
    print("Fichier chiffré avec succès !")

def dechiffrer_fichier(nom_fichier_chiffre, cle):
    with open(nom_fichier_chiffre, 'rb') as file:
        data = file.read()

    cipher = Fernet(cle)
    decrypted_data = cipher.decrypt(data)

    with open('fichier_dechiffre.txt', 'wb') as file:
        file.write(decrypted_data)
    print("Fichier déchiffré avec succès !")


if __name__ == "__main__":
    cle = generer_cle()  
    fichier_original = 'mon_fichier.txt'

    chiffrer_fichier(fichier_original, cle) 
    fichier_chiffre = 'mon_fichier.txt.encrypted'

    dechiffrer_fichier(fichier_chiffre, cle)  
