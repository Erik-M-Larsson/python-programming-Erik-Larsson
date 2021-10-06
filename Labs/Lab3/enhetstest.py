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
        self.assertEqual(f.__repr__(), "GeometriskForm( x = -1, y = 2, z = None )" ) 




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
    def test_omkrets(self):
        o  = self.rektangel.omkrets()
        self.assertEqual(o, 12.4)

    # 28
    def test_area(self):
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
        self.assertEqual(re.__repr__(), "Rektangel( x = -1, y = 0, a = 4.2, b = 2 )" ) 




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
    def test_omkrets(self):
        o  = self.enhetscirkel.omkrets()
        self.assertEqual(o, tau)

    # 44
    def test_area(self):
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
        self.assertEqual(c.__repr__(), "Cirkel( x = 0, y = 0, r = 1 )" ) 
 



class TestKub(unittest.TestCase):
    def setUp(self) -> None:
        self.kub = l.Kub(-1, 0, 1, 2)

    # Test skapa objekt
    # 53
    def test_skapa_kub(self) -> None:
        k = self.kub
        self.assertEqual((k.x, k.y, k.z, k.a) , (-1, 0, 1, 2))

    # 54
    def test_skapa_kub_indata_val(self):
        with self.assertRaises(TypeError):
            l.Rektangel(1,'2', 3, 4)
   
    # 55
    def test_skapa_kub_neg_sida(self):  
        with self.assertRaises(ValueError):
            l.Kub(1, 2, 3, -4)

    # 56
    def test_skapa_tom_kub(self):
        with self.assertRaises(TypeError):
            l.Kub()
      
    # Geometriska metoder
    # 57
    def test_omkrets(self):
        o  = self.kub.omkrets()
        self.assertEqual(o, 24)

    # 58
    def test_area(self):
        a = self.kub.area()
        self.assertEqual(a, 24)    
 
    # 59
    def test_volym(self):
        v = self.kub.volym()
        self.assertEqual(v, 8) 

    # Testa inne_i()
    # 60
    def test_punkt_inne_i(self):
        k = self.kub
        self.assertTrue(k.inne_i(-0.5, 0.5, 0.5))    

    # 61
    def test_punkt_inne_i2(self):
        k = self.kub
        self.assertTrue(k.inne_i(-0.1, 0.9, 1.9))   

    # 62
    def test_punkt_horn(self):
        k = self.kub
        self.assertTrue(k.inne_i(0, 1, 2))   

    # 63  
    def test_punkt_utanfor_x (self):
        k = self.kub
        self.assertFalse(k.inne_i(1, 0, 1))   

    # 64 
    def test_punkt_utanfor_y (self):
        k = self.kub
        self.assertFalse(k.inne_i(-1, -2, 1)) 

    # 65 
    def test_punkt_utanfor_z (self):
        k = self.kub
        self.assertFalse(k.inne_i(-1, -0, 3)) 

    # Test av __eq__
    # 66
    def test_lika(self):
        k1 = l.Kub(0, 0, 0, 3)
        k2 = l.Kub(1, 1, 2, 3)
        self.assertTrue(k1 == k2)
 
    # 67
    def test_olika(self):
        k1 = l.Kub(0, 0, 2, 3)
        k2 = l.Kub(0, 0, 2, 1)
        self.assertFalse(k1 == k2)
    
    # 68
    def test_lika_not_Kub(self):
        with self.assertRaises(TypeError):
            k1 = l.Kub(0, 1, 2, 2)
            k1 == 2

    # 69
    def test_repr(self):                     
        k = self.kub
        self.assertEqual(k.__repr__(), "Kub( x = -1, y = 0, z = 1, a = 2 )" ) 




class TestSfar(unittest.TestCase):
    def setUp(self) -> None:
        self.enhetssfar = l.Sfar(0, 0, 0, 1)

    # Test skapa objekt
    # 70
    def test_skapa_sfar(self) -> None:
        s = self.enhetssfar
        self.assertEqual((s.x, s.y, s.z, s.r) , (0, 0, 0, 1))

    # 71
    def test_skapa_sfar_indata_val(self):
        with self.assertRaises(TypeError):
            l.Sfar(1,'2', 3, 4)
   
    # 72
    def test_skapa_sfar_neg_radie(self):  
        with self.assertRaises(ValueError):
            l.Sfar(1, 2, 3, -4)

    # 73
    def test_skapa_tom_sfar(self):
        with self.assertRaises(TypeError):
            l.Sfar()
      
    # Geometriska metoder
    # 74
    def test_omkrets(self):
        o  = self.enhetssfar.omkrets()
        self.assertEqual(o, tau)

    # 75
    def test_area(self):
        a = self.enhetssfar.area()
        self.assertEqual(a, 2*tau)    

    # 76   
    def test_volym(self):
        v = self.enhetssfar.volym()
        self.assertEqual(v, 2*tau/3)
 
   # Testa inne_i()
    # 77
    def test_punkt_inne_i(self):
        s = self.enhetssfar
        self.assertTrue(s.inne_i(-0.5, 0.5, 0.5))     

    # 78
    def test_punkt_yta(self):
        s = self.enhetssfar
        yz = 1/sqrt(2)
        self.assertTrue(s.inne_i(0, yz, yz))   

    # 79  
    def test_punkt_utanfor_x (self):
        s = self.enhetssfar
        self.assertFalse(s.inne_i(1.1, 0, 0))   

    # 80 
    def test_punkt_utanfor_y (self):
        s = self.enhetssfar
        self.assertFalse(s.inne_i(0, -2, 0)) 

    # 81 
    def test_punkt_utanfor_z (self):
        s = self.enhetssfar
        self.assertFalse(s.inne_i(0, 0, 2)) 
    
    # 82 
    def test_punkt_utanfor_xyz (self):
        s = self.enhetssfar
        xyz = 1/sqrt(2)
        self.assertFalse(s.inne_i(xyz , xyz, xyz)) 
 
    # Test av __eq__
    # 83
    def test_lika(self):
        s1 = l.Sfar(0, 0, 0, 3)
        s2 = l.Sfar(1, 1, 2, 3)
        self.assertTrue(s1 == s2)
 
    # 84
    def test_olika(self):
        s1 = l.Sfar(0, 0, 2, 3)
        s2 = l.Sfar(0, 0, 2, 1)
        self.assertFalse(s1 == s2)
  
    # 85
    def test_lika_not_Sfar(self):
        with self.assertRaises(TypeError):
            s1 = l.Sfar(0, 1, 2, 2)
            s1 == 2

    # 86
    def test_repr(self):                     
        s = self.enhetssfar
        self.assertEqual(s.__repr__(), "Sfar( x = 0, y = 0, z = 0, r = 1 )" ) 





if __name__ == "__main__":
    unittest.main()
   