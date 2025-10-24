info_estudiante = {
    "nombre": "Alice",
    "edad": 25,
    "universidad": "UJA"
}

print(info_estudiante["nombre"]) # Acceder al valor asociado a la clave "nombre"
print(info_estudiante["edad"])   # Acceder al valor asociado a la clave "edad"

# Añadir más datos al diccionario
info_estudiante["grado"] = "Ingeniería Informática"

for clave, valor in info_estudiante.items():    
    print(f"{clave}: {valor}")