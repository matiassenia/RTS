import datetime


#Acceso

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

print('Hola, soy tu asistente virtual')
bot_name = input('¿Cómo quieres que me llame??')
print({bot_name.title()}, '... es una buena idea')

print('Para completar la configuración, necesito saber un poco sobre ti')
name = input('¿Cómo te llamas?')
print('Mucho gusto', {name.title()})
age = input('¿Cuántos años tienes?')
city = input('¿De qué ciudad eres?')
hobby = input('¿Cuál es tu hobby')
games = input('¿Qué tipo de juegos te gusta jugar?')
print('¡Genial! Ahora sé sobre ti:')
print('Tu nombre es', name)
print('Tienes', age, 'años')
print('Vives en la ciudad de', city)
print('Tu hobby es:', hobby)
print('Tus juegos favoritos son:', games)


# Creación del asistente para resolver problemas matematicos
# Tarea 2 - 
# Enseña al asistente a realizar todas las operaciones matemáticas

print('Hola, soy yo de nuevo,', {bot_name.title()})
print({name.title()}, 'puedo ayudarte a resolver tus tareas')
num1 = int(input('Ingresa el primer número: '))
num2 = int(input('Ingresa el segundo número: '))
print('Suma', num1 + num2)
print('Resta', num1 - num2)
print('Multiplicación', num1 * num2)
print('División', num1 / num2)
print('Exponenciación', num1 ** num2)


#Tarea lección 4
#Agrega la solucion de tu tarea al asistente

print(f'Hola {name.title()}. ¿En qué puedo ayudarte?')
print('1 - Obtener la hora')
print('2 - Obtener la fecha')
print('3 - Calculadora')
print('4 - Encontrar el área de un rectángulo')
print('5 - Resolver una ecuación cuadrática')
answer = int(input('¿En qué puedo ayudarte?'))
if answer == 1:
	...
if answer == 2:
	...
if answer == 3:
	...
if answer == 4:
	...
if answer == 5:
	...