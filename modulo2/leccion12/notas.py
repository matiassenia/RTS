#Etapa 1. Pensemos en cómo podría aplicarse un programa de este tipo...
#1. Añadir nota
#2. Ver todas las notas
#3. Eliminar nota
#4. Salir

#ejemplo : Elige una acción: 

notes = dict()

def add_note(title, text):
    global notes
    notes[title] = text
    print("¡La nota ha sido añadida con éxito!")

def display_notes():
    if len(notes) == 0:
        print("no hay notas por ahora")
    else:
        for title, text in notes.items():
            print(f"{title}: {text}")

def main():
    while True:
        print("1. Añadir una nota")
        print("2. Ver todas las notas")
        print("3. Eliminar una nota")
        print("4. Salir")
        choice = input("Escoge una opción: ")
        if choice == "1":
            note_title = input("Introduce el nombre de la nota: ")
            note_text = input("Introduce el texto de la nota: ")
            add_note(note_title, note_text)
        elif choice == "2":
            display_notes()
        elif choice == "3":
            pass
        elif choice == "4":
            break
        else:
            print("Código incorrecto. Inténtalo otra vez.")

main()