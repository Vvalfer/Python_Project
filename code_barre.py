from barcode import EAN13

while True:
    number = input("Entrez un code à 13 chiffres (ou 'q' pour quitter) : ")

    if number.lower() == 'q':
        break

    while len(number) != 13 or not number.isdigit():
        print("Le code doit comporter exactement 13 chiffres. Veuillez réessayer.")
        number = input("Entrez un code à 13 chiffres (ou 'q' pour quitter) : ")

    file_name = "new_code_barre"
    my_code = EAN13(number)
    my_code.save("new_code_barre")

    print(f"Le code-barres pour {number} a été généré et enregistré en tant que {file_name}.")

print("Programme terminé.")