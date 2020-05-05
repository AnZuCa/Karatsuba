"""
Trabajo Karatsuba
Autores:
Braslyn Rodriguez Ramirez (08:00 am)  ID:402420750
Andres Zuñiga Calderon(10:00am) ID:402430799
group:04-08am
"""
class CheckNum:
    @staticmethod
    def Check(num,base):
        """verifica si un entero o string o lista esta en la base correspondiente"""
        cadena="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        try: 
            if type(num)==int:
                aux = str(num)
            else:
                aux = num
            for i in range(len(aux)):
                if str(aux[i]).isdigit():
                    int(str(cadena[int(aux[i])]),base)    
                else:
                    int(aux[i],base) 
        except ValueError:
            raise Exception(f"El numero {num} no esta en la base {base}")
        return True  
    @staticmethod
    def ConvertListtoint(num):
        """Convierte una lista a digitos tipo int adentro"""
        newlist=[]
        for i in range(len(num)):
            newlist.append(int(str(num[i]),16))
        return newlist
    def Size(num):
        """Verifica si una lista o un numero son de tamaño menor que 16"""
        if type(num)==list:
            if len(num)>16: raise Exception(f"El numero {num} excede el tama?o maximo que es 16")
        else:
            if len(str(num))>16: raise Exception(f"El numero {num} excede el tama?o maximo que es 16")
        return True        
            