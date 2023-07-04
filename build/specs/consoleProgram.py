from AWSserver import DataBase
from TableClass import Table
from tableUtils import *


print("Bienvenido al sistema interactivo del Hospital")

while True:
    sentence = input(">>")
    if sentence == "help":
        print("""Comandos
        verMedicos-verMedicamentos-verPacientes-Resetear-getTime-Actualizar
        agregarPaciente- AgregarMedicamento - AgregarDoctor""")
    else:
        print("Comando desconocido")
