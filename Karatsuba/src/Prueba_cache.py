"""
Trabajo Karatsuba
Autores:
Braslyn Rodriguez Ramirez (08:00 am)  ID:402420750
Andres Zuñiga Calderon(10:00am) ID:402430799
group:04-08am
"""

from Num import *
from Num_con_cache import *
import timeit

def tocoma(n):
    """
    Esta funcion remplaza un punto por una coma
    """
    return str(n).replace(".",",")

if __name__ == "__main__":
    """
    Aqui se prueba el cache para ver si llega a ser mas eficiente que la suma de la clase Num
    """
    Num1 = Num(700) 
    Num2 = Num(1000)
    Num3 = NumC(700)
    Num4 = NumC(1000)
    with open("../data/Analisis_De_cache.csv", "w") as file:
        file.write("n;Num;NumC\n")      
        for i in range(10):
            print("nueva interaccion")
            time_Num = timeit.timeit("Num1 + Num2", globals=globals(), number=10)
            time_NumC = timeit.timeit("Num3 + Num4", globals=globals(), number=10)
            file.write(f"{i};{tocoma(time_Num)};{tocoma(time_NumC)}\n")
    print("Listo!")   