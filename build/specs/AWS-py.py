import pymysql

#db = pymysql.connect(host="hospital.ckxz9xhtccxk.eu-north-1.rds.amazonaws.com", user="admin", password="12345678")

class DataBase():
    def __init__(self, host, user, password):
        self.db = pymysql.connect(host = host, user = user, password = password)
        self.cursor = self.db.cursor()
        print("Se ha creado la Base de datos")

    def getVersion(self):
        self.cursor.execute("select version()")
        version = self.cursor.fetchone()
        print("La version es", version)

    def createTable(self, tableName):
        pass
    