#Tarea para casa
#Crear un juego de cara o cruz

#Elusuario elige cara o cruz, el programa emite el resultado

import random
print('Bienvenidos al juego Cara o Cruz')
print('Elije una de las opciones: \n 1 - Cara \n 2 - Cruz')
user = int(input('Tu elección (Introduce un número entre 1 y 2): '))
bot = random.randint(1, 2)
if user == bot:
	print('Empate')
else:
	print('Derrota:(')


#Utiliza un bucle While para imprimir numeros del 1 al 100

x = 1
while x <= 100:
    print (x)
    x += 1


#Tarea para casa

#Agrega a tu programa una verificación de inicio de sesión

true_log = 'admin'
true_pass = 'admin007'
user_log = input('Ingresa tu nombre del usuario:')
user_pass = input('Ingresa tu contraseña: ')
while user_log != true_log or user_pass != true_pass:
	print('Usuario o contraseña incorrectos')
	user_log = input('Ingresa tu nombre de usuario: ')
	user_pass = input('Ingresa tu contraseña: ')
else:
	print('Se ha iniciado la sesión')