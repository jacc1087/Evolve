estudiantes = ["Ana", "Luis", "Carlos", "Marta", "Sofía"]

for estudiante in estudiantes:
    print(f"Hola, {estudiante}!")

print(estudiantes[0])
print(estudiantes[-1])

estudiantes.append("Jorge")
estudiantes.remove("Carlos")

for estudiante in estudiantes:
    print(f"Hola a la nueva clase, {estudiante}!")