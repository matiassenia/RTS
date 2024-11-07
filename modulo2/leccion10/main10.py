while True:
    print("Selecciona una opción:")
    print("9 - Tabla de multiplicar")
    print("0 - Salir")

    # Pedir al usuario que elija una opción
    answer = int(input("Ingresa el número de la opción: "))

    if answer == 9:
        # Mostrar la tabla de multiplicar
        for num1 in range(1, 10):
            for num2 in range(1, 10):
                print(f"{num1} * {num2} = {num1 * num2}")
            print("-------")
    elif answer == 0:
        # Salir del bucle
        print("Saliendo del programa.")
        break
    else:
        # Opción inválida
        print("Opción no válida. Intenta de nuevo.")



#Ejercicio 
#ejecuta un bucle en el que el usuario pueda introducir el nombre de su juego/ pelicula favorito hasta que introduzca un stop. Todas las respuestas deben guardarse en una lista
#Ordena la lista en orden ascendente
#Imprime todos los elementos de la lista en la consola uno por uno

games = []
answer = input('Nombre de tu juego preferido')
while answer != 'para':
    games.append(answer)
    answer = input('El nombre de tu juego o para:')
games.sort()
for game in games:
	print(game) 