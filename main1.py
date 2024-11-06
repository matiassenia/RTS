#Introducción al asistente virtual
#Tarea 1 - 
#Escribe un programa de presentación con tu asistente virtual
#Con este programa puedes establecer el nombre del aistente, y el asistente recopilará toda la información necesaria para su trabajo futuro

print('Hola, soy tu asistente virtual')
bot_name = input('¿Cómo quieres que me llame??')
print(bot_name, '... es una buena idea')
print('ara completar la configuración, necesito saber un poco sobre ti')
name = input('¿Cómo te llamas?')
print('Mucho gusto', name)
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