---
description: This describes overloading and how to overload functions in Versace.
---

# Overloading

<details>

<summary>What is Overloading Functions?</summary>

Overloading is when you can have multiple functions with the same name, but different parameters.

</details>

### Overloading functions

You can overload functions by using the `overload` method. This is an example of overloading the `add` function:

```swift
@overload(int, int);
int func add(int a | int b) {
    return a + b;
}

@overload(str, str);
str func add(str a | str b) {
    return f"{a} {b}";
}

out << add(1, 2) << bright_blue;
out << add("hello", "world");
```

The output you will see is:

```swift
3
hello world
```

### What is the difference between overloading and overriding?

Overloading is when you overload a function. Overriding is when you override a function.

{% hint style="warning" %}
NOTE: Currently, you can overload only functions in Versace, I am working on adding support to overloading classes, structs, enums, and more.
{% endhint %}
