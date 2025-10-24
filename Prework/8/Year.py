class Year:
    def __init__(self, year):
        "Inicializamos el año"
        self.year = year

    def es_bisiesto(self):
        "Determina si el año es bisiesto"
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
        
try:
    year = int(input("Ingrese un año: "))
    anio= Year (year)
    if anio.es_bisiesto():
        print(f"{year} es un año bisiesto")
    else:
        print(f"{year} no es un año bisiesto")
except ValueError:
    print("Por favor, ingrese un número válido para el año.")