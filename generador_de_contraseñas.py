import random

# Generador de contraseñas
caracteres = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
print("este es un generador de contraseñas")

long = int(input("Por favor, digite la longitud de la contraseña: "))

contraseña = ""

for i in range(long):

    carac_aleatorio = random.choice(caracteres)

    contraseña += carac_aleatorio

print("Contraseña generada:", contraseña)