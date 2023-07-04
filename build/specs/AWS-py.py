import pymysql
from TableClass import Table
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
    def instanceDataBase(self):
        try:
            self.cursor.execute("create database kgptalkie")
        except:
            self.cursor.execute("drop database kgptalkie")
            self.cursor.execute("create database kgptalkie")
        finally:
            self.cursor.connection.commit()
            self.cursor.execute("use kgptalkie")
    def createTable(self, table):
        
        self.cursor.execute(table.createCode)
        print("Tabla creada con exito")
    
    def getTableTitles(self):
        self.cursor.execute("show tables")
        return self.cursor.fetchall()
    
    def getTable(self, tableName):
        self.cursor.execute(f"select * from {tableName}")
        return self.cursor.fetchall()
    
    def insertData(self, tableName, *values):
        code = f"insert into {tableName} values(null"
        for value in values:
            try:
                int(value)
            except:
                code += ",'" + str(value)+"'"
            else:
                code += "," + str(value)
        code += ")"
        print(code)
        self.cursor.execute(code)
        self.db.commit()
        print("Datos introducidos correctamente")



if __name__ == "__main__":
    dbs = DataBase(host="hospital.ckxz9xhtccxk.eu-north-1.rds.amazonaws.com", user="admin", password="12345678")
    pacientes = Table("Pacientes")
    pacientes.addTextVar("nombre")
    pacientes.addTextVar("apellido")
    pacientes.addTextVar("correo")
    pacientes.addIntVar("edad")
    pacientes.create()
    dbs.instanceDataBase()
    dbs.createTable(pacientes)
    dbs.insertData("Pacientes", "Octavio", "Gauto","gmail", 30)
    print(dbs.getTable("Pacientes"))
    pacientes.importVar(dbs.getTable("Pacientes"))
    print(pacientes)
