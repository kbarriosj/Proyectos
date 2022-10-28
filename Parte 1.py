import math
area_zona = float(input("Ingrese el area a instalar: "))
antenas_Existentes = int(input("Ingrese la cantidad de antenas que existen: "))
areatipo_Antenas = input("Ingrese el tipo de antenas a instalar (a, b, c, d, e): ")
if antenas_Existentes >= 0 and (areatipo_Antenas == "a" or areatipo_Antenas == "b" or areatipo_Antenas == "c" or areatipo_Antenas == "d" or areatipo_Antenas == "e"):
    if areatipo_Antenas == "a":
        y = 50600
    elif areatipo_Antenas == "b":
        y = 19200
    elif areatipo_Antenas == "c":
        y = 36900
    elif areatipo_Antenas == "d":
        y = 40500
    elif areatipo_Antenas == "e":
        y = 34200
    area = area_zona-(16600*antenas_Existentes)
    if area < 0:
        print(0)
    if area > 0:
        numero_Antenasnuevas = math.ceil (area/y)
        print(numero_Antenasnuevas)
else:
    print("Error en los datos")