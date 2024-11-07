#Para casa
#En la primera lección, escribimos un programa de introduccion al asistente virtual. Haz que las respuestas del usuario se guarden en el archivo user_info.json  

import json
user_info = {
    'bot_name': input('¿Cómo quieres llamarme?'),
    'name': input('¿Cómo te llamas?'),
    'age': input('¿Cuántos años tienes?'),
    'city': input('¿De qué ciudad eres?'),
    'hobby': input('¿Cuáles son tus aficiones?'),
    'games': input('¿Qué tipo de juegos te gustan?')
}

with open("user_info.json", "w") as file:
    json.dump(user_info, file)
