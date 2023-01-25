---
description: >-
  What is Declaring Variables and Assigning Variables and how to you use them in
  Versace.
---

# Declaring Variables and Changing Variables

### If you need to learn about references, go [Here](references.md).

<details>

<summary>What is a variable?</summary>

A variable is a name that refers to a value. The value can be a number, a string, a list, a dictionary, or any other type of value. The name of the variable can be any string, but there are some rules for what makes a good variable name. A variable name can contain only letters, numbers, and underscores. It can start with a letter or an underscore, but not with a number. You cannot use Python keywords or built-in function names for your variable names. You should also avoid using Python keywords and function names because they might be used in new versions of Python, which might confuse you.

</details>

{% hint style="danger" %}
You must have your variable declared before you can use it. If you try to use a variable that has not been declared, you will get an error.
{% endhint %}

{% hint style="warning" %}
Variables are case-sensitive. For example, my\_variable is not the same as My\_Variable.
{% endhint %}

{% hint style="warning" %}
Variables are in the local scope by default. This means that a variable declared inside a function is only available inside that function. To create a global variable inside a function, you can use the `ref` keyword.
{% endhint %}

### Declaring Variables

To declare a variable, you just need to give it a name. You can declare a variable without assigning it a value. In this case, the variable is said to be empty. You can assign a value to a variable using the assignment operator, =. The assignment operator assigns the value on the right to the variable on the left. The following example declares a variable named my\_variable and assigns it the value 10.

```csharp
int my_variable = 10;
```

You can declare multiple variables on the same line by separating them with commas. The following example declares three variables, a, b, and c, and assigns them the values 1, 2, and 3, respectively.

```csharp
int a, b, c = 1, 2, 3;
```

You can also assign variables without any value. The following example declares three variables, a, b, and c, but does not assign them any values.

```csharp
int a, b, c;
```

### Changing Variables

You can change the value of a variable by assigning it a new value. The following example assigns the value 20 to the variable my\_variable.

```csharp
int my_variable = 10;
let my_variable = 20;
```

You can also change the value of a variable by using the variable itself in an assignment. The following example assigns the value of the variable my\_variable to the variable your\_variable.

```csharp
int my_variable = 10;
let your_variable = my_variable;
```

### Variable Types

Variables can be of different types. The type of a variable determines what kind of value it can hold. The following table lists the different types of variables in Python.

| Type       | Description                                                                         |
| ---------- | ----------------------------------------------------------------------------------- |
| int        | An integer number. For example, 1, 2, 3, 4, 5, etc.                                 |
| float      | A floating-point number. For example, 1.0, 2.5, 3.14, etc.                          |
| bool       | A boolean value. Either True or False.                                              |
| str        | A string. For example, "Hello", "World", etc.                                       |
| list       | A list of values. For example, \[1, 2, 3], \["Hello", "World"], etc.                |
| dict       | A dictionary of values. For example, {"name": "John", "age": 30}, etc.              |
| set        | A set of values. For example, {1, 2, 3}, {"Hello", "World"}, etc.                   |
| tuple      | A tuple of values. For example, (1, 2, 3), ("Hello", "World"), etc.                 |
| tuple      | A tuple of values. For example, (1, 2, 3), ("Hello", "World"), etc.                 |
| complex    | A complex number. For example, 1 + 2j, 1.5 + 2.5j, etc.                             |
| NULL       | A null value. The value None is used to represent a null value which is equal to 0. |
| array      | An array of values. For example, \[1, 2, 3], \["Hello", "World"], etc.              |
| double     | A double-precision floating-point number. For example, 1.0, 2.5, 3.14, etc.         |
| usize      | An unknown size object that can be used to store any type of value.                 |
| bytes      | A sequence of bytes. For example, b"Hello", b"World", etc.                          |
| char       | A single character. For example, 'a', 'b', 'c', etc.                                |
| memoryview | A memory view of a bytes-like object.                                               |
| bytearray  | A mutable sequence of bytes. For example, b"Hello", b"World", etc.                  |
| range      | A sequence of numbers. For example, range(0, 10), range(10), etc.                   |
| NULLTYPE   | A null type. The value None is used to represent a null value which is equal to 0.  |
