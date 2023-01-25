---
description: What the most basic type of Functions are in Versace
---

# Functions

### If you needed to learn about overloading functions, go [Here](overloading.md#overloading-functions).

### If you need to learn about private functions, go [Here](private.md#what-is-a-private-function).

### If you need to learn about public functions, go [Here](public-functions.md).

{% hint style="warning" %}
The return type is optional. If you don't specify a return type, the function will still allow for any returns, but if you do specify a return type it improves the readability of the code.
{% endhint %}

<details>

<summary>What is a Function?</summary>

A function is a block of code that performs a specific task. Functions are used to perform certain actions, and they are executed when something invokes them (calls them).

</details>

<details>

<summary>Why use functions?</summary>

Functions are used to perform certain actions, and they are executed when something invokes them (calls them). You can use the same code many times with different arguments, to produce different results.

</details>

### How to create a function?

TO create a function in Versace, you need to use the `func` keyword. The syntax is as follows:

```go
func <nameOfFunction>(<arguments>) {
    // code to be executed
}
```

### How to call a function?

To call a function, you need to use the function name followed by parentheses. The syntax is as follows:

```cpp
<nameOfFunction>(<arguments>)
```

### Example

```csharp
func sayHello() {
    out << "Hello, World!";
}
sayHello();
```

### Example with arguments

```csharp
func sayHello(str name) {
    out << "Hello, " << name << "!";
}
sayHello("John");
```

### Example with return value

```csharp
func add(int a, int b) {
    return a + b;
}
out << add(1, 2);
```

### Example with a specified return type

```csharp
int func add(int a, int b) {
    return a + b;
}
out << add(1, 2);
```
