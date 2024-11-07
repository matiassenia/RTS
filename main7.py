#Tarea práctica
#Etapa 1: Escribe un código que adivine un número aleatorio entre 1 y 100
#Etapa 2: Ehecutar el bucle principañ del juego
#por ejemplo, un infinito
#Etapa 3: El usuario ingresa un número
#Dentro del bucle damos al usuario la oportunidad de introducir un número
#Etapa 4: Comprobar si el usuario ha adivinado el numero 
# Si el usuario adivina, emitimos el mensaje  `¡Felicidades! ¡Has adivinado el número!`
#En otros casos, puedes darle una pista, por ejemplo:  `¡El número es demasiado grande! ¡Intenta de nuevo!`
#Agrega un numero limitado de intentos



import random
number = random.randint(1, 100)

attempts = 0

while True:
	guess = int(input('Adivina el número del 1 al 100'))
	attempts += 1
	
	if guess > number:
		print('El número es demasiado grande, ¡inténtalo de nuevo!')
	elif guess < number:
		print('El número es demasiado pequeño, ¡inténtalo de nuevo!')
	else:
		print(f'¡Enhorabuena! ¡Has adivinado el número en {attempts} de intentos!')
		
	if attempts == 10:
		print('¡Se acabaron los intentos!')
		break