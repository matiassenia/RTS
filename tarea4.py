import random
print('¡Descubre qué te espera hoy!')
input('¿Listo?')
magic_list = [
    "ndudablemente.", "Está predestinado.", "Sin dudas.", "Definitivamente sí.",
    "Puedes estar seguro de ello.", "Me parece que sí.", "Probablemente.",
    "Buenas perspectivas.", "Las señales dicen que sí.", "Sí.", "Pregunta más tarde.",
    "Aún no está claro, inténtalo de nuevo.", "Mejor no decirlo.", "No.",
    "Muy dudoso.", "Ni lo pienses.", "Mi respuesta es no."
]
input("Haz tu pregunta y te daré una respuesta...  ")
num = random.randint(0, len(magic_list))
print(magic_list[num])