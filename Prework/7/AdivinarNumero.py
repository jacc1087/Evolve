numero_secreto = 7
intentos = 0

while intentos < 3:
    intento = int(input("Adivina el número (entre 1 y 10): "))
    intentos += 1
    
    if intento == numero_secreto:
        print("¡Felicidades! Has adivinado el número.")
        break
    elif intento < numero_secreto:
        print("Demasiado bajo") 
    else:
        print("Demasiado alto")
else:
    print(f"Lo siento, has agotado tus intentos. El número era {numero_secreto}.") 