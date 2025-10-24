contador = 0

for numero in range(1, 21):
    if numero % 2 == 0:
        contador += 1

print(f"Hay {contador} números pares entre 1 y 20.")