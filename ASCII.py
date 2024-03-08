import os

motclair = "toto"
lettre_décalé= ""
motchiffré = ""
position = 0

print(motclair)
print(type(motclair))

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



for lettre in motclair :
 
 position = ord(lettre) + 2
 lettre_décalé = chr(position)


 motchiffré += lettre_décalé

print(motchiffré)