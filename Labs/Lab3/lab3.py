from matplotlib import axes
import matplotlib.pyplot as plt
import numpy as np
from math import tau


class XYplan:
    pass

class Geometrisk_form:
    """Klass för geometriska former"""

    def __init__(self, x: float, y: float) -> None:
        self.x = x # TODO Tillkalla flööö istället?
        self.y = y
        self.rita_ut()


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

    @staticmethod
    def _test_reelt(val: any) -> None:
        if not isinstance(val, (float, int)):
            raise(TypeError("Angivet värde är inte ett reellt tal")) # TODO hitta på bättre meddelande

    def flööö(self,x, y, relativ = False) -> None:          # TODO Hitta något tråkigt seriöst namn         
        """Flööar på mittpunkten till ny angiven punkt.
        Med relativ = True flyttas mittpunkten x enheter i x-led och y enheter i y-led"""
        if relativ:
            #self._test_reelt(x)
            #self._test_reelt(y)
            self.x += x 
            self.y += y
        else:
            self.x = x
            self.y = y
        
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
        self._a = val

    @property
    def b(self) -> float:
        return self._b

    @b.setter
    def b(self, val: float) -> None:
        self._test_reelt(val) 
        self._b = val

    def omkrets(self) -> float:
        return (self.a + self.b) * 2

    def area(self) -> float:
        return (self.a * self.b)

    def inne_i(self, x: float, y: float) -> bool:
        self._test_reelt(x)
        self._test_reelt(y)
        
        return abs(self.x - x) <= self.a/2 and abs(self.y - y) <= self.b/2

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
        self._r = val

    def omkrets(self) -> float:
        print("\U0001F49A", '\u03C4')
        return tau * self.r     
    
    def area(self) -> float:
        return tau * self.r**2 /2       

    def inne_i(self, x: float, y: float) -> bool:
        avstånd_mitt = np.sqrt((self.x - x)**2 + (self.y - y)**2)
        return avstånd_mitt <= self.r

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


class Kub:
    pass

class Sfar:
    pass