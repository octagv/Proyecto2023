from tableUtils import *
class Table():
    def __init__(self, tableName):
        self.title = tableName
        self.createCode = f"""create table {tableName} (
            id int not null auto_increment""" 
        self.content = []
        self.titles = []
        
        
    def __str__(self):
        text = ""
        for row in self.content:
            for column in row:
                text += str(column) + "   "
            text += "\n"
        return text
        
    def addIntVar(self, varName):
        self.createCode += f",{varName} int"
        self.titles.append(varName)

    def addTextVar(self, varName):
        self.createCode += f",{varName} text"
        self.titles.append(varName)
    

    def create(self):
        self.createCode += ",primary key (id) )"
        self.content.append(self.titles)

    def importVar(self, *args):
        for arg in args:
            self.content.append(list(arg))
        
if __name__ == "__main__":
    pacientes = Table("Pilin")
    pacientes.addTextVar("nombre")
    pacientes.addTextVar("apellido")
    pacientes.addIntVar("Edad")
    pacientes.create()
    pacientes.importVar(("Octa", "Gauto", 20), ("Ambar", "Vera", 22))
    print(pacientes)
    print(getColumn(pacientes.content,2))
