fruta = input("elija una fruta: ").lower()

match fruta:
    case "manzana":
        print ("rojo o verde")
    case "platano":
        print ("amarillo")
    case "uva":
        print ("verde o morado")
    case _:
        print ("error")
        
