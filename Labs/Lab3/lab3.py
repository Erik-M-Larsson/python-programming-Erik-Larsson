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
        self.test_reelt(val)
        self._x = val


    @property
    def y(self) -> float:
        return self._y
        
    @y.setter
    def y(self,val):
        self.test_reelt(val)
        self._y = val

    @staticmethod
    def test_reelt(val: any) -> None:
        if not isinstance(val, (float, int)):
            raise(TypeError("Angivet värde är inte ett reellt tal")) # TODO hitta på bättre meddelande

    def flööö(self,x, y, relativ = False) -> None:          # TODO Hitta något tråkigt seriöst namn         
        """Flööar på mittpunkten till ny angiven punkt.
        Med relativ = True flyttas mittpunkten x enheter i x-led och y enheter i y-led"""
        if relativ:
            #self.test_reelt(x)
            #self.test_reelt(y)
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
        pass


class Rektangel(Geometrisk_form):
    pass

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
        self.test_reelt(val)
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