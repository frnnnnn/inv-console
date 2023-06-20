# imports
import re
from colorama import *


def ingresar_producto(cn, cr, r):
    cn  # inicializamos la connection

    # primero hay que crear el id del producto
    print("Desea ingresar un id de producto de formal manual o automatica?")
    decision = input("Elija una opcion (1. manual  o  2. automatico)")
    while not (decision == "1" or decision == "manual" or decision == "2" or decision == "automatico"):
        print("Por favor elija una opcion valida.")
        print("Desea ingresar un id de producto de formal manual o automatica?")
        decision = input("Elija una opcion (1. manual  o  2. automatico)")

    if decision == "1" or decision == "manual":
        while True:
            # solicitar ingreso de id
            print(
                Fore.CYAN + "Como recomendacion el id de producto puede tener formato A1234" + r)
            id = input("Ingrese el id: ").upper()
            if len(id) < 5 or len(id) > 5:
                print(Fore.RED+"Asegurese que el ID tenga 5 caracteres!" + r)

            elif len(id) == 5:
                # Validamos que la primera Letra sea un var y el resto integers
                while not (id[0].isalpha() and id[1:].isdigit() and len(id) == 5):
                    print(
                        Back.RED + "Asegúrese de que el primer carácter sea una letra y el resto solo números" + r)
                    print(Back.YELLOW +
                          "El id de producto puede tener el formato A1234" + r)
                    id = input(Fore.YELLOW + "Ingrese el id: " + r).upper()

                # Validamos que el codigo ingresado no exista.
                sw = True
                cr.execute(f"select * from persona where id = '{id}'")
                for i in cr:
                    sw = False
                    print(Fore.RED+"------------------------")
                    print(
                        "El ID ingresado ya existe en la base de datos, por favor escoja otro.")
                    print("------------------------" + r)

                if sw:
                    print(Fore.GREEN + "Codigo Valido!" + r)
                    break
        while True:
            # crear nombre del producto
            nombre = input(
                Fore.YELLOW + "Ingrese un nombre para el articulo: " + r)
            if len(nombre) < 2 or len(nombre) > 15:
                print(
                    Fore.RED + "El nombre del producto debe tener entre 2 y 15 caracteres" + r)
            else:
                break

        while True:
            # precio del producto
            while True:
                try:
                    precio = int(
                        input(Fore.YELLOW + "Ingrese un precio para el articulo: " + r))
                    break
                except ValueError:
                    print(Fore.RED + "Debe ingresar un precio de tipo numerico" + r)
            if precio <= 0:
                print(Fore.RED + "Debe ingresar un precio mayor que Cero (0)" + r)
            else:
                break

        while True:  # stock
            while True:
                try:
                    stock = int(
                        input(Fore.YELLOW + "Ingrese las unidades para el articulo: " + r))
                    break
                except ValueError:
                    print(Fore.RED + "Debe ingresar un valor numerico." + r)
            if stock <= 0:
                print(Fore.RED + "Debe ingresar unidades mayor que Cero (0)" + r)
            else:
                break

        while True:  # descripcion
            descripcion = input(
                Fore.YELLOW + "Ingrese la descripcion para el articulo: " + r)
            if len(descripcion) <= 0:
                print(
                    Fore.RED + "Debe una descripcion con caracteres mayor que Cero (0)" + r)

    elif decision == "2" or decision == "automatico":
        pass


def verificar_email(email):
    # Patrón de expresión regular para validar el email
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    # Verificar si el email coincide con el patrón
    if re.match(patron, email):
        return True
    else:
        return False

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def auth(cn, cr, r):
    cn
    repeat = True

    while repeat:
        while True:
            print(Fore.LIGHTBLUE_EX +
                  "El formato del correo puede ser: usuario@example.com" + r)
            mail = input(Fore.GREEN+"Ingrese un correo: " + r)
            is_true = verificar_email(mail)

            if is_true:
                break
            else:
                print(Fore.RED+"El correo ingresado no es valido." + r)

        while True:
            sw = True
            password = input(Fore.GREEN+"Ingrese su contraseña: " + r)

            cr.execute(
                f"select * from users where mail = '{mail}' and password = '{password}';")

            for i in cr:
                sw = False
                print(Fore.GREEN + "INGRESO EXITOSO!" + r)
                return mail
            if sw:
                print(Fore.RED + "INGRESO FALLIDO" + r)
                while True:
                    dsc = input(
                        Fore.YELLOW + "¿Desea cambiar el correo? si/no : " + r).lower()
                    while not (dsc == "si" or dsc == "no"):
                        print(Fore.RED + "Ingrese una Respuesta valida!" + r)
                        dsc = input(
                            Fore.YELLOW + "¿Desea cambiar el correo? si/no : " + r).lower()
                    if dsc == "no":
                        repeat = False
                        return False
                    break
                break

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def type_user(cn, cr, ml):
    cn
    sw = True

    cr.execute(
        f"SELECT nombre, roles_id_rol, mail_fk FROM personas where mail_fk = '{ml}';")
    for i in cr:
        sw = False
        if i[1] == 2:
            return "bodeguero"
        elif i[1] == 1:
            return "administrador"


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main_admin(cn, cr):
    cn
    print(Fore.YELLOW + """
     _     _                           _     _       
    | |   (_)                         (_)   | |      
    | |__  _  ___ _ ____   _____ _ __  _  __| | ___  
    | '_ \| |/ _ \ '_ \ \ / / _ \ '_ \| |/ _` |/ _ \ 
    | |_) | |  __/ | | \ V /  __/ | | | | (_| | (_) |
    |_.__/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\___/ 
                                                    
                                                    
    """ + Style.RESET_ALL)

    while True:
        while True:
            try:
                sw = int(input(""" 
                --- // MENÚ // ---       
                1.- Creacion de cuentas de usuario.
                2.- Consultar productos
                3.- Venta de productos
                4.- Salir del menú
                
                Seleccione una opcion: """))
                while not (sw == 1 or sw == 2 or sw == 3 or sw == 4):
                    print("ingrese una opcion valida")
                    sw = int(input(""" 
                    --- // MENÚ // ---      
                 1.- Creacion de cuentas de usuario.
                 2.- Consultar productos
                 3.- Venta de productos
                 4.- Salir del menú
                
                 Seleccione una opcion: """))
                break
            except ValueError:
                print("ingrese valores numericos")

        if sw == 1:
            main_admin_1(cn, cr)
            pass

        elif sw == 2:
            pass

        elif sw == 3:
            pass

        elif sw == 4:
            break

    pass

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def main_admin_1__(cn, cr):
    cn
    check1 = check2 = False
    repeat = True

    while repeat:

        print(Fore.BLUE + "--/CREACION DE CUENTAS DE USUARIO/--" + Style.RESET_ALL)

        print(Fore.LIGHTBLUE_EX +
              "El formato del correo puede ser: usuario@example.com" + Style.RESET_ALL)
        while True:
            sw = True
            mail = input(Fore.GREEN+"Ingrese un correo: " + Style.RESET_ALL)
            is_true = verificar_email(mail)
            if is_true:
                cr.execute(f"select * from users where mail = '{mail}'")
                for i in cr:
                    sw = False
                    print(
                        Fore.RED + "El correo ya existe, por favor escoja otro." + Style.RESET_ALL)

                if sw:
                    check1 = True
                    print(Fore.GREEN + "Correo Valido!" + Style.RESET_ALL)
                    break
            else:
                print(
                    Fore.RED + "El correo no es valido, intentelo nuevamente." + Style.RESET_ALL)

        while True:
            contrasena = input(
                Fore.YELLOW + "Ingrese una Contraseña: " + Style.RESET_ALL)
            if len(contrasena) < 4 or len(contrasena) > 10:
                print(
                    Fore.RED + "La contraseña debe tener entre 4 y 10 caracteres." + Style.RESET_ALL)
            else:
                check2 = True
                print(Fore.GREEN + "Contraseña Valida!" + Style.RESET_ALL)
                break

        while True:
            if check1 and check2:
                cr.execute(
                    f"insert into users values('{mail}', '{contrasena}')")
                cn.commit()
                print(Fore.GREEN + "Creacion de cuenta completada!" + Style.RESET_ALL)
                break

        while True:
            """dsc = input(
                Fore.YELLOW + "¿Desea agregar otra cuenta? si/no : " + Style.RESET_ALL).lower()
            while not (dsc == "si" or dsc == "no"):
                print(Fore.RED + "Ingrese una Respuesta valida!" + Style.RESET_ALL)
                dsc = input(
                    Fore.YELLOW + "¿Desea agregar otra cuenta? si/no : " + Style.RESET_ALL).lower()
            if dsc == "no":
                repeat = False
            break"""


def main_admin_1(cn, cr):
    cn
    repeat = True

    while repeat:
        print(Fore.BLUE + "--/CREACION DE CUENTAS DE USUARIO/--" + Style.RESET_ALL)

        while True:
            nombre = input(
                Fore.YELLOW + "Ingrese el NOMBRE del empleado: " + Style.RESET_ALL)
            if len(nombre) < 2:
                print(
                    Fore.RED + "El nombre debe tener minimo 2 caracteres." + Style.RESET_ALL)
            else:
                break

        while True:
            apellido = input(
                Fore.YELLOW + "Ingrese el APELLIDO del empleado: " + Style.RESET_ALL)
            if len(nombre) < 2:
                print(
                    Fore.RED + "El APELLIDO debe tener minimo 2 caracteres." + Style.RESET_ALL)
            else:
                break

        while True:
            try:
                telefono = int(input(
                    Fore.YELLOW + "Ingrese numero de TELEFONO del empleado: " + Style.RESET_ALL))
                tel_str = str(telefono)
                while True:
                    if len(tel_str) != 9:
                        print(Fore.RED + "El TELEFONO debe tener 9 numeros." + Style.RESET_ALL)
                        print(Fore.RED + "Por ejemplo: 912345678." + Style.RESET_ALL)
                        telefono = int(input(
                        Fore.YELLOW + "Ingrese numero de TELEFONO del empleado: " + Style.RESET_ALL))
                        tel_str = str(telefono)
                    else: 
                        break
                break
            except ValueError:
                print(
                    Fore.RED + "Ingrese un numero de telefono de tipo numerico." + Style.RESET_ALL)

        while True:

            print(
                Fore.GREEN + "LOS ACTUALES ROLES SON: 1. administrador o 2. bodeguero" + Style.RESET_ALL)
            id_rol = input(Fore.YELLOW + "Ingrese el rol " + Style.RESET_ALL).lower()
            while not (id_rol == '1' or id_rol == '2' or id_rol == 'admin' or id_rol == 'bodeguero'):
                print(Fore.RED + "Debe elegir una de las DOS opciones." + Style.RESET_ALL)
                print(
                Fore.GREEN + "LOS ACTUALES ROLES SON: 1. admin o 2. bodeguero" + Style.RESET_ALL)
                id_rol = input(Fore.YELLOW + "Ingrese el rol " + Style.RESET_ALL).lower()
            if id_rol == '1' or id_rol == 'administrador':
                id_rol = 1
                break
                
            elif id_rol == '2' or id_rol == 'bodeguero':
                id_rol = 2
                break
        
        while True:
            print(Fore.BLUE + "--/CREACION DEL CORREO DEL USUARIO/--" + Style.RESET_ALL)
            print(Fore.LIGHTBLUE_EX +
                "El formato del correo puede ser: usuario@example.com" + Style.RESET_ALL)
            while True:
                sw = True
                mail = input(Fore.GREEN+"Ingrese un correo: " + Style.RESET_ALL)
                is_true = verificar_email(mail)
                if is_true:
                    cr.execute(f"select * from users where mail = '{mail}'")
                    for i in cr:
                        sw = False
                        print(
                            Fore.RED + "El correo ya existe, por favor escoja otro." + Style.RESET_ALL)

                    if sw:
                        check1 = True
                        print(Fore.GREEN + "Correo Valido!" + Style.RESET_ALL)
                        break
                else:
                    print(
                        Fore.RED + "El correo no es valido, intentelo nuevamente." + Style.RESET_ALL)

            while True:
                contrasena = input(
                    Fore.YELLOW + "Ingrese una Contraseña: " + Style.RESET_ALL)
                if len(contrasena) < 4 or len(contrasena) > 10:
                    print(
                        Fore.RED + "La contraseña debe tener entre 4 y 10 caracteres." + Style.RESET_ALL)
                else:
                    check2 = True
                    print(Fore.GREEN + "Contraseña Valida!" + Style.RESET_ALL)
                    break

            while True:
                if check1 and check2:
                    cr.execute(
                        f"insert into users values('{mail}', '{contrasena}')")
                    cn.commit()
                    ###########################
                    cr.execute(f"insert into personas(nombre, apellido, telefono, roles_id_rol, mail_fk) values('{nombre}', '{apellido}', {telefono}, {id_rol}, '{mail}');")
                    cn.commit()
                    print(Fore.GREEN + "Creacion de cuenta completada!" + Style.RESET_ALL)
                    break
            
            while True:
                dsc = input(
                    Fore.YELLOW + "¿Desea agregar otra cuenta? si/no : " + Style.RESET_ALL).lower()
                while not (dsc == "si" or dsc == "no"):
                    print(Fore.RED + "Ingrese una Respuesta valida!" + Style.RESET_ALL)
                    dsc = input(
                        Fore.YELLOW + "¿Desea agregar otra cuenta? si/no : " + Style.RESET_ALL).lower()
                if dsc == "no":
                    repeat = False
                break
            break