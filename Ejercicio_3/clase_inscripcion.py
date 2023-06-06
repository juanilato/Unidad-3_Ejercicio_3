
class Inscripcion:
    def __init__(self, fechaIns: str, pago: bool, persona, taller):
        self.__fechaIns = fechaIns
        self.__pago = pago
        self.__persona = persona
        self.__taller = taller
    def dni(self):
        return int(self.__persona.getDNI())
    def __str__(self):
        cadena = self.__taller.getNombre()
        cadena += " " + str(self.__taller.getMonto())
        return cadena
    def getPersona(self):
        return self.__persona
    def cambioPago(self, pago):
        self.__pago = pago
        print("Pago realizado con éxito ")
    def getCadena(self):
        cadena = str(self.__persona.getDNI()) + ";"
        cadena += str(self.__taller.getID()) + ";"
        cadena += self.__fechaIns + ";"
        cadena += str(self.__pago) 
        return cadena