class Persona:
    def __init__(self, nombre: str, direccion: str, dni: int):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__dni = dni
    def getDNI (self):
        return int(self.__dni)
    def __str__(self):
        cadena = self.__nombre + " "
        cadena += self.__direccion + " "
        cadena += str(self.__dni) + " "
        return cadena
