
from Num import *
#Autores:
#Andres Zuniga Calderon(10am)
#Braslyn Rodriguez (8am)
#grupo:04-10am



class Knum(Num):
           
    def __mul__(self,other):           
        """Funcion de karatsuba es mas eficiente que una multiplicacion de escuela
        Multiplica dos Knum con el algoritmo de karatsuba
        
        self  =   [2,5]       other  =  [5,0]    n = max entre self y other , nby2 = n//2 si es impar se suma 1
        
        despues se dividen self a la mitad y other tmabien en a,b para self y c,d para other
        a[2] , b[5], c[5], d=[0]
        
        ac = a * c = [2] * [5]
                   = [1,0]

        bd = b * d = [5] * [0]            
                   = [0] 
        
        k =  ( a + b) * (c + d) - ac - bd = ([2]+[5]) * ([5]+[0]) - [1,0] - [0] = [2,5]
        
        
        return (ac << ((n-nby2)*2)) + (k << (n-nby2)) + bd = [1,0,0,0] + [2,5,0] + [0] = [1,2,5,0] 
                    
        
        """
        self.Verificaciones(other)
        if len(self) == 1 or len(other) == 1:
            numero = copy.copy(super().__mul__(other))
            return Knum(numero.ListaN,numero.base,numero.Complemento)
        else:
            #si se desea que el programa funcione con negativos se deben implementar las siguientes instrucciones 
            if self.Complemento and other.Complemento:
                return ~self * ~other
            elif self.Complemento:
                return ~(~self * other)
            elif other.Complemento:
                return ~(self * ~ other)
            n = max(len(self),len(other))
            nby2 = n // 2
            if n % 2 != 0:
               nby2 += 1
            self_copy = copy.copy(self.ListaN[self.size-n:])
            other_copy= copy.copy(other.ListaN[self.size-n:])
            a = type(self)(self_copy[:nby2],self.base,self.Complemento)
            b = type(self)(self_copy[nby2:],self.base,self.Complemento)
            c = type(other)(other_copy[:nby2],other.base,other.Complemento)
            d = type(other)(other_copy[nby2:],other.base,other.Complemento)
            ac = a * c
            bd = b * d
            k = (a + b) * (c + d) - ac - bd
            return (ac << ((n-nby2)*2)) + (k << (n-nby2)) + bd

    
    
    def __invert__(self):
        return super().__invert__()


    def __getitem__(self,index):
        return super().__getitem__(index) 


    def __len__(self):
        return super().__len__()

    def __le__(self,other):
        return super().__le__(other)

        
    def __gt__(self,other):
        return super().__gt__(other)


    def __repr__(self):
        return super().__repr__()

       
    def __lshift__(self,positions):
        numero = copy.copy(super().__lshift__(positions))
        return Knum(numero.ListaN,numero.base,numero.Complemento)

    def __rshift__(self,positions):
        numero = copy.copy(super().__rshift__(positions))
        return Knum(numero.ListaN,numero.base,numero.Complemento)
        
    def __eq__(self, other):
        return super().__eq__(other)
        Knum(numero.ListaN,numero.base,numero.Complemento)
  
      
    def __add__(self,other):
        numero = copy.copy(super().__add__(other))
        return Knum(numero.ListaN,numero.base,numero.Complemento)
   
 
    def __floordiv__(self,other):
        numero = copy.copy(super().__floordiv__(other))
        return Knum(numero.ListaN,numero.base,numero.Complemento)
   
            
    def __mod__(self,other):
        numero = copy.copy(super().__mod__(other))
        return Knum(numero.ListaN,numero.base,numero.Complemento)    
            
    def __pow__(self,other):
        numero = copy.copy(super().__pow__(other))
        return Knum(numero.ListaN,numero.base,numero.Complemento)

    def __sub__(self,other):
        numero = copy.copy(super().__sub__(other))
        return Knum(numero.ListaN,numero.base,numero.Complemento)