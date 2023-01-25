---
description: What are constants and how to you use them in Versace.
---

# Constants

<details>

<summary>What is a constant?</summary>

A constant is a variable that cannot be changed. It is a value that is set once and never changes. Constants are defined using the `const` keyword.

</details>

{% hint style="info" %}
Constants must be initialized when they are defined. They cannot be initialized later in the program.
{% endhint %}

{% hint style="info" %}
Constants require a vaule and data type to be defined. They cannot be left undefined.
{% endhint %}

### Defining a constant

A constant is defined using the `const` keyword. The syntax is as follows:

```csharp
const <data type> <name> = <value>;
```

### Example

```csharp
const int x = 5;
```

Constants can be used in the same way as variables. The only difference is that they cannot be changed. They can also be accessed from anywhere in the program regardless of the local namespace they were defined in.

```csharp
const float x = 3.69;
out << x << "is a constant"
func somefunctions() {
    out << x << "This is calling the constant from a function";
}
somefunctions();
```
