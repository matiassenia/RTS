
#1.Pensemos como podría hacerse un programa de este tipo
#Plan de programa
#LIsta de pasos del hackeo
#Bucle de la salida de los elementos
#Pausas
#Paso 2. Crear una lista con las etapas del hacking
#Paso 3: Introduce los elementos de la lista mediante un bucle
#Paso 4: Perfeccionamiento
#Despues de la salida de cada elemento - están los simbolos x y ✓ random.choice() - devuelve un elemento aleatorio de la lista
#Añadamos una salida aleatoria de x y ✓ 

import random
import time

actions = ["Hackeando la NSA...",
            "Descargando archivos secretos...",
            "Usando criptoanalisis cuántico...",
            "Usando algoritmos de redes neuronales para entrar...",
            "Interceptando comunicaciones por satelite...",
            "Lanzando un gusano para evitar cortafuegos...",
            "Utilizando ingenieria social contra usuarios objetivo...",
            "Inyectando un troyano en una base de datos...",
            "Poniendo en peligro servidores de correo electronico...",
            "Cifrando los datos de la victima mediante un Ransomware..."
            ]



for action in actions:
    print(action + random.choice(["✓","x"]))
    time.sleep(random(1,2))
    

