clima = input("como esta el clima hoy?: ")

match clima:
    case ("soleado"):
          print("recuerda llevar agua y usar protector solar!")
    case ("lluvioso"):
          print(" cuidado con mojarse, lleva tu paraguas!")
    case ("nevando"):
          print ("recuerda abrigarte bien, no queremos un resfrio!")
    case ("nublado"):
            print ("lleva una chaqueta, el viento esta fuerte!")
    case _:
            print("tenemos problemas!")