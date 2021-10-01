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
            self.test_reelt(x)
            self.test_reelt(y)
            self.flööö(self._x + x, self._y + y, relativ = False)
        else:
            self.x = x
            self.y = y
            # TODO rita ut figuren igen på nya platsen. När den metoden finns.

    def rita_ut(self) -> None:
        fig, ax = plt.figure(),plt.axes() 

        ax.plot(self.x, self.y, ["b+"])
        # TODO plot randen på formen

        ax.set(titlle="Nått smart", xlabel="x", ylabel="y")
        plt.show()



class Rektangel(Geometrisk_form):
    pass

class Cirkel(Geometrisk_form):
    pass

class Kub:
    pass

class Sfar:
    pass