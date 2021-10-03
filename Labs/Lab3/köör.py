from math import tau, sqrt
import lab3 as l
import numpy as np

#form = l.Geometrisk_form(5, 4)
#form2 = l.Geometrisk_form(5, 4, 2)
#form.rita_ut()

#form.flööö(3, 3 )

#form.flööö(0, -6, True )


#cirkel1 = l.Cirkel(5, 4, 4)
#cirkel2 = l.Cirkel(5, 4, 3.2)
#cirkel3 = l.Cirkel(5, 4, 1)

#cirkel.flööö(3, 0)
#cirkel1.flööö(3, 3, True)

#print(cirkel1 == cirkel2)
#print(3 == cirkel1)
#print("\U0001F49A",'\u03C4')

#print(cirkel1.inne_i(1, 1))     # False
#print(cirkel1.inne_i(5, 0))     # True
#print(cirkel1.inne_i(5, 1))     # True
#x1 = 5 + 4 * np.cos(3*tau/8)    
#y1 = 4 + 4 * np.sin(3*tau/8)
#print(cirkel1.inne_i(x1, y1))   # True

#print(cirkel3.area())
#print(cirkel3.omkrets())

#print(cirkel3)


#r = l.Rektangel(4,4,3,2)
#r2 = l.Rektangel(5,5,3,2)
#r3 = l.Rektangel(4,4,1,2)
#r4 = l.Rektangel(1,1,2,3)
#print(r.inne_i(3,4))    #True
#print(r.inne_i(2.5,4))  #True
#print(r.inne_i(5,1))    #False
#print(r.inne_i(5.6, 4)) #False
#print(r)
#print(r.area())
#print(r.omkrets())
#print(r == 3)
#print(r == r2)
#print(r == r3)
#print(r == r4)

#k = l.Kub(4, 4, 4, 3)

#print(k)

#print( k.omkrets() )
#print( k.area() )
#print( k.volym() )

#print(k.inne_i(4,4,3))      # True
#print(k.inne_i(1,1,1))      # False
#print(k.inne_i(-1,-1,-1))   # False
#print(k.inne_i(3,4,5.5))    # True

#print(k == l.Kub(1, 1, 1, 3)) # True
#print(k == l.Kub(4, 4, 4, 2)) # False
#k.flööö(5, 5, 5)
#print(  k )


s1 = l.Sfar(4,4,4,3)
s2 = l.Sfar(1,1,1,3)
s3 = l.Sfar(4,4,4,2)

#print(s1)
#print(s1.omkrets())
#print(s1.area())
#print(s1.volym())

#print(s1.inne_i(4, 4, 3))   # True
#print(s1.inne_i(1,1,1))     # False
#print(s1.inne_i(5.5,4,4))   # True

#print(s1 == 3)
#print(s1 == s2) 
#print(s1 == s3)

#s1.flööö(5,5,5)
#print(s1)

#s1.flööö(5,5,5, True)
#print(s1)