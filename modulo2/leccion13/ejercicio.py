#Escribir una funcion save_notes() que esciba el diccionario de notas en el archivo notes.json  
#Esta finción debe ser llamada despues de cada cambio del diccionario

import json

notes = dict()

def add_note(title, text):
    notes[title] = text
    print("¡Nota añadida copn éxito!")

def update_notes():
    global notes
    with open('notes.json', 'r') as json_file:
        notes = json.load(json_file)

def display_notes():
    update_notes()
    if len(notes) == 0:
        print("No hay notas por ahora.")
    else:
        for title, text in notes.items():
            print(f"{title}: {text}")

def delete_note(title):
    if title in notes.keys():
        del notes[title]
        print(f'La nota {title} fue eliminada')
    else:
        print('La nota ya no existe')

def save_notes():
    with open("notes.json", "w") as file:
        json.dump(notes, file)

def main():
    while True:
        print("\n1. Añadir una nota\n2. Ver todas las notas\n3. Borrar una nota\n4. Salir")
        choice = input("Escoge una opción: ")
        if choice == "1":
            note_title = input("Introduce el nombre de la nota: ")
            note_text = input("Introduzca el texto de la nota: ")
            add_note(note_title, note_text)
            save_notes()
        elif choice == "2":
            display_notes()
        elif choice == "3":
            update_notes()
            for title in notes.keys():
                print(title)
            title_to_del = input('Introduce el nombre de la nota a eliminar: ')
            delete_note(title_to_del)
            save_notes()
        elif choice == "4":
            break
        else:
            print("Entrada incorrecta. Inténtalo de nuevo.")

main()