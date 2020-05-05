"""
Trabajo Karatsuba
Autores:
Braslyn Rodriguez Ramirez (08:00 am)  ID:
Andres Zuñiga Calderon(10:00am) ID:402430799
group:04-08am
"""

from Num import*
from Knum import *
import timeit

if __name__=="__main__":
    """
    Pequeño main donde se muestran los resultados de Num y Knum
    """
    print("Sistema implementado por los Estudiantes")
    print("Andres Zuñiga Calderon(10am) y Braslyn Rodriguez(08am)")
    print("Grupo 04-08")
    print("************************Clase Num*************************")
    Num1=Num(70000,10)
    Num2=Num(10000,10)
    print(f"Num({Num1.show_number()}) + Num({Num2.show_number()}) = {Num1+Num2}")
    print(f"Num({Num1.show_number()}) + ~ Num({Num2.show_number()}) = {Num1 + ~Num2}")
    print(f"Num({Num1.show_number()}) * Num({Num2.show_number()}) = {Num1 * Num2}")
    print(f"Num({Num1.show_number()}) // Num({Num2.show_number()}) = {Num1 // Num2}")
    print(f"Num({Num1.show_number()}) % Num({Num2.show_number()}) = {Num1 % Num2}")
    print(f"~Num({Num1.show_number()}) = {~Num1}")
    Num1=Num(70,10)
    Num2=Num(10,10)
    print(f"Num({Num1.show_number()}) ** Num({Num2.show_number()}) = {Num1 ** Num2}")
    print()
    print("************************Clase Knum*************************")
    Num1=Knum(70000,10)
    Num2=Knum(10020,10)
    print(f"Knum({Num1.show_number()}) + Knum({Num2.show_number()}) = {Num1+Num2}")
    print(f"Knum({Num1.show_number()}) + ~ Knum({Num2.show_number()}) = {Num1 + ~Num2}")
    print(f"Knum({Num1.show_number()}) * Knum({Num2.show_number()}) = {Num1 * Num2}")
    print(f"Knum({Num1.show_number()}) // Knum({Num2.show_number()}) = {Num1 // Num2}")
    print(f"Knum({Num1.show_number()}) % Knum({Num2.show_number()}) = {Num1 % Num2}")
    print(f"~Knum({Num2.show_number()}) = {~Num2}")
    Num1=Knum(70,10)
    Num2=Knum(10,10)
    print(f"Knum({Num1.show_number()}) ** Knum({Num2.show_number()}) = {Num1 ** Num2}")