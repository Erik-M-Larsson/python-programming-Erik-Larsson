from matplotlib import axes
import matplotlib.pyplot as plt
import numpy as np
from math import tau, sqrt


# Det här behövs ju inte ååååååå
class XYplan: # TODO snyggt plan för flera geometriska filurer
    pass
 


class Geometrisk_form:
    """Klass för geometriska former"""

    def __init__(self, x: float, y: float, z: float = None) -> None: # https://www.educative.io/edpresso/what-is-the-none-keyword-in-python
        self.x = x # TODO Tillkalla flööö istället?
        self.y = y
        if z != None: # TODO behövs den här ifsatsen? z= 0 istället?
            self.z = z
            #print("yoo")
        #else:
            #print("tjoho")
    
        #self.rita_ut()


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
        self._test_reelt(val)
        self._z = val

    @staticmethod
    def _test_reelt(val: any) -> None:
        if not isinstance(val, (float, int)):
            raise(TypeError("Angivet värde är inte ett reellt tal")) # TODO hitta på bättre meddelande

    @staticmethod
    def _avstand_mitt(max_distans:  float, x1: float=0, y1:  float=0, z1: float=0, x2: float=0, y2: float=0, z2: float=0 ) -> bool: # TODO namnge metoden
        """Kontrollerar euklidiskt avstånd mellan två punkter och jämför om det är <= max_distans"""
        
        # Kontroll datatyp 
        tester = (max_distans, x1, y1, z1, x2, y2, z2)
        for t in tester:
            Geometrisk_form._test_reelt(t)

        # Beräkna avstånd och jämför med angivet maxvärde
        return round(sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2), 10) <= round(max_distans, 10) # Risk för avrundningsfel med flyttal. Möjligen roblematiskt vid randen. Den punkt jag tittade på flev felet åt rätt håll.
        #https://docs.python.org/3/tutorial/floatingpoint.html

    def omkrets(self) -> float:
        """Beräknar omkretsen på ett cirkulärt objekt"""
        print("\U0001F49A", '\u03C4')
        return tau * self.r     

    def flööö(self,x: float, y: float, z: float = 0, relativ: bool = False) -> None:          # TODO Hitta något tråkigt seriöst namn         
        """Flööar på mittpunkten till ny angiven punkt.
        Med relativ = True flyttas mittpunkten x enheter i x-led och y enheter i y-led"""
        if relativ:
            #self._test_reelt(x)
            #self._test_reelt(y)
            self.x += x 
            self.y += y
            self.z += z # TODO hantera om z= None
        else:
            self.x = x
            self.y = y
            self.z = z
        
        self.rita_ut()

    def rita_ut(self) -> None:
        fig, ax = plt.figure(),plt.axes() 

        ax.plot(self.x, self.y, "ro")
        ax.plot(self.x + self._xx, self.y + self._yy, "r-")

        ax.set(title="Nått smart", xlabel="x", ylabel="y", aspect='equal')
        plt.show()

    def __repr__(self) -> str: # TODO skriv nått i denna
        return "hej"




class Rektangel(Geometrisk_form):
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
        # TODO koll negativ
        self._a = val

    @property
    def b(self) -> float:
        return self._b

    @b.setter
    def b(self, val: float) -> None:
        self._test_reelt(val) 
        # TODO koll negativ
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

    def rita_ut(self) -> None:
        xa = np.linspace(-self.a/2, self.a/2) 
        ya = np.linspace(-self.b/2, -self.b/2)
        xb = np.linspace(self.a/2, self.a/2)
        yb = np.linspace(-self.b/2, self.b/2)
        xc = np.linspace(self.a/2, -self.a/2)
        yc = np.linspace(self.b/2, self.b/2)
        xd = np.linspace(-self.a/2, -self.a/2)
        yd = np.linspace(self.b/2, -self.b/2)
        self._xx = np.concatenate((xa, xb, xc, xd))    # TODO Hitta bättre variabelnamn än  xx
        self._yy = np.concatenate((ya, yb, yc, yd))
      
        return super().rita_ut()

    def __repr__(self) -> str: 
        return f"Rektanngel( x = {self.x}, y = {self.y}, a = {self.a}, b = {self.b})"




class Cirkel(Geometrisk_form):
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
        # TODO koll negativ
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

    def rita_ut(self) -> None:

        self._xx = self.r * np.cos(np.linspace(0, tau)) # TODO Hitta bättre variabelnamn än  xx
        self._yy = self.r * np.sin(np.linspace(0, tau)) 

        return super().rita_ut()
        
    def __repr__(self) -> str:
        return f"Cirkel( x = {self.x}, y = {self.y}, r = {self.r})"




class Kub(Geometrisk_form):
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
        # TODO koll negativ
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

    
    def rita_ut(self) -> None:
        pass
        #return super().rita_ut()

    def __repr__(self) -> str:
        return f"Kub(x = {self.x}, y = {self.y}, z = {self.z}, a = {self.a}"




class Sfar(Geometrisk_form):
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
        # TODO koll negativ
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
    
    def rita_ut(self) -> None:
        pass
        #return super().rita_ut()

    def __repr__(self) -> str:
        return f"Sfar(x = {self.x}, y = {self.y}, z = {self.z}, r = {self.r})"

