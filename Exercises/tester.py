from fraction import Fraction
import unittest


class TestFraction(unittest.TestCase):

    #def setUp(self) -> None:
    #    return super().setUp()

    # Tester

    # Test mata in rätt typ nämnare
    def test_typ_taljare(self) -> None:
        with self.assertRaises(TypeError):
            Fraction(1.2,2)

    # Test mata in rätt typ täljare
    def test_typ_namnare(self) -> None:
        with self.assertRaises(TypeError):
            Fraction(1, 1.2)


    # Test mata in täljaren = 0
    def test_0_taljare(self) -> None:
        with self.assertRaises(ValueError):
            Fraction(1, 0)

    # Test skapa Fraction
    def test_skapa_fraction(self) -> None:
        f = Fraction(1,2)
        self.assertEquals((f.taljare, f.namnare), (1, 2))
    
    # Test förenkla
    def test_forenkla(self) -> None:
        f = Fraction(3, -9)
        f = f.simplify()
        self.assertEqual((f.taljare, f.namnare), (-1, 3))

    # Test Mixed  
    def test_mixed(self) -> None:
        f = Fraction(9, -4)
        self.assertEqual(f.mixed(), "-2 1/4")
     
    # Test +
    def test_add(self) -> None:
        f = Fraction(1, 2) + Fraction(2, 3)
        self.assertEqual((f.taljare, f.namnare), (7, 6))

    # Test Fraction + int
    def test_add_int(self) -> None:
        f = Fraction(1, 2) + 1
        self.assertEqual((f.taljare, f.namnare), (3, 2))  

       # Test int + Fraction
    def test_radd_int(self) -> None:
        f = 1 + Fraction(1, 2)
        self.assertEqual((f.taljare, f.namnare), (3, 2))  

    # Test -
    def test_sub(self) -> None:
        f = Fraction(1, 2) - Fraction(2, 3)
        self.assertEqual((f.taljare, f.namnare), (-1, 6))
    
    # Test *
    def test_mul(self) -> None:
        f = Fraction(1, 2) * Fraction(2, 3)
        self.assertEqual((f.taljare, f.namnare), (1, 3))
    
    # Test /
    def test_div(self) -> None:
        f = Fraction(1, 2) /  Fraction(2, 3)
        self.assertEqual((f.taljare, f.namnare), (3, 4))
     
    # Test == 
    def test_likamed(self) -> None:
        f1, f2 = Fraction(2,3), Fraction(2,3)
        self.assertTrue(f1 == f2)

    # Test  !=
    def test_inte_likamed(self) -> None:
        f1, f2 = Fraction(2,3), Fraction(-2,3)
        self.assertFalse(f1 == f2)


if __name__ == "__main__":
    unittest.main()