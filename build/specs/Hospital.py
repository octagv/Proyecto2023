from tableUtils import *
class Hospital():
    def __init__(self):
        self.Pacientes = []
        self.Doctores = []
        self.Medicamentos = []
        self.dailystats = []
        self.monthlystats = []
    def addDoctorTable(self, table):
        self.Doctores = table
    def addMedicamentsTable(self, table):
        self.Medicamentos = table
    def addPacientsTable(self, table):
        self.Pacientes = table
    def addDailyStatsTable(self, table):
        self.dailystats = table
    def addMonthlyStatsTable(self, table):
        self.monthlystats = table
    def exportTable(self, table, dir):
        TableToDataFrame(table).to_csv(dir, index = False)
    def importTable(self, dir):
        return DataFrameToTable(pd.read_csv(dir))
    def grafDailyPacients(self, initial, end):
        pass
    def grafMonthlyPacients(self, initial, end):
        pass
    def update(self):
        pass
    def addDoctor(self, doctor):
        self.Doctores.append(doctor)
    def addMedicaments(self, medicamento):
        self.Medicamentos.append(medicamento)
    def addPacient(self, paciente):
        self.Pacientes.append(paciente)
    

