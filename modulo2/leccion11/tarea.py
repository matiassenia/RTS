#crea una lista de notas 
#Escribe un programa para encontrar la media aritmetica de estas notas
#(para calcular la media aritmetica se suman todos los valores y se divide entre el numero total de datos)

marks = [5, 4, 4, 5, 3, 5, 5, 4]
sum = 0
for mark in marks:
	sum += mark
print(f' Nota promedio: {sum / len(marks)}')

