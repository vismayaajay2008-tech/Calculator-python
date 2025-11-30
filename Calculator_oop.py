class Calculator:
    def _init_(self):
        print("Calculator Started!")

    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero!"
        return a / b
        
    def modulus(self, a, b):
        return a % b


# ---- Main Program ----
calc = Calculator()
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", calc.add(a, b))
print("Subtraction:", calc.subtract(a, b))
print("Multiplication:", calc.multiply(a, b))
print("Division:", calc.divide(a, b))
print("Modulus:",calc.modulus(a,b))

