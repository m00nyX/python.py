#validador de contraseñas
usuario = str(input("ingrese nombre de usuario: ")).lower()
contraseña = str(input("ingrese su contraseña: ")).lower()

if usuario == ("admin"):
    if contraseña == ("1234"):
        print("acceso total")
    elif contraseña != ("1234"):
        print("contraseña incorrecta")
    else:
        print("error")
        
elif usuario == ("invitado"):
    if contraseña == ("hola"):
        print("acceso limitado")
    elif contraseña != ("hola"):
        print("cotraseña incorrecta")
    else:
        print ("error")
else:
    print("datos incorrectos")
    

