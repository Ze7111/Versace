from rich import console; print = console.Console().print


import time 
class Calculator:
    
    
    def add(a, b):
        
        return a + b;
    def subtract(a, b):
        
        return a - b;
    def multiply(a, b):
        
        return a * b;
    def divide(a, b):
        
        return a / b;
    def choose(num1, num2, op):
        
        if op == "+":
            ans = Calculator.add(num1, num2)
            print("The answer is ", ans, end="\n", style="blue")
        elif op == "-":
            ans = Calculator.subtract(num1, num2)
            print("The answer is ", ans, end="\n", style="blue")
        elif op == "*":
            ans = Calculator.multiply(num1, num2)
            print("The answer is ", ans, end="\n", style="blue")
        elif op == "/":
            ans = Calculator.divide(num1, num2)
            print("The answer is ", ans, end="\n", style="blue")
        else:
            ans = "Invalid operator"
            print("", ans, end="\n", style="red")
def main():
    
    print("Enter a number: ", style="red", end="")
    num1 = int(input())
    print("Enter another number: ", style="red", end="")
    num2 = int(input())
    print("Enter an operation: ", style="red", end="")
    op = str(input())
    Calculator.choose(num1, num2, op)
main() 
