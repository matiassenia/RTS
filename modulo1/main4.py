#Tarea en casa
#Escribir un programa "Magic 8-Ball" que devuelva una predicción para la fecha al azar al iniciarse

import random
print('¡Descubre qué te espera hoy!')
input('¿Listo?')
magic_list = [
    "Indudablemente.", "Está predestinado.", "Sin dudas.", "Definitivamente sí.",
    "Puedes estar seguro de ello.", "Me parece que sí.", "Probablemente.",
    "Buenas perspectivas.", "Las señales dicen que sí.", "Sí.", "Pregunta más tarde.",
    "Aún no está claro, inténtalo de nuevo.", "Mejor no decirlo.", "No.",
    "Muy dudoso.", "Ni lo pienses.", "Mi respuesta es no."
]
input("Haz tu pregunta y te daré una respuesta...  ")
num = random.randint(0, len(magic_list))
print(magic_list[num])

#Tarea practica
#Inventa una contraseña y guardala en una variable. Solicita la contraseña al usuario y verificala:
#Si la contraseña es correcta, muestra "Acceso concedido"
#Si lacontraseña es incorrecta, muestra "Contraseña incorrecta"

password = 'qwerty'
user = input('Ingresa la contraseña: ')
if user == password:
	print('Acceso concedido')
if user != password:
	print('Contraseña incorrecta')


#Tarea
#Crea un asistente que pregunte que información deseamos saber(fecha o hora) y proporcione la información necesaria

import datetime
name = 'Max'
print(f'Hola {name}. ¿En qué puedo ayudarte?')
print('1 - Averiguar la hora')
print('2 - Averiguar la fecha')
answer = int(input('¿En qué puedo ayudarte?'))
if answer == 1:
	date_time = datetime.datetime.now()
	print('Hora actual:', date_time.time())
if answer == 2:
	date_time = datetime.datetime.now()
	print('Fecha actual:', date_time.date())
