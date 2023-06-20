import pymysql as driver
from colorama import *
import functions

def main():
    # Establece una conexión
    connection = driver.connect(
        host= "34.127.24.176",
        database= "railway",
        user= "root",
        password= "i1qOmj8f7EHW1efIUh7F",
        port = 7121
    )
    cursor = connection.cursor()
    reset = Style.RESET_ALL
    
    #Inicio de la aplicacion
    mail = functions.auth(connection, cursor, reset)
    ######################################################


    if isinstance(mail, str):
        #Validacion sobre que tipo de usuario es, si es admin se ejecuta la interfaz de administrador en cambio solo se ejecutaria la interfaz de bodeguero.
        tipo = functions.type_user(connection, cursor, mail)

        if tipo == "administrador":
            functions.main_admin(connection, cursor)
        
        elif tipo == "bodeguero":
            print("pobre xd")
        
    print(tipo)
    

if __name__ == "__main__":
    main()
