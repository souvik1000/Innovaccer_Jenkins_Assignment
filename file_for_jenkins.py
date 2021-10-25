from DevelopedCode import Calculator
import unittest



class testingUser(unittest.TestCase):
    def setUp(self):
        self.add_check = Calculator.Calculator(10, 20)
        self.sub_check = Calculator.Calculator(30, 20)
        self.mult_check = Calculator.Calculator(7, 8)
        self.div_check = Calculator.Calculator(70, 7)

    def test_addition(self):
        self.assertEqual(30, self.add_check.addition())

    def test_subCheck(self):
        self.assertEqual(10, self.sub_check.substraction())

    def test_multCheck(self):
        self.assertEqual(56, self.mult_check.multiply())
    
    def test_divCheck(self):
        self.assertEqual(10, self.div_check.divition())


if __name__ == "__main__":
    unittest.main()