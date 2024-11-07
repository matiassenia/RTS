# Crear un diccionario con preguntas y opciones de respuesta
questions = {
    "¿Cómo se llama el pico más alto de la Tierra?": {
        'A': 'Monte Everest',
        'B': 'Kanchenjunga',
        'C': 'Kilimanjaro',
        'D': 'Makalu'
    },
    "¿Cuál es la capital de los Países Bajos?": {
        'A': 'Ámsterdam',
        'B': 'La Haya',
        'C': 'Utrecht',
        'D': 'Rotterdam'
    },
    "¿Quién escribió El Quijote?": {
        'A': 'Alexander Pushkin',
        'B': 'León Tolstoi',
        'C': 'Isabel Allende',
        'D': 'Cervantes'
    }
}

# Respuestas correctas
correct_answers = {
    "¿Cómo se llama el pico más alto de la Tierra?": "A",
    "¿Cuál es la capital de los Países Bajos?": "A",
    "¿Quién escribió El Quijote?": "D"
}

money = 0
lvl = 1

for question, answers in questions.items():
    print(question)
    for num, ans in answers.items():
        print(f'{num}: {ans}')
    answer = input('Tu respuesta: ').upper()  # Convertir respuesta a mayúscula para evitar errores de comparación
    if answer == correct_answers[question]:
        print('Respuesta correcta')
        money += 100000 * lvl
        print(f'Obtenido: {money}')
    else:
        print('Respuesta incorrecta')
        break
    lvl += 1

print(f'Total ganado: {money}')
