from clase_inscripcion import Inscripcion
import numpy as np

class ManejaInscripcion:
    def __init__(self):
        self.__arreglo = np.array([], dtype = Inscripcion)
    def crear(self, persona, taller, fecha):
        inscripcion = Inscripcion(fecha, False, persona, taller)
        self.__arreglo = np.append(self.__arreglo, inscripcion)
        return inscripcion
    def mostrar(self):
        for inscripcion in self.__arreglo:
            print(inscripcion)
    def buscaDNI(self, dni):
        band = False
        i = 0
        while i < len(self.__arreglo) and band == False:
            if self.__arreglo[i].dni() == dni:
                band = True
            else:
                i += 1
        if band:
            inscripcion = self.__arreglo[i]    
        else:
            inscripcion = -1
        return inscripcion
    def buscaPago(self, dni):
        band = False
        i = 0
        while i < len(self.__arreglo) and band == False:
            if self.__arreglo[i].dni() == dni:
                band = True
            else:
                i += 1
        if band:
            indice = i    
        else:
            indice = -1
        return indice
    
    
    def realizarPago(self, i):
        self.__arreglo[i].cambioPago(True)
    def guardar(self):
        with open("datos.csv", "w") as archivo:
            for objeto in self.__arreglo:
                cadena = str(objeto.getCadena()) + '\n'
                archivo.write(cadena)
        