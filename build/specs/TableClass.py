
class Table():
    def __init__(self, tableName):
        self.title = tableName
        self.createCode = f"""create table {tableName} (
            id int not null auto_increment""" 
        
    def __str__(self):
        return self.createCode
        
    def addIntVar(self, varName):
        self.createCode += f",{varName} int"

    def addTextVar(self, varName):
        self.createCode += f",{varName} text"

    def close(self):
        self.createCode += ",primary key (id) )"
