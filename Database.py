import mysql.connector
from mysql.connector import Error

cas = ['a','b','c','d','e','f','g','h']
target = ['a','b','c','d','e','f','g','h']

class Database:
    def __init__(self):
        try:
            self.databaseConection = mysql.connector.connect(
                host="zemoga-test-db.crhpedy9xxto.us-east-1.rds.amazonaws.com",
                port=3306,
                user="zemoga_test_db",
                password="Zem0ga.101",
                db='zemoga_test_db'
                )
            if self.databaseConection.is_connected():
                print("conexión exitosa")
                infoserver = self.databaseConection.get_server_info()
                print("información del servidor:", infoserver)
        except Error as ex:
            print("error durante la conexión:", ex)

    def get_all(self):
        cursor = self.databaseConection.cursor()
        cursor.execute("SELECT * FROM portfolio")
        data = cursor.fetchall()
        for x in data:
            print(x)

    def create(self, profile):
        cursor = self.databaseConection.cursor()
        sql = (
            "INSERT INTO `portfolio` (idportfolio, description, image_url, twitter_user_name, email, experience_summary, last_names, names) VALUE (  default, %s, %s, %s, %s, %s, %s, %s);"
        )
        cursor.execute(sql, profile)
        self.databaseConection.commit()

db = Database()

