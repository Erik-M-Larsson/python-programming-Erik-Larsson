from typing import Union

class Fraction:
    """Klass för bråktal"""

    def __init__(self, taljare: int, namnare: int) -> None:
        self.taljare = taljare
        self.namnare = namnare
    
    @property
    def taljare(self) -> int:
        """Returnerar värdet för taljare"""
        return self._taljare 

    @taljare.setter
    def taljare(self, t: int) -> None:
        """Tilldelar värdet för taljare"""

        if not isinstance (t, int):
            raise TypeError("Måste vara ett heltal") 
            
        self._taljare = t
    

    @property
    def namnare(self) -> int:
        """Returnerar värdet för nämnaren"""
        return self._namnare

    @namnare.setter
    def namnare(self, n: int) -> None:
        """Tilldelar värdet för nämnaren"""

        if not isinstance(n, int):
            raise TypeError("Måste vara ett heltal")
        if n == 0:
            raise ValueError("Nämnaren kan inte vara noll (0)")
        
        self._namnare = n


    def __str__(self) -> str:

        if (self.namnare < 0) != (self.taljare <0):
            string = "-"
        else:
            string = ""

        if self.namnare != 1:
            string += f"{abs(self.taljare)}/{abs(self.namnare)}"
        else:
            string += f"{abs(self.taljare)}"
        
        return string

    def __add__(self, other: Union["Fraction", int]) -> "Fraction":
        if isinstance(other, int):
            other = Fraction(other, 1)
       
        taljare = self.taljare * other.namnare + other.taljare * self.namnare
        namnare = self.namnare * other.namnare

        return Fraction(taljare, namnare).simplify()

    def __radd__(self, other: Union["Fraction", int]) -> "Fraction":
        return self.__add__(other)

    def __sub__(self, other: "Fraction") -> "Fraction":

        taljare = self.taljare * other.namnare - other.taljare * self.namnare
        namnare = self.namnare * other.namnare

        return Fraction(taljare, namnare)

    def __mul__(self, other: "Fraction") -> "Fraction":

        taljare = self.taljare * other.taljare
        namnare = self.namnare * other.namnare

        return Fraction(taljare, namnare).simplify()

    def __truediv__(self, other: "Fraction") -> "Fraction":

        taljare = self.taljare * other.namnare
        namnare = self.namnare * other.taljare


        return Fraction(taljare, namnare).simplify()

    def simplify(self, value: int = None) -> "Fraction":

        if value:
            return Fraction( self.taljare // value, self.namnare // value)
        else:
            
            a = self.taljare 
            b = self.namnare
            
            while b:
                a, b = b, a%b
                    
            return Fraction(self.taljare//a, self.namnare//a)

    def mixed(self) -> str:

        t = self.taljare
        n = self.namnare
        sign = t*n // abs(t*n)

        t = abs(t)
        n = abs(n)

        heltalsdel = t//n
        rest = t % n

        return f"{sign*heltalsdel} {Fraction(rest, n).simplify()}"

    def __eq__(self, other: "Fraction") -> bool:
        
        return self.simplify().taljare == other.simplify().taljare and self.simplify().namnare == other.simplify().namnare
