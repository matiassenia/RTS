#Escribe un programa con el que puedas averiguar cualquier informacion sobre tu pc( o un pc que te guste). Usa un diccionario para almacenar información

user = {
    'OS': 'Windows',
    'Version': 11,
    'Processor': 'Intel Core i5',
    'RAM': 16,
    'SSD': 512
}
print('Conocer las características de la PC. Disponible:\n OS, Version, Processor, RAM, SSD')
answer = input('Introduce las características: ')
print(user[answer])