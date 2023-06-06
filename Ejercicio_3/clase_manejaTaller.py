import csv
from clase_taller import TallerCapacitacion

class ManejaTaller:
    def __init__(self):
        self.__lista = []
    def agregar(self, taller):
        self.__lista.append(taller)
    def carga(self):
        band = True
        archivo = open("talleres.csv")
        reader = csv.reader(archivo, delimiter = ";")
        for fila in reader:
            if band:
                band = False
            else:
                taller = TallerCapacitacion(int(fila[0]), fila[1], int(fila[2]), int(fila[3]))
                self.__lista.append(taller)
    def cargaPersona(self, i, inscripcion):
        self.__lista[i-1].inscribirPersona(inscripcion)
    def busca(self, i):
        return self.__lista[i-1]
    def muestraPersonas(self, i):
        self.__lista[i-1].listaPersonas()
                        
                