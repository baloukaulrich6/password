# generator password
# le programme vous demande combien de lettre doit contenir le password
# combien de chiffre
# combien de symnole
# genere le password

import  random

letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
 'U', 'V', 'W', 'X', 'Y', 'Z',]
number = ['0', '1', '2', '3','4', '5', '6','7', '8', '9']
symbole = ['&', '£', '?', '(', '-','_', ')', '$','¤', ']', '%', '§', '/', '#', '{', '[', '|', '^', '@', ']', '}']

print("welcome to the PyPassword Generator")
nombre_de_lettre = int(input("entre le nombre de lettre pour votre passeword?\n"))
nombre_de_symbole = int(input("entre le nombre de Symbole pour votre passeword?\n"))
nombre_de_chiffre = int(input("entre le nombre de chiffre pour votre passeword?\n"))

password = ""
for char in range(1, nombre_de_lettre + 1) :
 random_char = random.choice(letters)
 password += random_char


for sym in range(1, nombre_de_symbole  + 1) :
 random_sym = random.choice(symbole)
 password += random_sym


for num in range(1, nombre_de_chiffre  + 1) :
 random_num = random.choice(number)
 password += random_num
print(password)