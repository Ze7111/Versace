# Functions

**Documentation reference: ID 46 66756E63**

### What is a Function?

Functions are prevalent in Versace code. You’ve already seen one of the most important functions in the language: the `public main` function, which is the entry point of all Versace programs. You’ve also seen the `func` keyword, which allows you to declare new functions.

Versace code uses snake case as the conventional style for function and variable names, in which all letters are lowercase and underscores separate words. Here’s a program that contains an example function definition:

<div align="left">

<figure><img src="../.gitbook/assets/image (1).png" alt="public main() {     out << &#x22;Hello World&#x22;;     call some_function(); }  func some_function() {     out << &#x22;This is some_function&#x22;; }"><figcaption></figcaption></figure>

</div>

When you call a function, the program jumps to the function’s definition and executes the statements there. When the function ends, the program returns to the point where the function was called. This is called a function call.

We can call any function we’ve defined by entering its name followed by a set of parentheses. Because some\_function is defined in the program, it can be called from inside the main function. Note that we defined another\_function after the main function in the source code; we could have defined it before as well. Versace doesn’t care where you define your functions, only that they’re defined somewhere in a scope that can be seen by the caller.

{% hint style="warning" %}
This does not apply for any calls made outside of the main function. If you call a function outside of the main function, it must be defined before the call.
{% endhint %}

### Function Parameters

Functions can also take parameters. Parameters are variables that are passed to the function when it is called. The function can then use the parameters as if they were regular variables. Here’s an example of a function that takes two parameters:

<div align="left">

<figure><img src="../.gitbook/assets/image (7).png" alt="public main() {     out << &#x22;Hello World&#x22;;     call print_sum(5, 10); }  func print_sum(int a, int b) {     out << a + b; }"><figcaption></figcaption></figure>

</div>

In this example, the function print\_sum takes two parameters, a and b. When the function is called, the values 5 and 10 are passed to the parameters a and b, respectively. The function then prints the sum of a and b.

```
Hello World
15
```

This is the output of the program. The function print\_sum is called with the arguments 5 and 10, which are passed to the parameters a and b, respectively. The function then prints the sum of a and b, which is 15.

### Function Return Values

Functions can also return values. When a function returns a value, the caller can store the value in a variable or use it in some other way. Here’s an example of a function that returns a value:

<div align="left">

<figure><img src="../.gitbook/assets/image (2).png" alt="public main() {     int product;     out << &#x22;Hello World&#x22;;     let product = get_product(5, 10);     out << product; }  func get_product(int a, int b) {     return a * b; }"><figcaption></figcaption></figure>

</div>

In this example, the function get\_product takes two parameters, a and b. When the function is called, the values 5 and 10 are passed to the parameters a and b, respectively. The function then returns the product of a and b.

```
Hello World
50
```

This is the output of the program. The function get\_product is called with the arguments 5 and 10, which are passed to the parameters a and b, respectively. The function then returns the product of a and b, which is 50. The caller stores the return value in the variable product, and then prints the value of product.

### Quick Reference

| Syntax                                            | Description                                                                  |
| ------------------------------------------------- | ---------------------------------------------------------------------------- |
| `func function_name(parameter1, parameter2, ...)` | Defines a function named function\_name that takes the specified parameters. |
| `call function_name(argument1, argument2, ...)`   | Calls the function named function\_name with the specified arguments.        |
| `return expression`                               | Returns the value of the specified expression.                               |

### Quick Quiz

1. What is the output of the following program?

<div align="left">

<figure><img src="../.gitbook/assets/image (5).png" alt="public main() {     out << &#x22;Hello World&#x22;;     call print_sum(15, 10); }   func print_sum(a, b) {     out << a + b; }"><figcaption></figcaption></figure>

</div>

* a. 15&#x20;
* b. 25&#x20;
* c. 10&#x20;
* d. 5&#x20;

<details>

<summary>Answer</summary>

Answer is B because the function print\_sum is called with the arguments 15 and 10, which are passed to the parameters a and b, respectively. The function then prints the sum of a and b, which is 25.

</details>

2. What is the output of the following program?

<div align="left">

<figure><img src="../.gitbook/assets/image.png" alt="public main() {     int product;     out << &#x22;Hello World&#x22;;     let product = get_product(5, 10);     out << product; }"><figcaption></figcaption></figure>

</div>

* a. 50&#x20;
* b. 15&#x20;
* c. 5&#x20;
* d. Error

<details>

<summary>Answer</summary>

Answer is D because the function get\_product is not defined.

</details>
