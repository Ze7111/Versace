---
description: What are Methods and how to you use them in Versace.
---

# Methods

<details>

<summary>What is a Method?</summary>

A Method is a function that takes a function as an argument and returns a function. It is used to modify the behavior of the function it takes as an argument. It is a way to wrap a function in another function. It is a way to modify the behavior of a function without modifying the function itself.

</details>

<details>

<summary>Why use a Method?</summary>

Methods are used to modify the behavior of a function without modifying the function itself. This is useful when you want to use the same function in multiple places but with different behaviors. For example, you may want to use the same function to calculate the area of a circle, but you may want to use it to calculate the area of a square as well. You could create a function for each shape, but that would be a lot of duplicate code. Instead, you can create a method that takes a function as an argument and returns a function. This way, you can use the same function to calculate the area of a circle and the area of a square.

</details>

{% hint style="danger" %}
You can <mark style="color:red;">**NOT**</mark> specify data types in the arguments that go in methods.
{% endhint %}

### How to use a Method?

In Versace to create a method, you have to use the `method` keyword, they take in an argument of a function, this is the format of a method in Versace:

```
method (<arguments to provide into the method> | <arguments from the function>) {
    // code
}
```

By default, the arguments from the function will always have an unpacked version of all arguments and keywords from the function.

### Example

```swift
method someMethod(fun | a, b) {
    out << a + b*2 << "This is a method";
    fun(a, b);
}

@someMethod
func someFunction(a, b) {
    out << a + b << "This is a function";
}

someFunction(1, 2);
```

Output:

```
5 This is a method
3 This is a function
```

### Example 2

```swift
method someMethod(fun) {
    // some operations
    fun(~args);
} 

@someMethod(str)
func someFunction(a, b) {
    out << a + b << "This is a function";
}

someFunction(1, 2);
```

Output:

```
5 This is a method
3 This is a function
```

This is the same as the previous example, but instead of unpacking the arguments, we are using the `~args` unpacking operator to unpack the arguments from the function. You can also use the \~\~k`wargs` unpacking operator to unpack the keywords from the function.
