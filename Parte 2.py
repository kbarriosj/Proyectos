import math
n_zonas = float(input("Ingrese el numero de zonas a analizar: "))
if n_zonas > 0:
    i=1
    antenas_a = 0
    antenas_b = 0
    antenas_c = 0
    antenas_d = 0
    antenas_e = 0
    total_antenas = 0
    while i <= n_zonas:
        Area = float(input(f"Ingrese el area zona {i}: "))
        Antenas_viejas = float(input(f"Ingrese el numero de antenas ya instaladas en zona {i}: "))
        Antena_nueva = str(input(f"Ingrese el tipo de antenas a instalar en zona {i} (a b c d e): "))
        
        if Antenas_viejas % 1 == 0:
            Antenas_viejas = int(Antenas_viejas)
            if Antenas_viejas >= 0 and (Antena_nueva == "a" or Antena_nueva == "b" or Antena_nueva == "c" or Antena_nueva == "d" or Antena_nueva == "e"):
                if Antena_nueva == "a":
                    x = 50600
                elif Antena_nueva == "b":
                    x = 19200
                elif Antena_nueva == "c":
                    x = 36900
                elif Antena_nueva == "d":
                    x = 40500
                elif Antena_nueva == "e":
                    x = 34200
                Numero_antenas_nuevas = math.ceil((Area - 16600*Antenas_viejas)/x) 
                if Numero_antenas_nuevas <0:
                    Numero_antenas_nuevas = 0
                else:
                    total_antenas = total_antenas + Numero_antenas_nuevas
            
            else:
                Numero_antenas_nuevas = 0
        else:
            Numero_antenas_nuevas = 0
        if Antena_nueva == "a":
            antenas_a = antenas_a + Numero_antenas_nuevas
        elif Antena_nueva == "b":
            antenas_b = antenas_b + Numero_antenas_nuevas
        elif Antena_nueva == "c":
            antenas_c = antenas_c + Numero_antenas_nuevas
        elif Antena_nueva == "d":
            antenas_d = antenas_d + Numero_antenas_nuevas
        elif Antena_nueva == "e":
            antenas_e = antenas_e + Numero_antenas_nuevas
       
        i += 1
    porcentaje_a = format(((antenas_a * 100)/total_antenas), '0.2f')
    porcentaje_b = format(((antenas_b * 100)/total_antenas), '0.2f')
    porcentaje_c = format(((antenas_c * 100)/total_antenas), '0.2f')
    porcentaje_d = format(((antenas_d * 100)/total_antenas), '0.2f')
    porcentaje_e = format(((antenas_e * 100)/total_antenas), '0.2f')
    print("", str(total_antenas),"\n a", str(porcentaje_a)+"%","\n b", str(porcentaje_b)+"%","\n c", str(porcentaje_c)+"%","\n d", str(porcentaje_d)+"%","\n e", str(porcentaje_e)+"%")
else:
    total_antenas = 0
    porcentaje_a = format(0, '0.2f')
    porcentaje_b = format(0, '0.2f')
    porcentaje_c = format(0, '0.2f')
    porcentaje_d = format(0, '0.2f')
    porcentaje_e = format(0, '0.2f')
    print("", str(total_antenas),"\n a", str(porcentaje_a)+"%","\n b", str(porcentaje_b)+"%","\n c", str(porcentaje_c)+"%","\n d", str(porcentaje_d)+"%","\n e", str(porcentaje_e)+"%")