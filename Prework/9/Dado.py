import random

def tirar_dado():
    return random.randint(1, 6)

try:
    lanzamientos = int(input("¿Cuántas veces quieres lanzar el dado? "))
    for i in range(lanzamientos):
        print(f"Lanzamiento {i + 1}: {tirar_dado()}")
except ValueError:
    print("Por favor, ingresa un número válido.")








