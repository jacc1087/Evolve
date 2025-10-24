#Pedimos al usuario que ingrese un año
try:
    year = int(input("Enter a year: "))

#Comprobamos si el año es bisiesto
    if(year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                print(f"{year} es un año bisiesto")
            else:
                print(f"{year} no es un año bisiesto")
        else:
            print(f"{year} es un año bisiesto")
    else:
        print(f"{year} no es un año bisiesto")

except ValueError:
    print("Por favor, ingrese un número válido para el año.")