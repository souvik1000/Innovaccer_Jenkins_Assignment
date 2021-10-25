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
