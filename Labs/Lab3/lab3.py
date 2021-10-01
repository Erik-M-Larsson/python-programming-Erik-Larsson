from matplotlib import axes
import matplotlib.pyplot as plt
import numpy as np
from math import tau


class Geometrisk_form:
    """Klass för geometriska former"""

    def __init__(self, x: float, y: float) -> None:
        self.x = x # TODO Tillkalla flööö istället?
        self.y = y


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
        # TODO plot randen på formen

        ax.set(title="Nått smart", xlabel="x", ylabel="y")
        plt.show()



class Rektangel(Geometrisk_form):
    pass

class Cirkel(Geometrisk_form):
    pass

class Kub:
    pass

class Sfar:
    pass