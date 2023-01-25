---
description: >-
  What are Static Variables and Final Variables and how to you use them in
  Versace.
---

# Static Variables and Final Variables

<details>

<summary>What is a static variable?</summary>

A static variable finalizes a variable in a local namespace, for example if you create a variable called `int test = 10;` in a function and then declare that variable like so, `static test;` it will make the variable static meaning you cannot change the value of the variable later on in the code.

</details>

{% hint style="warning" %}
This only works for variables in that function (local variables) and not for global variables.
{% endhint %}

<details>

<summary>What is a final variable?</summary>

A final variable is a variable that cannot be changed later on in the code, for example if you create a variable called `int test = 10;` and then declare that variable like so, `final test;` it will make the variable final meaning you cannot change the value of the variable later on in the code.

</details>

{% hint style="warning" %}
This works for both local and global variables.
{% endhint %}

### How do I use static and final variables?

To use static variables, you must declare them like so:

```csharp
int test = 10;
static test;
```

To use final variables, you must declare them like so:

```csharp
int test = 10;
final test;
```

### How do I use static and final variables in functions?

To use static variables in functions you must declare them like so:

```csharp
func test() {
    int test = 10;
    static test;
}
```

To use final variables in functions you must declare them like so:

```csharp
int test = 10;
func test() {
    ref test;
    final test;
}
```
