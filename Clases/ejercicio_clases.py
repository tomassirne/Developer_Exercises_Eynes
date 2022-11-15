"""
#TEST1
>>> test = Circulo(10)
>>> print(test)
Medidas Circulo:
        Radio = 10
        Area = 314.1592653589793
        Perimetro= 62.83185307179586

#TEST2
>>> test = Circulo(10)
>>> test.radio = -1
Traceback (most recent call last):
  ...
Exception: Radio Inválido

#TEST3
>>> test = Circulo(10)
>>> test.radio = 2
>>> print(test)
Medidas Circulo:
            Radio = 2
            Area = 12.566370614359172
            Perimetro= 12.566370614359172

#TEST4
>>> test = Circulo(10)
>>> print(test * 2)
Medidas Circulo:
            Radio = 20
            Area = 1256.6370614359173
            Perimetro= 125.66370614359172

#TEST5
>>> test = Circulo(10)
>>> print(test * -2)
Traceback (most recent call last):
  ...
Exception: Radio Inválido
"""


from math import pi 
import doctest



class Circulo:
    def __init__(self, radio : int()) -> None:
        self.radio = radio
        
    def __str__(self) -> str:
        return f"""Medidas Circulo:
            Radio = {self.radio} 
            Area = {self.area()}
            Perimetro= {self.perimetro()}"""
    
    def __setattr__(self, __name: str, __value: any) -> None:
        if __name == "radio":
            if __value <= 0 : raise Exception ("Radio Inválido")
            else: self.__dict__[__name] = __value

    def __mul__(self, n : int()) -> type:
        return Circulo(self.radio * n)

    def area(self) -> float:
            return pi * self.radio ** 2

    def perimetro(self) -> float:
            return self.radio * 2 * pi





doctest.testmod()