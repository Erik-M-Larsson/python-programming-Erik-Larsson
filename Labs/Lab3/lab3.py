from math import tau, sqrt

 
class GeometriskForm:
    """Klass för geometriska former"""

    # Initierar objekt av klassen GeometriskForm
    def __init__(self, x: float, y: float, z: float = None) -> None: # https://www.educative.io/edpresso/what-is-the-none-keyword-in-python
        """x, y, z koordinater för objektets mittpunkt"""
        self.x = x
        self.y = y
        self.z = z

    # Koordinater som propertys
    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self,val):
        GeometriskForm._kontroll_typ(val)     # Kontrollerar så att x är ett tal 
        self._x = val

    @property
    def y(self) -> float:
        return self._y
        
    @y.setter
    def y(self,val):
        GeometriskForm._kontroll_typ(val)     # Kontrollerar så att y är ett tal 
        self._y = val

    @property
    def z(self) -> float:
        return self._z

    @z.setter
    def z(self, val: float) -> None:
        if val != None:                 # Kontrollera om 2D eller 3D objekt"
            GeometriskForm._kontroll_typ(val)     # Kontrollerar så att x är ett tal 
        self._z = val

    # Metoder för felhantering
    @staticmethod
    def _kontroll_typ(val: any) -> None:
        """Kontrollerar att angivet värde är av typ float eller int"""
        if not isinstance(val, (float, int)):
            raise TypeError(f"Angivet värde är inte ett reellt tal: {val}")

    @staticmethod
    def _kontroll_inte_negativt(val: float) -> None:
        """Kontrollerar att talet inte är negativt"""
        GeometriskForm._kontroll_typ(val)       # Kontroll av typ
        if val < 0:
            raise ValueError(f"Angivet värde kan inte var negativt: {val}")        

    # Geometriska metoder
    @staticmethod
    def _avstand_mitt(max_avstand:  float, x1: float=0, y1:  float=0, z1: float=0, x2: float=0, y2: float=0, z2: float=0 ) -> bool: 
        """Kontrollerar euklidiskt avstånd mellan två punkter och jämför om det är <= största tillåtna avståndet"""
        
        # Kontroll datatyp 
        tester = (max_avstand, x1, y1, z1, x2, y2, z1, z2)
        for t in tester:                       
            GeometriskForm._kontroll_typ(t)     # TODO gör om metoden så den kan ta multipla värden istället

        # Kontroll max_avstand ej negativt
        GeometriskForm._kontroll_inte_negativt(max_avstand) 

        # Beräkna avstånd och jämför med angivet maxvärde
        return round(sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2), 10) <= round(max_avstand, 10) # Risk för avrundningsfel med flyttal. Möjligen roblematiskt vid randen. Den punkt jag tittade på flev felet åt rätt håll.
        #https://docs.python.org/3/tutorial/floatingpoint.html 

    # Manipulation
    def flytta(self,x: float, y: float, z: float = None, relativ: bool = False) -> None:          
        """Fllyttar mittpunkten till ny angiven punkt.
        Med relativ = True flyttas mittpunkten x enheter i x-led och y enheter i y-led"""

        if (self.z == None) != (z == None):     # Kontrollera så att antalet dimensioner på objektet och förflyttningen överenstämmer. Varför finns inte xor?
            raise TypeError("Antalet dimensioner matchar inte objektets dimensioner")       
        
        if relativ:                             # Relativ förflyttning
            GeometriskForm._kontroll_typ(x)     # Felhantering 
            GeometriskForm._kontroll_typ(y)
            self.x += x                         # Addera värde till tidigare värde
            self.y += y
            if z != None:                       # Kontrollera om 3D
                GeometriskForm._kontroll_typ(z)
                self.z += z 
        else:                                   # Absolt förflyttning
            self.x = x                          # Sätt nytt värde
            self.y = y
            self.z = z

    # Representation   
    def __repr__(self) -> str: 
        return f"GeometriskForm( x = {self.x}, y = {self.y}, z = {self.z} )"




class Rektangel(GeometriskForm):
    """Klass för rektanglar"""

    # Initierar objekt av klassen
    def __init__(self, x: float, y: float, a: float, b: float) -> None:
        """x, y rektangelns mittpunkt. a sidlängd i x-led. b sidlängd i y-led."""
        self.a = a
        self.b = b
        super().__init__(x, y) # Tillkalla föräldrarklassens __init__

    # Sidlängder som propertys
    @property
    def a(self) -> float:
        return self._a
        
    @a.setter
    def a(self, val: float) -> None:
        Rektangel._kontroll_inte_negativt(val) # Sidan a kan inte vara negativ
        self._a = val

    @property
    def b(self) -> float:
        return self._b

    @b.setter
    def b(self, val: float) -> None:
        Rektangel._kontroll_inte_negativt(val) # Sidan b kan inte vara negativ
        self._b = val

    # Geometriska metoder
    def omkrets(self) -> float:
        """Rektangelns omkrets"""
        return (self.a + self.b) * 2

    def area(self) -> float:
        """Rektangelns area"""
        return (self.a * self.b)

    # Jämförande metoder
    def inne_i(self, x: float, y: float) -> bool:
        """Kontrollerar om en punkt tillhör rektangeln eller ej"""
        return Rektangel._avstand_mitt(self.a/2, x1=self.x, x2=x) and Rektangel._avstand_mitt(self.b/2, y1=self.y, y2=y) # Kontrollera avstånd mellan punkt och mittpunkt i x- och y-led separat.

    def __eq__(self, other: "Rektangel") -> bool: 
        """Kontrollerar om rektangeln har samma sidlängder som en annan rektangel"""
        if not isinstance(other, Rektangel):                    # Kontrollera att other är ett objekt av klassen Rektangel
            raise TypeError("Måste vara av klassen Rektangel") 
        return (self.a == other.a and self.b == other.b) or (self.a == other.b and self.b == other.a) # Kontollera om rektanglarna har samma sidlängder

    # Representation
    def __repr__(self) -> str: 
        return f"Rektangel( x = {self.x}, y = {self.y}, a = {self.a}, b = {self.b} )"




class Cirkel(GeometriskForm):
    "Klass för cirklar"

    # Initierar objekt av klassen Cirkel
    def __init__(self, x: float, y: float, r :float) -> None:
        """x, y, z: koordinater cirkelns mittpunkt. r cirkelns radie"""
        self.r = r        
        super().__init__(x, y) # Tillkalla föräldrarklassens __init__

    # Radien som property   
    @property
    def r(self) -> float:
        return self._r

    @r.setter
    def r(self, val: float) -> None:
        Cirkel._kontroll_inte_negativt(val) # Radien kan inte vara negativ
        self._r = val

    # Geometriska metoder
    def omkrets(self) -> float: # Mår lite dåligt för att det är samma formel i sfären. Hade jag tid kunde jag gjort en egen klass för GeometriskaBeräkningar och använda konstitution. Varför kom jag inte på det med en gång.
        """Beräknar cirkelns omkrets med τ"""
        print("\U0001F49A", '\u03C4')
        return tau * self.r     
    
    def area(self) -> float:
        """Beräknar cirkelns area med τ"""
        return tau * self.r**2 /2       

    # Jämförande metoder
    def inne_i(self, x: float, y: float) -> bool:
        """Kontrollerar om en punkt tillhör cirkeln eller ej"""
        return Cirkel._avstand_mitt(self.r, x1=self.x, y1=self.y, x2=x, y2=y)

    def __eq__(self, other: "Cirkel") -> bool:
        """Kontrollerar om cirkeln har samma radie som en annan cirkel"""

        if not isinstance(other, Cirkel):       # Kontrollerar att other är ett objekt av klassen Cirkel
            raise TypeError("Måste vara av klassen Cirkel") 
        return self.r == other.r

    # Representation
    def __repr__(self) -> str:
        return f"Cirkel( x = {self.x}, y = {self.y}, r = {self.r} )"




class Kub(GeometriskForm):
    """Klass för kuber"""

    # Initierar objekt av klassen Kub
    def __init__(self, x: float, y: float, z: float, a: float) -> None:
        """x, y, z kubens mittpunkt. a är kubens sidlängd"""
        self.a = a
        super().__init__(x, y, z) # Tillkalla föräldrarklassens __init__

    # Sidlängd som property
    @property
    def a(self) -> float:
        return self._a

    @a.setter
    def a(self, val: float) -> None:   
        Kub._kontroll_inte_negativt(val) # Sidlängden kan inte vara negativ
        self._a = val

    # Geometriska metoder
    def langd_kanter(self) -> float:
        """Beräknar summan av längden på kanterna"""
        return 12 * self.a 
        

    def area(self) -> float:
        """Beräknar begränsningsarean"""
        return 6 * self.a**2    # Avgränsningsarea = 6 * arean av en sida


    def volym(self) -> float:
        """Beräknar volymen"""
        return self.a**3    

    # Jämförande metoder
    def inne_i(self, x: float, y: float, z: float) -> bool:
        """Kontrollerar om en punkt tillhör kuben eller ej"""
        return (Kub._avstand_mitt(self.a/2, x1=self.x, x2=x) and   # Kontrollera avstånd i x-led mellan punkt och mittpunkt
                Kub._avstand_mitt(self.a/2, y1=self.y, y2=y) and   # Kontrollera avstånd i y-led mellan punkt och mittpunkt
                Kub._avstand_mitt(self.a/2, z1=self.z, z2=z) )     # Kontrollera avstånd i z-led mellan punkt och mittpunkt
    
    def __eq__(self, other: "Kub") -> bool:
        """Kontrollerar om kuben har samma sidlängd som en annan kub"""
        if not isinstance(other, Kub):              # Kontrollerar att other är ett objekt av klassen Kub
            raise TypeError("Måste vara av klassen Kub") 
        return self.a == other.a

    # Representation
    def __repr__(self) -> str:
        return f"Kub( x = {self.x}, y = {self.y}, z = {self.z}, a = {self.a} )"




class Sfar(GeometriskForm):
    """Klass för sfärer"""
    
    # Initierar objekt av klassen Sfar
    def __init__(self, x: float, y: float, z: float, r: float) -> None:
        """x, y, z kubens mittpunkt. r är sfärens radie"""
        self.r = r
        super().__init__(x, y, z) # Tillkalla föräldrarklassens __init__

    # Radien som property  
    @property
    def r(self) -> float:
        return self._r

    @r.setter
    def r(self, val: float) -> float:
        Sfar._kontroll_inte_negativt(val)
        self._r = val

    # Geometriska metoder
    def omkrets(self) -> float:  # Upprepad kod 😰
        print("\U0001F49A", '\u03C4')
        return tau * self.r     

    def area(self) -> float:
        """Beräknar mantelarean"""
        return 2 * tau * self.r**2

    def volym(self) -> float:
        """Beräknar volymen"""
        return 2/3 * tau * self.r**3

    # Jämförande metoder
    def inne_i(self, x: float, y: float, z: float) -> bool:
        """Kontrollerar om en punkt tillhör sfären eller ej"""
        return Sfar._avstand_mitt(self.r, self.x, self.y, self.z, x, y, z) # kontrollera euklidiskt avstånd mellan punkt och mittpunkt

    def __eq__(self, other: "Sfar") -> bool:
        """Kontrollerar om sfären har samma radie som en annan sfär"""
        if not isinstance(other, Sfar):             # Kontrollerar att other är ett objekt av klassen Sfär
            raise TypeError("Måste vara av klassen Sfar") 
        return self.r == other.r

    # Representation
    def __repr__(self) -> str:
        return f"Sfar( x = {self.x}, y = {self.y}, z = {self.z}, r = {self.r} )"
