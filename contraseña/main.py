import random
caracteres =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
contrasena = int(input("escribe la longitud de tu contraseña: "))
contrasena2 = ""
for i in range(contrasena):
    contrasena2 = contrasena2 + random.choice(caracteres)
print (contrasena2)