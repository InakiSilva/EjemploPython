import string
import random

print("Generador de claves de la explicación de práctica 14-03")

#creando lista de posibles caracteres para el password

chars= string.ascii_letters + string.digits + string.punctuation;

password= ""

length= 10; #longitud de password

# itera la longitud requerida de veces, generando un chars random y agregandolo a la var password

for _ in range(length):
    password = password + random.choice(chars);

print("la contraseña generada ess: ", password);





