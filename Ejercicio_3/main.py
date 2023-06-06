from clase_manejaTaller import ManejaTaller
from clase_manejaPersona import ManejaPersona
from clase_manejaInscripcion import ManejaInscripcion
from clase_persona import Persona
from clase_menu import Menu
import csv

if __name__ == "__main__":
    
    manejaTaller = ManejaTaller()
    
    manejaTaller.carga()
    
    manejadorPersona = ManejaPersona()
    
    manejaInscripcion = ManejaInscripcion()
    
    opciones = ["Inscribir", "Consulta Inscripción", "Consulta Inscriptos", "Registra Pago", "Guarda Inscripciones"]
    menu = Menu(5)
    menu.IngresaOpcion(opciones)    
    
    menu.Muestra()
    
    op = int(input("Ingrese opcion: "))
    while op != menu.getCantidad()+1:
        if op == 1:
            
            print("Cargue datos persona a inscribir")
            nombre = input("Nombre: ")
            direccion = input("Direccion: ")
            dni = int(input("Dni: "))
            fecha = input("Ingrese fecha actual: ")
            
            num_taller = int(input("Ingrese numero de taller a inscribir: "))
            taller = manejaTaller.busca(num_taller)
            
            persona = Persona(nombre, direccion, dni)
            manejadorPersona.carga(persona)
            
            inscripcion = manejaInscripcion.crear(persona, taller, fecha)
            manejaTaller.cargaPersona(num_taller, inscripcion)
        elif op == 2:
            dni = int(input("Ingrese dni de persona a buscar: "))
            inscripcion = manejaInscripcion.buscaDNI(dni)
            
            if inscripcion != -1:
                print(inscripcion)
            else:
                print("No se encontro la persona solicitada ")
                
        elif op == 3:
            num_taller = int(input("Ingrese identificador de taller: "))
            manejaTaller.muestraPersonas(num_taller)
        elif op == 4:
            dni = int(input("Ingrese dni de persona a realizar pago: "))
            indice = manejaInscripcion.buscaPago(dni)
            
            if indice != -1:
                manejaInscripcion.realizarPago(indice)
            else:
                print("No se encontro la persona ")
        elif op == 5:
            manejaInscripcion.guardar()
        else:
            print("Ingreso opcion no valida ")
            
        menu.Muestra()
        op = int(input("Ingrese opcion: "))
    

    
   