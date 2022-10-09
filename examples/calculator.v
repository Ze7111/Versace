// THIS IS A MODULE FOR THE EXAMPLE.V
// Running this directly will cause errors

// This is an example program made using verscae by ze7111.
// This program is a simple calculator that can add, subtract, multiply, and divide.
// This program is made for the purpose of showing how verscae works.
// This program also shows the interopability of verscae with python.

include [time] // time is a python module but it will work with verscae

class Calculator { // in out lang we can make comments like this anywhere in the code and they will be ignored by the compiler
    // This is the class that contains all of the calculator functions
    // It is a class because it is easier to organize the functions this way
    func add(a, b) {
        // This function adds two numbers
        return a + b; // As you can see a ; does work
    }

    func subtract(a, b) {
        // This function subtracts two numbers
        return a - b
    }

    func multiply(a, b) {
        // This function multiplies two numbers
        return a * b
    }

    func divide(a, b) { // No indentation needed, even tho this function is a part of this class, not indenting it will still work as it should
        return a / b
    }

    func choose(num1, num2, op) {
    // This function chooses which function to use
        if op == "+" {
            ans = Calculator.add(num1, num2)
            out < "The answer is " < ans < newl < blue
        }
        else if op == "-" {
            ans = Calculator.subtract(num1, num2)
            out < "The answer is " < ans < newl < blue
        }
        else if op == "*" {
            ans = Calculator.multiply(num1, num2)
            out < "The answer is " < ans < newl < blue
        }
        else if op == "/" {
            ans = Calculator.divide(num1, num2)
            out < "The answer is " < ans < newl < blue
        }
        else {
            ans = "Invalid operator"
            out < "" < ans < newl < red
        }
    }
}

public start() { // This is the start function that will be called when the program is run
    // This is the main function 
    in num1 < "Enter a number: " < red < endl < int
    in num2 < "Enter another number: " < red < endl < int
    in op < "Enter an operation: " < red < endl < str

    for i in range(6) {
        out < f"Calculating{'. ' * i}" < rw < green 
        time.sleep(0.5)
    }    
    out < "                        " < rw

    Calculator.choose(num1, num2, op)
}

// Run the program by typing "verscae examples\calculator.v"(if in cmd) in the terminal.
// Remember you do not call the main function, verscae does that for you.
// Remember to always have a public main function in your program or it will not run.