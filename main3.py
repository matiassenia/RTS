#Tarea
#Pide al usuario su nombre y muestra un saludo usando f-strings
#El nombre debe comenzar con mayusculas

name = input('Ingresa tu nombre: ')
print(f'Hols {name.title()}')

#Generdor de noticias falsas
#Tarea
#Comienza a crear un generador de noticias falsas
#1. Pide el nombre de la persona sobre la cual deseas generar la noticia falsa
#2. Crea una lista que contenga las noticias falsas 
#*Incluye el nombre de la persona en cada noticia
#** Recuerda escribir el nombre con mayuscula inicial

import random

print('¿Quieres conocer un poco más sobre tu mejor amigo o alguien cercano?')
friend_name = input('Ingresa su nombre y te revelaré todos sus secretos: ')

fake_news = [
    f"{friend_name.title()} fue descubierto en una situación inesperada.",
    f"Sorprendente revelación: ¡{friend_name.title()} resultó ser una celebridad secreta!",
    f"{friend_name.title()} confesó ser un experto en tecnología.",
    f"Asustado, {friend_name.title()} fue atrapado en una aventura misteriosa.",
    f"Increíble transformación: ¡{friend_name.title()} resultó ser una estrella en ascenso!"
]

num = random.randint(0, len(fake_news) - 1)
print(fake_news[num])

#Tarea
#Implementa la impresion aleatoria de una noticia falsa de la lista

import random
print('¿Quieres conocer un poco más sobre tu mejor amigo o alguien cercano?')
friend_name = input(' Ingresa su nombre y te revelaré todos sus secretos: ')
fake_news = [
    f" {friend_name.title( )}  descubierto …",
    f" Increíble transformación:: {friend_name.title( )} resultó ser …",
    f" {friend_name.title( )} confesó ser …",
    f" Asustado {friend_name.title( )} fue atrapado en …",
    f" Increíble transformación: {friend_name.title( )} resultó ser …"
]
num = random.randint(0, len(fake_news) - 1)
print(fake_news[num])

