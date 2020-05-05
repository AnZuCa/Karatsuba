"""
Trabajo Karatsuba
Autores:
Braslyn Rodriguez Ramirez (08:00 am)  ID:402420750
Andres Zuñiga Calderon(10:00am) ID:402430799
group:04-08am
"""
from read_test_cases import *

def Prueba():
    """
    Funcion para ejecutar el read_test_cases.py con nuestros casos pruebas se le
    envian dos parametro el csv y el tipo de caso que va a ejecutar
    
    cada uno de los csv realizados para esta prueba estan hechos 
    para que siempre todos los casos esten correctos
    """
    print("-----------------Casos para Suma-------------------")
    lectura("../test/test_suma.csv","+")
    print()
    print("-----------------Casos para Resta-------------------")
    lectura("../test/test_resta.csv","-")
    print()
    print("-----------------Casos para Multiplicacion-------------------")
    lectura("../test/test_multiplicacion.csv","*")
    print()
    print("-----------------Casos para Division-------------------")
    lectura("../test/test_Division.csv","//")
    print()
    print("-----------------Casos para Mod-------------------")
    lectura("../test/test_mod.csv","%")
    print()
    print("-----------------Casos para Exponente-------------------")
    lectura("../test/test_exponente.csv","**")
    print()
    print("Pruebas Finalizadas")


if __name__ == "__main__":
    #Aqui llamos a Prueba encargado de ejecutarme cada una de las pruebas con los .CSV
    Prueba()