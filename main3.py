#Generdor de noticias falsas
import random

print('¿Quieres conocer un poco más sobre tu mejor amigo o alguien cercano?')
friend_name = input('Ingresa su nombre y te revelaré todos sus secretos: ')

fake_news = [
    f"{friend_name.title()} fue descubierto en una situación inesperada.",
    f"Sorprendente revelación: ¡{friend_name.title()} resultó ser una celebridad secreta!",
    f"{friend_name.title()} confesó ser un experto en tecnología.",
    f"Asustado, {friend_name.title()} fue atrapado en una aventura misteriosa.",
    f"Increíble transformación: ¡{friend_name.title()} resultó ser una estrella en ascenso!"
]

num = random.randint(0, len(fake_news) - 1)
print(fake_news[num])