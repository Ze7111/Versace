---
description: Explains what are structures.
---

# Structures

<details>

<summary>What are structures?</summary>

Structures are data types that can be used to group data of different types. They are similar to arrays, but they can contain data of different types. Structures are defined using the `struct` keyword.

</details>

{% hint style="danger" %}
You can <mark style="color:red;">**NOT**</mark> call an entire structure; you can only call a specific variable from a structure.
{% endhint %}

{% hint style="info" %}
Variables in structures can be modified more than once.
{% endhint %}

### What is the difference between a structure and an enumeration?

A structure is a user-defined type that can have any values in post runtime, while an enumeration is has predefined values.

### Defining a structure

A structure is defined using the following syntax:

```c
struct <structure name> {
    <data type> <variable name>;
    <data type> <variable name>;
    ...
    <data type> <variable name>;
};
```

For example, the following code defines a structure named `person`:

```csharp
struct person {
    str name;
    int age;
    float height;
};
```

### Calling a specific variable from a structure

Before you can call a variable from a structure, you must first define the structure. You can then call a specific variable from a structure using the following syntax:

```c
<structure name>::<variable name>;
```

For example, the following code calls the `name` variable from the `person` structure:

```csharp
struct person {
    str name;
    int age;
    float height;
};
out << person::name;
```

### How to define a structure?

To define a structure, you must first define the structure using the `struct` keyword. You can then define the structure using the following syntax:

```c
struct <structure name> {
    <data type> <variable name>;
    <data type> <variable name>;
    ...
    <data type> <variable name>;
};
```

For example, the following code defines a structure named `person` and we will add the name `John`, age `20` and height `1.8` to the structure:

```csharp
struct person {
    str name;
    int age;
    float height;
};
let person::name = "John";
let person::age = 20;
let person::height = 1.8;
out << person::name << "is" << person::age << "years old and is" << person::height << "meters tall.";
```

Output of the above code is as follows:

```
John is 20 years old and is 1.8 meters tall.
```
