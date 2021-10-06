from math import tau, sqrt
import unittest
from unittest.main import main
import lab3 as l

class TestGeometriskForm(unittest.TestCase):
    def setUp(self) -> None:
        self.geo_form_2D = l.GeometriskForm(-1, 2)
        self.geo_form_3D = l.GeometriskForm(-1, 2, 3)

    # Testa metoder för felhantering i indata
    # 1
    def test_ange_float(self):
        l.GeometriskForm._test_reelt(tau)

    # 2
    def test_ange_int(self):
        l.GeometriskForm._test_reelt(-1)

    # 3 
    def test_ange_felaktig_typ(self):
        with self.assertRaises(TypeError):
            l.GeometriskForm._test_reelt("pi")    

    # 4
    def test_negativt_tal(self):
        with self.assertRaises(ValueError):
            l.GeometriskForm._test_inte_negativt(-1)

    # 5
    def test_noll_negativt(self): # TODO är detta rätt sätt?
        l.GeometriskForm._test_inte_negativt(0)
        
          
    # Test skapa objekt
    # 6
    def test_skapa_form_2D(self) -> None:
        f = self.geo_form_2D
        self.assertEqual((f.x, f.y, f.z) , (-1, 2, None))

    # 7
    def test_skapa_form_3D(self):
        f = self.geo_form_3D   
        self.assertEqual((f.x, f.y, f.z),  (-1, 2, 3))

    # 8
    def test_skapa_form_indata_val(self):
        with self.assertRaises(TypeError):
            l.GeometriskForm(1,'2', 3)
    
    # 9
    def test_skapa_form_indata_val2(self):  # z behandlas lite annorlunda
        with self.assertRaises(TypeError):
            l.GeometriskForm(1, 2, '3')

    # 10
    def test_skapa_tom_form(self):
        with self.assertRaises(TypeError):
            l.GeometriskForm()

    # Test flytta
    # 11
    def test_flytta_abs_2D(self):
        f = self.geo_form_2D
        f.flööö(6, -7)
        self.assertEqual((f.x, f.y, f.z), (6, -7, None))

    # 12
    def test_flytta_abs_3D(self):
        f = self.geo_form_3D
        f.flööö(6, -7, 8)
        self.assertEqual((f.x, f.y, f.z), (6, -7, 8))

    # 13
    def test_flytta_rel_2D(self):
        f = self.geo_form_2D
        f.flööö(6, -7, relativ=True)
        self.assertEqual((f.x, f.y, f.z), (5, -5, None))

    # 14
    def test_flytta_rel_3D(self):
        f = self.geo_form_3D
        f.flööö(6, -7, 8, relativ=True)
        self.assertEqual((f.x, f.y, f.z), (5, -5, 11))

    # 15 
    def test_flytta_2D_i_3D(self): 
        with self.assertRaises(TypeError):
            f = self.geo_form_2D
            f.flööö(6, -7, 8)

    # 16
    def test_flytta_3D_i_2D(self):
        with self.assertRaises(TypeError):
            f = self.geo_form_3D
            f.flööö(6, -7)

    # Test _avstand_mitt()
    # 17
    def test_avstand_mitt_rand(self):
        a_m = l.GeometriskForm._avstand_mitt(5, x1=3, y1=0, z1=3, x2=-1, y2=0, z2=0)
        self.assertTrue(a_m)     

    # 18
    def test_avstand_mitt_langre(self):
        a_m = l.GeometriskForm._avstand_mitt(1, x2=-2)
        self.assertFalse(a_m)  

    # 19
    def test_avstand_mitt_narmare(self):
        a_m = l.GeometriskForm._avstand_mitt(3, x2=1)
        self.assertTrue(a_m) 

    # 20 
    def test_avstand_mitt_neg_avs(self):
        with self.assertRaises(ValueError):
            l.GeometriskForm._avstand_mitt(-1)

    # 21 
    def test_avstand_mitt_type(self):
        with self.assertRaises(TypeError):
            l.GeometriskForm._avstand_mitt("hej") 

    # 22
    def test_repr(self):                     
        f = self.geo_form_2D
        self.assertEqual(f.__repr__(), "GeometriskForm( x = -1, y = 2, z = None)" ) 




class TestRektangel(unittest.TestCase):
    def setUp(self) -> None:
        self.rektangel = l.Rektangel(-1, 0, 4.2, 2)

    # Test skapa objekt
    # 23
    def test_skapa_rektangel(self) -> None:
        re = self.rektangel
        self.assertEqual((re.x, re.y, re.a, re.b) , (-1, 0, 4.2, 2))

    # 24
    def test_skapa_rektangel_indata_val(self):
        with self.assertRaises(TypeError):
            l.Rektangel(1,'2', 3, 4)
    
    # 25
    def test_skapa_rektangel_neg_sida(self):  
        with self.assertRaises(ValueError):
            l.Rektangel(1, 2, -3, 4)

    # 26
    def test_skapa_tom_rektangel(self):
        with self.assertRaises(TypeError):
            l.Rektangel()
   
        
    # Geometriska metoder
    # 27
    def testa_omkrets(self):
        o  = self.rektangel.omkrets()
        self.assertEqual(o, 12.4)

    # 28
    def testa_area(self):
        a = self.rektangel.area()
        self.assertEqual(a, 8.4)    

    # Testa inne_i()
    # 29
    def test_punkt_inne_i(self):
        re = self.rektangel
        self.assertTrue(re.inne_i(0, 0))    

    # 30
    def test_punkt_inne_i2(self):
        re = self.rektangel
        self.assertTrue(re.inne_i(-3.1, 0.9))   

    # 31
    def test_punkt_horn(self):
        re = self.rektangel
        self.assertTrue(re.inne_i(1.1, 1))   

    # 32  
    def test_punkt_utanfor_x (self):
        re = self.rektangel
        self.assertFalse(re.inne_i(1.11, 1))   

    # 33 
    def test_punkt_utanfor_y (self):
        re = self.rektangel
        self.assertFalse(re.inne_i(1.1, 1.1))   

    # Test av __eq__
    # 34
    def test_lika(self):
        re1 = l.Rektangel(0, 0, 2, 3)
        re2 = l.Rektangel(1, 1, 2, 3)
        self.assertTrue(re1 == re2)

    # 35
    def test_lika_vriden(self):
        re1 = l.Rektangel(0, 0, 2, 3)
        re2 = l.Rektangel(1, 1, 3, 2)
        self.assertTrue(re1 == re2)
    
    # 36
    def test_olika(self):
        re1 = l.Rektangel(0, 0, 2, 3)
        re2 = l.Rektangel(0, 0, 1, 3)
        self.assertFalse(re1 == re2)
    
    # 37
    def test_lika_not_rektangel(self):
        with self.assertRaises(TypeError):
            re1 = l.Rektangel(0, 0, 2, 3)
            re1 == 2
    
    # 38
    def test_repr(self):                     
        re = self.rektangel
        self.assertEqual(re.__repr__(), "Rektangel( x = -1, y = 0, a = 4.2, b = 2)" ) 




class TestCirkel(unittest.TestCase):    
    def setUp(self) -> None:
         self.enhetscirkel = l.Cirkel(0, 0, 1)
         

     
    # Test skapa objekt
    # 39
    def test_skapa_cirkel(self) -> None:
        c = self.enhetscirkel
        self.assertEqual((c.x, c.y, c.r) , (0, 0, 1))

    # 40
    def test_skapa_cirkel_indata_val(self):
        with self.assertRaises(TypeError):
            l.Cirkel(1,'2', 3)
    
    # 41
    def test_skapa_cirkel_neg_radie(self):  
        with self.assertRaises(ValueError):
            l.Cirkel(1, 2, -3)

    # 42
    def test_skapa_tom_cirkel(self):
        with self.assertRaises(TypeError):
            l.Cirkel()
      
    # Geometriska metoder
    # 43
    def testa_omkrets(self):
        o  = self.enhetscirkel.omkrets()
        self.assertEqual(o, tau)

    # 44
    def testa_area(self):
        a = self.enhetscirkel.area()
        self.assertEqual(a, tau/2)    

    # Testa inne_i()
    # 45
    def test_punkt_inne_i(self):
        c = self.enhetscirkel
        self.assertTrue(c.inne_i(0.5, -0.5))    

    # 46
    def test_punkt_rand(self):
        c = self.enhetscirkel
        xy = 1/sqrt(2)
        self.assertTrue(c.inne_i(xy, xy))   

    # 47
    def test_punkt_utanfor_x (self):
        c = self.enhetscirkel
        self.assertFalse(c.inne_i(1.1, 1))   

    # 48 
    def test_punkt_utanfor_y (self):
        c = self.enhetscirkel
        self.assertFalse(c.inne_i(1, 1.1))     

    # Test av __eq__
    # 49
    def test_lika(self):
        c1 = l.Cirkel(0, 0, 2)
        c2 = l.Cirkel(1, 1, 2)
        self.assertTrue(c1 == c2)

    # 50
    def test_olika(self):
        re1 = l.Cirkel(0, 0, 2)
        re2 = l.Cirkel(0, 0, 1)
        self.assertFalse(re1 == re2)
   
    # 51
    def test_lika_not_cicl(self):
        with self.assertRaises(TypeError):
            c = self.enhetscirkel
            c == 2
    
    # 52
    def test_repr(self):                     
        c = self.enhetscirkel
        self.assertEqual(c.__repr__(), "Cirkel( x = 0, y = 0, r = 1)" ) 
 








class TestKub(unittest.TestCase):
    pass




if __name__ == "__main__":
    unittest.main()
   