"""
Trabajo Karatsuba
Autores:
Braslyn Rodriguez Ramirez (08:00 am)  ID:
Andres Zuñiga Calderon(10:00am) ID:402430799
group:04-08am
Material obtenido del profesor Carlos Loria Saenz
"""
import time
import sys
from Num import *


def lectura(archivo, llave = None):#utilizo aqui el identificador para saber el tipo de operacion que voy a realizar
    """
    Funcion encargada de leer los .csv de prueba  recibe un archivo y un tipo de llave 
    para especificar la operación que quiero realizar
    """
    print("*** Reading Test Cases ***")
    cases = None
    total = 0
    failed = 0
    passed = 0
    given = Num(0)
    with open(archivo, "r") as file: #aqui leo el csv
        lines = file.read()
        cases = lines.split("\n")
    total = len(cases)
    start = time.time()
    for case in cases:
        # Skips comments
        if case.startswith("#"): 
            continue
        (case_num, xval, yval, expected) = (int(n) for n in case.split(";"))
        print(f"Processing case {case_num}")
        if llave == "+":
            expected= Num(expected)
            given = Num(xval) + Num(yval)   
        elif llave == "-":
            expected= Num(expected)
            given = Num(xval)- Num(yval)
        elif llave == "*":
            expected= Num(expected)
            given = Num(xval)* Num(yval)
        elif llave == "//":
            expected= Num(expected)
            given = Num(xval) // Num(yval)
        elif llave == "%":
            expected= Num(expected)
            given = Num(xval)% Num(yval)
        elif llave == "**":
            expected= Num(expected)
            given = Num(xval)** Num(yval)
        else:#caso si no se especifica una llave valida
            expected = Num(expected)
        
        if  given != expected:
            print(f"*** Case {case_num} failed! {given} != {expected} ***")
            failed += 1
        else:
            print(f"*** Case {case_num} passes! ***")
            passed += 1
            
    end = time.time()
    print("\n*** Test Case Result ***")
    print(f"Total cases={total}. Failed={failed} Passed={passed}")
    print(f"Duration:{(end -start):.4f}sec")

if __name__ == "__main__":
    """
    para una mayor facilidad se debe enviar tambien con los parametros la llave con la que se va a ejecutar el csv  
    """
    llave = None
    argumento = sys.argv  
    if len(argumento) == 1: #No se envio ningun parametro csv se usa por defecto test_01.csv
        archivo = "../test/test_01.csv"
    elif len(argumento) == 2: #se envio un parametro csv
        archivo = argumento[1]
    else:
        archivo = argumento[1]
        llave = argumento[2]
    lectura(archivo,llave)    
    