#Para casa
#Escribe una función delete_note() que tome el nombre de una nota como parametro y borre la nota con ese nombre

#Pista: la función comprueba si el nombre de la nota se encuentra entre las claves del diccionario y , en caso afirmativo, lo elimina.
def delete_note(title):
    if title in notes.keys():
        del notes[title]
        print(f'La nota {title} ha sido eliminada')
    else:
        print('La nota no existe')

def main():
    while True:
        print("1. Añadir una nota")
        print("2. Ver todas las notas")
        print("3. Eliminar nota")
        print("4. Salir")
        choice = input("Escoge una opción: ")
        if choice == "1":
            note_title = input("Introduce el nombre de la nota: ")
            note_text = input("Introduce el texto de la nota: ")
            add_note(note_title, note_text)
        elif choice == "2":
            display_notes()
        elif choice == "3":
            for title in notes.keys():
                print(title)
            title_to_del = input('Introduce el nombre de la nota que deseas eliminar : ')
            delete_note(title_to_del)
        elif choice == "4":
            break
        else:
            print("Entrada incorrecta. Inténtalo de nuevo.")
