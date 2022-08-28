## Chinese Zodiac

# More info https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm

year = int(input("Ingresa el año de nacimiento: "))

def chinese_zodiac(year:int):
    elements = ("madera", "fuego", "tierra", "metal", "agua")
    animals = ("rata", "buey", "tigre", "conejo", "dragón", "serpiente", "caballo", "oveja", "mono", "gallo", "perro", "cerdo")

    if year < 604:
        print("El ciclo sexagenario chino comenzó en el año 604. Debes introducir un año adecuado.")
    else:
        sexagenary_year = (year - 4) % 60
        element = elements[int((sexagenary_year % 10) / 2)]
        animal = animals[int(sexagenary_year % 12)]

        print(f"Año: {year} / Zodiaco: {animal} de {element}")


chinese_zodiac(year)