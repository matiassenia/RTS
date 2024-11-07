#Ejercicio
#Usando el bucle for y la función range() obten todos los numeros pares del 1 al 100

# variante 1
for number in range(1, 101, 2):
    print(number)

# variante 2
for number in range(1, 101):
	if number % 2 == 0:  # comprobamos que no queda resto al dividir entre 2
            print(number)
            
#Ejercicio practico
#Escribe un programa que genere la tabla de multiplicar del número 5

for number in range(1, 10):
	print(5 * number)


