import unittest

class TestFraction(unittest.TestCase):

    #def setUp(self) -> None:
    #    return super().setUp()

    # Tester

    # Test mata in float
    def test_typ_taljare(self) -> None:
        with self.assertRaises(ValueError):
         Fraction(1.2,2)


    # Test mata in felaktiga tal
    # Test skapa Fraction
    # Test heltal
    
   
    # Test förenkla
    
    # Test Mixed
    # 
    # Test +
    # Test -
    # Test *
    # Test /
    # 
    # Test ==