"""
Trabajo Karatsuba
Autores:
Braslyn Rodriguez Ramirez (08:00 am)  ID:402420750
Andres Zuñiga Calderon(10:00am) ID:402430799
"""

from Num import *
from Knum import *
import timeit

def tocoma(n):
    """
    Esta funcion remplaza un punto por una coma
    """
    return str(n).replace(".",",")

if __name__ == "__main__":
   
    with open("../data/Analisis_De_tiempo1.csv", "w") as file:
        file.write("n;Num;Knum\n")      
        for i in range(600):
            print("nueva interaccion")
            time_Num = timeit.timeit("Num(70000) * Num(10000)", globals=globals(), number=1)
            time_Knum = timeit.timeit("Knum(70000) * Knum(10000)", globals=globals(), number=1)
            file.write(f"{i};{tocoma(time_Num)};{tocoma(time_Knum)}\n")
    print("Listo!")   
    
    
    