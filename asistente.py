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

#Configuración del asistente
print('Hola, soy tu asistente virtual')
bot_name = input('¿Cómo quieres que me llame? ')
print({bot_name.title()}, '... es una buena idea')

print('Para completar la configuración, necesito saber un poco sobre ti')
name = input('¿Cómo te llamas?')
print('Mucho gusto', {name.title()})

age = input('¿Cuántos años tienes?')
city = input('¿De qué ciudad eres?')
hobby = input('¿Cuál es tu hobby')
games = input('¿Qué tipo de juegos te gusta jugar? ')
print('¡Genial! Ahora sé sobre ti:')
print(f'Tu nombre es {name.title()}, tienes {age} años, vives en {city}, tu hobby es {hobby}, y te gusta jugar {games}.')


# Asistente para resolver problemas matematicos
print('Hola, soy yo de nuevo,', {bot_name.title()})
print({name.title()}, 'puedo ayudarte a resolver tus tareas')

num1 = int(input('Ingresa el primer número: '))
num2 = int(input('Ingresa el segundo número: '))
print('Suma', num1 + num2)
print('Resta', num1 - num2)
print('Multiplicación', num1 * num2)
print('División', num1 / num2)
print('Exponenciación', num1 ** num2)

# Menú de opcioes adicionales
print(f'Hola {name.title()}. ¿En qué puedo ayudarte?')
print('1 - Obtener la hora')
print('2 - Obtener la fecha')
print('3 - Calculadora')
print('4 - Encontrar el área de un rectángulo')

answer = int(input('¿En qué puedo ayudarte?'))
if answer == 1:
	# Opción para obtener la hora
    print("La hora actual es:", datetime.datetime.now().strftime("%H:%M:%S"))
if answer == 2:
	# Opción para obtener la fecha
    print("La fecha actual es:", datetime.datetime.now().strftime("%Y-%m-%d"))
if answer == 3:
	# Calculadora simple
    num1 = float(input('Ingresa el primer número: '))
    num2 = float(input('Ingresa el segundo número: '))
    print('Suma:', num1 + num2)
    print('Resta:', num1 - num2)
    print('Multiplicación:', num1 * num2)
    print('División:', num1 / num2 if num2 != 0 else 'No se puede dividir por cero.')
if answer == 4:
	# Calcular el área de un rectángulo
    largo = float(input('Ingresa el largo del rectángulo: '))
    ancho = float(input('Ingresa el ancho del rectángulo: '))
    area = largo * ancho
    print('El área del rectángulo es:', area)
else:
    print("Opción no válida.")