import mysql.connector
from mysql.connector import Error

cas = ['a','b','c','d','e','f','g','h']
target = ['a','b','c','d','e','f','g','h']


def conection():
    try:
        databaseConection = mysql.connector.connect(
            host="zemoga-test-db.crhpedy9xxto.us-east-1.rds.amazonaws.com",
            port=3306,
            user="zemoga_test_db",
            password="Zem0ga.101",
            db='zemoga_test_db'
        )
        if databaseConection.is_connected():
            print("conexión exitosa")
            infoserver = databaseConection.get_server_info()
            print("información del servidor:", infoserver)

        cursor = databaseConection.cursor()
        cursor.execute("SELECT * FROM portfolio")
        data = cursor.fetchall()
        for x in data:
            print(x)

    except Error as ex:
        print("error durante la conexión:", ex)

    finally:
        if databaseConection.is_connected():
            databaseConection.close()
            print("la conexión ha finalizado")


def new(target):
    try:
        databaseConection = mysql.connector.connect(
            host="zemoga-test-db.crhpedy9xxto.us-east-1.rds.amazonaws.com",
            port=3306,
            user="zemoga_test_db",
            password="Zem0ga.101",
            db='zemoga_test_db'
        )
        if databaseConection.is_connected():
            print("conexión exitosa")
            infoserver = databaseConection.get_server_info()
            print("información del servidor:", infoserver)

        cursor = databaseConection.cursor()
        sql = (
            "INSERT INTO `portfolio` VALUE ( %s, %s, %s, %s, %s, %s, %s, %s );"
        )
        cursor.execute(sql, (target))
        data = cursor.fetchall()

        for x in data:
            print(x)

    except Error as ex:
        print("error durante la conexión:", ex)

    finally:
        if databaseConection.is_connected():
            databaseConection.close()
            print("la conexión ha finalizado")

#new( cas)
cs=conection()

