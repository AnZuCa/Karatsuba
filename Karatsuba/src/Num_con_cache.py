"""
Trabajo Karatsuba
Autores:
Braslyn Rodriguez Ramirez (08:00 am)  ID:402420750
Andres Zuñiga Calderon(10:00am) ID:402430799
group:04-08am
"""
from CheckNum import *
import copy
from functools import lru_cache #Aqui se importa el cache

class NumC:
    base=10
    size=16
    cadena="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def __init__(self,numero,Base = 10,complemento = False):
        """
        convierte los numeros del compilador a numeros propios de la clase verifica que esten en la base 
        y que el tamaño no exceda 16
        """
        
        if CheckNum.Check(numero,Base) and CheckNum.Size(numero):
            self.cache = dict()
            self.Complemento = complemento
            self.base=Base
            if type(numero) == list:  
                self.ListaN = copy.copy(numero)
                self.ListaN =  [0]* (self.size - len(self.ListaN)) + self.ListaN
                
            else:
                self.ListaN = CheckNum.ConvertListtoint(str(numero))
                self.ListaN =  [0] * (self.size - len(self.ListaN)) + self.ListaN
                
              
    def __invert__(self):
        """
        Funcion que crea el complemento
        """
        listaInv = []
        for i in range(self.size):
            listaInv.append(self.base-1 - self[i])
        if self.Complemento == True:
            return NumC(listaInv,self.base,False) + NumC(1,self.base,False)
        return NumC(listaInv,self.base,True) + NumC(1,self.base,False)
        
    def Negativos(self):
        """
        Funcion encargada de mostrar un negativo al usuario
        """
        aux = copy.copy(~self)
        if self.base < 11: return int("-" + str(aux.int()))
        else: return "-" + self.base_mayor_10()
            
            
    def show_number(self):
        """
        Funcion encargada de mostrar los numeros al usuario
        """
        if self.Complemento:
           return self.Negativos()
        else:
            if self.base < 11:
                return self.int()
            else:
                return self.base_mayor_10()
    
    def base_mayor_10(self):
        """
        Funcion encargada de transformar un numero en base mayor a 10 con sus respectivas letras dependiendo de la base
        """
        if self.Complemento: self_copy = copy.copy(~self)
        else: self_copy = copy.copy(self)
        numero = ""
        contador = 0
        while self_copy[contador] == 0 and contador<15:
            contador+=1
        new = []
        new = self_copy.ListaN[contador:16]
        for i in new:
            numero += self.cadena[i] 
        return numero    
            
    def __eq__(self,other):
        """Sobrecarga de == que verifica si dos Num son iguales"""
        return self.int() == other.int()
    def __ne__(self,other):
        """
        sobrecarga del operador != devuelve un true si self y other son diferentes
        de lo contrario devuelve false
        """
        return str(self.show_number()) != str(other.show_number())
     
    def int(self):
        """
        Muestra la lista como numeros del compilador
        """
        if self.base > 10:
            return self.base_mayor_10()
        aux=0
        inc=1
        for i in range(len(self.ListaN)):
            aux+=self.ListaN[-(i+1)]*inc
            inc*=10
        return aux

    def __getitem__(self,index):
        """
        Muetra los numeros dentro de la lista (eje invertido "Provicional")
        """
        return self.ListaN[index]


    def __len__(self):
        """
        Retorna el tamaño del digito que esta en la lista, si es negativo devuelve 16
        """
        if self.Complemento:return self.size
        return(len(str(self.int())))
    def __le__(self,other):
        """
        Sobrecarga del operador <= me indica si other es mayor o igual que self
        """
        if self.Complemento==False and other.Complemento==True:return True
        elif self.Complemento==True and other.Complemento==False:return False
        elif self.int() <= other.int(): return True    
        return False
        
    def __gt__(self,other):
        """
        Esta sobrecarga > sirve para mostrar 
        """
        if self.Complemento==False and other.Complemento==True: return True
        elif self.Complemento==True and other.Complemento==False:return False
        elif self.int() > other.int():return True    
        return False 

    def __repr__(self):
        """
        aprovecha la funcion int para mostrar los valores por string
        """
        return f"(Valor: {self.show_number()}) (Base:{self.base}) (Max:10 **{self.size})  \n"#{self.ListaN}
        
    def __lshift__(self,positions):
        """
        Mueve todos los digitos a la izquierda <<
        """
        if not isinstance(positions,int): raise Exception("positions no es un int") 
        if positions < 0: raise Exception(f"El entero {positions} no es positivo") 
        aux = copy.copy(self)
        list = []
        list =  aux.ListaN + [0] * positions
        aux.ListaN=list[len(list)-self.size:len(list)]
        return aux
    def __rshift__(self,positions):
        """
        Mueve todos los digitos a la derecha >>
        """
        if not isinstance(positions,int): raise Exception("positions no es un int") 
        if positions < 0: raise Exception(f"El entero {positions} no es positivo") 
        aux = copy.copy(self)
        list=[]
        list = [0]* positions + aux.ListaN 
        aux.ListaN = list[0:self.size]
        return aux 
        
    def __eq__(self, other):
        return self.int() == other.int()
        
    def Verificaciones(self,other):
        if not isinstance(other,NumC): raise Exception(f"other no es tipo Num") 
        if not self.base == other.base: raise Exception(f"La base self {self.base} != La base other {other.base}")
        return True
      
    def __add__(self,other):
        """
        suma de dos numeros de la propia clase  Numero, esta toma caracter(int) por caracter(int) de atras hacia delante
        y los suma, tambien se acarrea si es necesario
        """
        self.Verificaciones(other)
        def suma():
           
            Residuo=0#lleva los decimales centenas ... que superen la capacidad de la respectiva unidad
            suma=0
            new=[] 
            for i in range(15,self.size-max(len(other),len(self))-1,-1):
                suma = self[i] + other[i]
                suma += Residuo
                if suma >= self.base:
                    if i == self.size-max(len(other),len(self)):
                        new.append(suma-self.base)
                        new.append(suma//self.base)
                    else:
                        new.append(suma-self.base)
                        Residuo = suma//self.base
                else:
                    new.append(suma)
                    Residuo = 0
            new = new[::-1]
            if self.Complemento == True or other.Complemento == True: #Aqui verifico si alguno de los numeros es negativo
                if new[1] == self.base-1: return NumC(new[len(new)-self.size:len(new)],self.base,True)# si el resultado es negativo
                else: return NumC(new[len(new)-self.size:len(new)],self.base)
            return NumC(new,self.base)
        return self.F_cache(suma,other.int(),"+")
    def __mul__ (self,other):
        """
        Funcion encargada de multiplicar de la forma ,suma de self una cantidad de veces other despues los voy
        acumulando para el resultado final
        """
        valor=other.show_number()
        def mult():
            self.Verificaciones(other)
            resultado = NumC(0,self.base)#Este Num guarda la suma de cada multiplicacion que se hace
            resultado_final = NumC(0,self.base)
            self_copy = copy.copy(self)
            aux=copy.copy(other)
            if other.Complemento: aux = copy.copy(~other) #estos dos if verifican si alguno de los numeros es negativo
            if self.Complemento: self_copy = ~self_copy   #y si encuentra uno lo pasa a positivo
            contador = 0
            Valor = str(aux.int())
            Valor = Valor[::-1]
            for i in Valor:         #De aqui obtengo la cantidad de veces que será sumado self_copy 
                aux = NumC(i,self.base) 
                while aux > NumC(0,self.base):
                    aux -= NumC(1,self.base)
                    resultado += self_copy  
                resultado = resultado << contador             
                resultado_final += resultado
                resultado = NumC(0,self.base)
                contador+=1
            if (other.Complemento and self.Complemento==False) or (other.Complemento==False and self.Complemento):
                return ~resultado_final 
            else:
                return resultado_final    
        return self.F_cache(mult,valor,"*")
    
    def __floordiv__(self,other):
        """
        Esta funcion es para la division, Se usa un contador para ver cuantas veces se tiene que sumar other 
        para que sea menor si no se puede llegar a ser igual que self,o igual si se puede operador // 
        """  
        valor=other.show_number()
        def div():    
            self.Verificaciones(other)
            self_copy = copy.copy(self)
            aux = copy.copy(other)
            other_copy = copy.copy(other)
            contador=NumC(0,self.base)
            if other.Complemento:
                aux = copy.copy(~other)
                other_copy = copy.copy(~other)
            if self.Complemento:
                self_copy = copy.copy(~self_copy)
            while aux <= self_copy:
                if aux <= self_copy:
                    contador += NumC(1,self.base)
                aux += other_copy
            if (other.Complemento and self.Complemento==False) or (other.Complemento==False and self.Complemento):
                return ~contador 
            else:
                return contador
        return self.F_cache(div,valor,"//")
            
    def __mod__(self,other):
        """
        Sobrecarga del operador % retorna el mod de self / other 
        """
        self.Verificaciones(other)
        return self-(self//other)*other
        
        
    def __pow__(self,other):
        """
        Sobrecarga del operador ** aqui se multiplica self cantidad de veces other
        """
        valor = other.show_number()
        def pow():
            self.Verificaciones(other)
            self_copy = copy.copy(self)
            aux = copy.copy(other)
            other_copy = copy.copy(other)
            resultado=NumC(1,self.base)
            if other.Complemento: raise("La sobrecarga division x**n no sirve con n negativos")
            while aux > NumC(0,self.base):
                resultado = resultado * self_copy
                aux -= NumC(1,other.base)
            return resultado
        return self.F_cache(pow,valor,"**")

    def __sub__(self,other):
        """
        Algoritmo consiste en la implementacion de la resta clasica
        """
        valor = other.show_number()
        def sub():
            self.Verificaciones(other)
            return self + ~other
        return self.F_cache(sub,valor,"~")
        
    def F_cache(self,func,other,operador):
        """
        Funcion de controlar, aqui se establece el cache para cada objeto
        """
        find=f"{other}{operador}"
        if find in self.cache:
            return self.cache[find]
        else:
            self.cache[find]=func()
            return self.cache[find]