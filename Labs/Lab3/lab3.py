#import numpy as np
from math import tau, sqrt


# TODO Kommentarer
# TODO Kolla Docstrings
# TODO Kolla type hint
 
class GeometriskForm:
    """Klass för geometriska former"""

    def __init__(self, x: float, y: float, z: float = None) -> None: # https://www.educative.io/edpresso/what-is-the-none-keyword-in-python
        self.x = x
        self.y = y
        self.z = z


    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self,val):
        self._test_reelt(val)
        self._x = val

    @property
    def y(self) -> float:
        return self._y
        
    @y.setter
    def y(self,val):
        self._test_reelt(val)
        self._y = val

    @property
    def z(self) -> float:
        return self._z

    @z.setter
    def z(self, val: float) -> None:
        if val != None:
            self._test_reelt(val)
        self._z = val

    @staticmethod
    def _test_reelt(val: any) -> None:
        if not isinstance(val, (float, int)):
            raise TypeError(f"Angivet värde är inte ett reellt tal: {val}")

    @staticmethod
    def _test_inte_negativt(val: float) -> None:
        if val < 0:
            raise ValueError(f"Angivet värde kan inte var negativt: {val}")        

    @staticmethod
    def _avstand_mitt(max_avstand:  float, x1: float=0, y1:  float=0, z1: float=0, x2: float=0, y2: float=0, z2: float=0 ) -> bool: # TODO namnge metoden
        """Kontrollerar euklidiskt avstånd från en punkt till mittpunkten och jämför om det är <= största tillåtna avståndet"""
        
        # Kontroll datatyp 
        tester = (max_avstand, x1, y1, z1, x2, y2, z1, z2)
        for t in tester:
            GeometriskForm._test_reelt(t)

        # Kontroll max_avstand ej negativt
        GeometriskForm._test_inte_negativt(max_avstand) 

        # Beräkna avstånd och jämför med angivet maxvärde
        return round(sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2), 10) <= round(max_avstand, 10) # Risk för avrundningsfel med flyttal. Möjligen roblematiskt vid randen. Den punkt jag tittade på flev felet åt rätt håll.
        #https://docs.python.org/3/tutorial/floatingpoint.html

    def omkrets(self) -> float:             # TODO den är inte generell? Flytta
        """Beräknar omkretsen på ett cirkulärt objekt"""
        print("\U0001F49A", '\u03C4')
        return tau * self.r     

    def flööö(self,x: float, y: float, z: float = None, relativ: bool = False) -> None:          # TODO Hitta något tråkigt seriöst namn         
        """Flööar på mittpunkten till ny angiven punkt.
        Med relativ = True flyttas mittpunkten x enheter i x-led och y enheter i y-led"""
        if (self.z == None) != (z == None): # Varför finns inte xor?
            raise TypeError("Antalet dimensioner matchar inte objektets dimensioner")       
        
        if relativ:
            self._test_reelt(x)
            self._test_reelt(y)
            self.x += x 
            self.y += y
            if z != None:              
                self._test_reelt(z)
                self.z += z 
        else:
            self.x = x
            self.y = y
            self.z = z

    
    def __repr__(self) -> str: 
        return f"GeometriskForm( x = {self.x}, y = {self.y}, z = {self.z} )"





class Rektangel(GeometriskForm):
    """Klass för rektanglar"""

    def __init__(self, x: float, y: float, a: float, b: float) -> None:
        self.a = a
        self.b = b
        super().__init__(x, y)

    @property
    def a(self) -> float:
        return self._a
        
    @a.setter
    def a(self, val: float) -> None:
        self._test_reelt(val)
        self._test_inte_negativt(val)
        self._a = val

    @property
    def b(self) -> float:
        return self._b

    @b.setter
    def b(self, val: float) -> None:
        self._test_reelt(val) 
        self._test_inte_negativt(val)
        self._b = val

    def omkrets(self) -> float:
        return (self.a + self.b) * 2

    def area(self) -> float:
        return (self.a * self.b)

    def inne_i(self, x: float, y: float) -> bool:

        return self._avstand_mitt(self.a/2, x1=self.x, x2=x) and self._avstand_mitt(self.b/2, y1=self.y, y2=y)

    def __eq__(self, other: "Rektangel") -> bool: 
        if not isinstance(other, Rektangel):
            raise TypeError("Måste vara av klassen Rektangel") 
        return (self.a == other.a and self.b == other.b) or (self.a == other.b and self.b == other.a)

    def __repr__(self) -> str: 
        return f"Rektangel( x = {self.x}, y = {self.y}, a = {self.a}, b = {self.b} )"




class Cirkel(GeometriskForm):
    "Klass för cirklar"

    def __init__(self, x: float, y: float, r :float) -> None:
        self.r = r        
        super().__init__(x, y)
        
    @property
    def r(self) -> float:
        return self._r

    @r.setter
    def r(self, val: float) -> None:
        self._test_reelt(val)
        self._test_inte_negativt(val)
        self._r = val

    def omkrets(self) -> float:
        print("\U0001F49A", '\u03C4')
        return tau * self.r     
    
    def area(self) -> float:
        return tau * self.r**2 /2       

    def inne_i(self, x: float, y: float) -> bool:

        return self._avstand_mitt(self.r, x1=self.x, y1=self.y, x2=x, y2=y)
        #avstånd_mitt = np.sqrt((self.x - x)**2 + (self.y - y)**2)
        #return avstånd_mitt <= self.r

    def __eq__(self, other: "Cirkel") -> bool:
        if not isinstance(other, Cirkel):
            raise TypeError("Måste vara av klassen Cirkel") 
        return self.r == other.r

    def __repr__(self) -> str:
        return f"Cirkel( x = {self.x}, y = {self.y}, r = {self.r} )"




class Kub(GeometriskForm):
    """Klass för kuber"""

    def __init__(self, x: float, y: float, z: float, a: float) -> None:
        self.a = a
        super().__init__(x, y, z)


    @property
    def a(self) -> float:
        return self._a

    @a.setter
    def a(self, val: float) -> None:   
        self._test_reelt(val)
        self._test_inte_negativt(val)
        self._a = val


    def omkrets(self) -> float:
        """Beräknar summan av längden på kanterna"""
        return 12 * self.a 
        

    def area(self) -> float:
        """Beräknar begränsningsarean"""
        return 6 * self.a**2


    def volym(self) -> float:
        """Beräknar volymen"""
        return self.a**3    


    def inne_i(self, x: float, y: float, z: float) -> bool:

        return (self._avstand_mitt(self.a/2, x1=self.x, x2=x) and
                self._avstand_mitt(self.a/2, y1=self.y, y2=y) and
                self._avstand_mitt(self.a/2, z1=self.z, z2=z) )
    

    def __eq__(self, other: "Kub") -> bool:
        if not isinstance(other, Kub):
            raise TypeError("Måste vara av klassen Kub") 
        return self.a == other.a


    def __repr__(self) -> str:
        return f"Kub( x = {self.x}, y = {self.y}, z = {self.z}, a = {self.a} )"




class Sfar(GeometriskForm):
    """Klass för sfärer"""
    
    def __init__(self, x: float, y: float, z: float, r: float) -> None:
        self.r = r
        super().__init__(x, y, z)


    @property
    def r(self) -> float:
        return self._r


    @r.setter
    def r(self, val: float) -> float:
        self._test_reelt(val)
        self._test_inte_negativt(val)
        self._r = val


    #def omkrets(self) -> float: # Använd super().omkrets
    #    print("\U0001F49A", '\u03C4')
    #    return tau * self.r     

    def area(self) -> float:
        """Beräknar mantelarean"""
        return 2 * tau * self.r**2


    def volym(self) -> float:
        """Beräknar volymen"""
        return 2/3 * tau * self.r**3


    def inne_i(self, x: float, y: float, z: float) -> bool:

        return self._avstand_mitt(self.r, self.x, self.y, self.z, x, y, z)


    def __eq__(self, other: "Sfar") -> bool:
        if not isinstance(other, Sfar):
            raise TypeError("Måste vara av klassen Sfar") 
        return self.r == other.r


    def __repr__(self) -> str:
        return f"Sfar( x = {self.x}, y = {self.y}, z = {self.z}, r = {self.r} )"

