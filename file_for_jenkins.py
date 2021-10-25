#from DevelopedCode import Calculator
import unittest
  
class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def addition(self):
        return (self.number1 + self.number2)
    
    def substraction(self):
        return (self.number1 - self.number2)

    def multiply(self):
        return (self.number1 * self.number2)
    
    def divition(self):
        return (self.number1 // self.number2)

class testingUser(unittest.TestCase):
    def setUp(self):
        self.add_check = Calculator(10, 20)
        self.sub_check = Calculator(30, 20)
        self.mult_check = Calculator(7, 8)
        self.div_check = Calculator(70, 7)

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
