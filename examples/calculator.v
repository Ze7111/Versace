[-*- no init -*-]       // this is to disable the use of public init to start the program

/*
This is a simple calculator made with the WinUI module and the tkinter module
This program is written in Versace Programming Language
More information about the language can be found at https://github.com/Ze7111/Versace
*/

include "Winui.vh" as cal; include "std.v"; include "StringVar" from "tkinter"; // this is to include all the required modules

usize s = ttk::Style(); // this is to create a style for the buttons
let s::configure("TButton", font=("arial", 20, "bold")); // this is to set the font for the buttons

let cal::title("Calculator"); // this is to set the title of the calculator
str operator = ""; // this is to create a string variable for the operators
usize text_input = StringVar(); // this is to create a string variable for the text input

func btnclick(numbers) // this function is for the buttons
{
    ref operator; // this is to create a reference to the operator variable
    let operator = operator + str(numbers); // this is to add the numbers to the operator variable
    let text_input::set(operator); // this is to set the text input to the operator variable
}

func btn_clear_display() // this function is for the clear button
{
    ref operator; // this is to create a reference to the operator variable
    let operator = ""; // this is to set the operator variable to an empty string
    let text_input::set(""); // this is to set the text input to an empty string
}

func btn_equals_input() // this function is for the equal button
{
    ref operator; // this is to create a reference to the operator variable
    str sumup = str(eval(operator)); // this is to evaluate the operator variable
    let text_input::set(sumup); // this is to set the text input to the sumup variable
    let operators = ""; // this is to set the operator variable to an empty string
} 

usize txtdisplay  = ttk::Entry(cal | textvariable=text_input | font=("arial" | 20 | "bold") | justify="right")::grid(columnspan=4 | ipadx=10 | ipady=20 | padx=10 | pady=10); // this is to create the text input

usize btnclear    = ttk::Button(cal | text="C" | style="TButton" | command=btn_clear_display)    :: grid(row=1 | column="0" | padx=4 | pady=8 | ipadx=16 | ipady=16); // this is to create the clear button
usize btnm        = ttk::Button(cal | text="M" | style="TButton"                            )    :: grid(row=1 | column="1" | padx=4 | pady=8 | ipadx=16 | ipady=16); // this is to create the memory button
usize btnbraket1  = ttk::Button(cal | text="(" | style="TButton" | command=lambda:btnclick("(")) :: grid(row=1 | column="2" | padx=4 | pady=8 | ipadx=16 | ipady=16); // this is to create the bracket button
usize btnbracket2 = ttk::Button(cal | text=")" | style="TButton" | command=lambda:btnclick(")")) :: grid(row=1 | column="3" | padx=4 | pady=8 | ipadx=16 | ipady=16); // this is to create the bracket button
usize btn7        = ttk::Button(cal | text="7" | style="TButton" | command=lambda:btnclick(7))   :: grid(row=2 | column="0" | padx=4 | pady=8 | ipadx=16 | ipady=16); // this is to create the number button
usize btn8        = ttk::Button(cal | text="8" | style="TButton" | command=lambda:btnclick(8))   :: grid(row=2 | column="1" | padx=4 | pady=8 | ipadx=16 | ipady=16); // this is to create the number button
usize btn9        = ttk::Button(cal | text="9" | style="TButton" | command=lambda:btnclick(9))   :: grid(row=2 | column="2" | padx=4 | pady=8 | ipadx=16 | ipady=16); // this is to create the number button
usize division    = ttk::Button(cal | text="/" | style="TButton" | command=lambda:btnclick("/")) :: grid(row=2 | column="3" | padx=4 | pady=8 | ipadx=16 | ipady=16); // this is to create the operator button 
usize btn6        = ttk::Button(cal | text="6" | style="TButton" | command=lambda:btnclick(6))   :: grid(row=3 | column="0" | padx=4 | pady=8 | ipadx=16 | ipady=16); // this is to create the number button
usize btn5        = ttk::Button(cal | text="5" | style="TButton" | command=lambda:btnclick(5))   :: grid(row=3 | column="1" | padx=4 | pady=8 | ipadx=16 | ipady=16); // this is to create the number button 
usize btn4        = ttk::Button(cal | text="4" | style="TButton" | command=lambda:btnclick(4))   :: grid(row=3 | column="2" | padx=4 | pady=8 | ipadx=16 | ipady=16); // this is to create the number button
usize subtract    = ttk::Button(cal | text="-" | style="TButton" | command=lambda:btnclick("-")) :: grid(row=3 | column="3" | padx=4 | pady=8 | ipadx=16 | ipady=16); // this is to create the operator button
usize btn3        = ttk::Button(cal | text="3" | style="TButton" | command=lambda:btnclick(3))   :: grid(row=4 | column="0" | padx=4 | pady=8 | ipadx=16 | ipady=16); // this is to create the number button
usize btn2        = ttk::Button(cal | text="2" | style="TButton" | command=lambda:btnclick(2))   :: grid(row=4 | column="1" | padx=4 | pady=8 | ipadx=16 | ipady=16); // this is to create the number button 
usize btn1        = ttk::Button(cal | text="1" | style="TButton" | command=lambda:btnclick(1))   :: grid(row=4 | column="2" | padx=4 | pady=8 | ipadx=16 | ipady=16); // this is to create the number button
usize multiply    = ttk::Button(cal | text="*" | style="TButton" | command=lambda:btnclick("*")) :: grid(row=4 | column="3" | padx=4 | pady=8 | ipadx=16 | ipady=16); // this is to create the operator button 
usize btn0        = ttk::Button(cal | text="0" | style="TButton" | command=lambda:btnclick(0))   :: grid(row=5 | column="0" | padx=4 | pady=8 | ipadx=16 | ipady=16); // this is to create the number button
usize dot         = ttk::Button(cal | text="." | style="TButton" | command=lambda:btnclick(".")) :: grid(row=5 | column="1" | padx=4 | pady=8 | ipadx=16 | ipady=16); // this is to create the number button
usize equal       = ttk::Button(cal | text="=" | style="TButton" | command=btn_equals_input)     :: grid(row=5 | column="2" | padx=4 | pady=8 | ipadx=16 | ipady=16); // this is to create the equal button
usize addition    = ttk::Button(cal | text="+" | style="TButton" | command=lambda:btnclick("+")) :: grid(row=5 | column="3" | padx=4 | pady=8 | ipadx=16 | ipady=16); // this is to create the operator button
let cal::mainloop(); // this is to run the calculator window
