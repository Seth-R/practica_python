entrada = input("\nIngrese Dia, Mes y Año de nacimiento"
                    "(Separados por un espacio): ")
dia_n, mes_n, anio_n = map(int, entrada.split())

print ("\ntu generacion es:\r")

if anio_n >= 1900 | anio_n<=1914:
    print ("Generación Interbellum\n")
else:
    if anio_n>=1915 | anio_n <= 1925:
        print ("Generación Grandiosa\n")
    else:
        if anio_n>= 1926 | anio_n<= 1945:
            print ("Generación Silenciosa\n")
        else:
            if anio_n>= 1946 | anio_n <= 1964:
                print ("Baby Boomers\n")
            else:
                if anio_n>=1965 | anio_n<= 1981:
                    print("Generación X\n")
                else:
                    if anio_n>=1982 | anio_n<=1996:
                        print("Generación Y o Millenials\n")
                    else:
                        if anio_n>=1997 | anio_n<=2015:
                            print("Generación Z\n")
                        else:
                            print("Generación Alfa\n")
#print (dia_n, mes_n, anio_n)