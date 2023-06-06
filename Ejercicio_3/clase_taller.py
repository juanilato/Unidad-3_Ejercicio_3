

class TallerCapacitacion:
    def __init__(self, idTaller: int, nombre: str, vacantes: int, montoInscripcion: int):
        self.__id = idTaller
        self.__nombre = nombre
        self.__vacantes = vacantes
        self.__montoIns = montoInscripcion
        self.__inscripciones = []
    def inscribirPersona(self, inscripcion):
        self.__vacantes -= 1
        self.__inscripciones.append(inscripcion)
    def getNombre(self):
        return self.__nombre
    def getMonto(self):
        return self.__montoIns
    def listaPersonas(self):
        for inscripcion in self.__inscripciones:
            print(inscripcion.getPersona())
    def __str__(self):
        cadena = self.__nombre + " "
        return cadena
    def getID(self):
        return self.__id