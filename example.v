/*
 * This is an example of a simple, code
 * that is meant to show off Versace

 * To run this code in windows all you need to do is,
    * "path_to_versace_exe" "example.v"
 
 * To run this code in linux all you need to do is,
    * "path_to_versace" "example.v"
 
 * To run this code in mac all you need to do is,
    * python3 "path_to_versace.py" "example.v"

 * If you want to convert this to python code you an do,
    * "path_to_versace" "example.v" -d

 * If you want to red the data in the debug mode all you do is,
    * "path_to_versace" "example.v" -debug
*/

include [os] // this is a import statement

public main() { // This is the main function it must be there to run the code
    os.system("cls" if os.name == "nt" else "clear") // This is to clear the console
    out < "Welcome to Versace!" < bold red < center; // This is a print statement
    out < "This is a simple example of Versace" < newl < bold red < center;  // This is also a print statement
    CalculateSalary.salary() // This is a function call
} // This is the end of the main function

class CalculateSalary { // This is a class
    func salary() { // This is a function this can also be written as: public salary()
        in salary < "Enter your salary: " < int < bold green; // This is to get the salary
        in tax < "Enter your tax (in %): " < int < bold green; // This is to get the tax
        finalsalary! = salary - (salary * tax / 100) // This is to calculate the final salary by subtracting the tax from the salary
        out < f"Your final salary is: {finalsalary!}" < newl < bold red < center; // This is to print the final salary
    } // This is the end of the function
} // This is the end of the class