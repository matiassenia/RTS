import random

opciones = ['Piedra', 'Papel', 'Tijera']
print('¡Bienvenido al juego Piedra, Papel o Tijera!')
print('Elige una de las opciones:')
print(f'1 - {opciones[0]} \n2 - {opciones[1]} \n3 - {opciones[2]}')

# Validación de la entrada del usuario
try:
    user = int(input('Tu elección (Introduce un número entre 1 y 3): '))
    if user not in [1, 2, 3]:
        raise ValueError("El número debe estar entre 1 y 3.")
except ValueError as e:
    print(f"Entrada inválida: {e}")
    exit()

user_choice = opciones[user - 1]
print('Tu elección:', user_choice)

# Elección del ordenador
bot_choice = random.choice(opciones)
print('Elección del ordenador:', bot_choice)

# Determinación del resultado
if user_choice == bot_choice:
    print('Empate')
elif (user_choice == 'Piedra' and bot_choice == 'Tijera') or \
    (user_choice == 'Tijera' and bot_choice == 'Papel') or \
    (user_choice == 'Papel' and bot_choice == 'Piedra'):
    print('¡Victoria!')
else:
    print('Derrota :(')
