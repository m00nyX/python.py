#calculadora de clima
clima = str(input("ingrese estacion del año: "))

match clima:
    case ("verano"):
        print("ocupa ropa fresca como poleras cortas o short, el calor derrite!")
    case ("otoño"):
        print("intenta ocupar chaquetas y pantalones abrigados el viento esta fuerte!")
    case ("invierno"):
        print ("lleva sueteres calentios y pantalanos abrigados,hace mucho frio!")
    case ("primavera"):
        print (" ponte lo que mas te guste el clima esta perfecto!")
    case _:
         print ("esa estacion no existe!")