---
description: What are Loops and how to you use them in Versace.
---

# Loops

<details>

<summary>What is a loop?</summary>

A loop is a way to repeat a block of code a certain number of times. There are there types of loops in Versace: `for` loops, `while` loops, and another type of `for` loop. The `for` loop is used when you know how many times you want to repeat a block of code. The `while` loop is used when you don't know how many times you want to repeat a block of code.

</details>

{% hint style="warning" %}
The `|` symbol is used to separate the three parts of the for loop.
{% endhint %}

### For loops

In Versace, there are two types of `for` loops: the first type is the regular Python like for loop, the other is C++ like for loop. Example:

```csharp
for (i in range(10)) {
    out << i;
}
```

This will print out the numbers 0 to 9. The second type of `for` loop is the C++ like for loop. This is used when you want to loop through a list. Example:

```csharp
for (int i = 0 | i != 10 | i++) {
    out << i;
}
```

This will also print out the numbers 0 to 9.

{% hint style="success" %}
The second type of `for` loop is quicker than a regular `for` loop.
{% endhint %}

### While loops

A while loop is used when you don't know how many times you want to repeat a block of code. Example:

```csharp
int i = 0;
while (i < 10) {
    out << i;
    i += 1;
}
```

This will also print out the numbers 0 to 9.

### For each loops

A for each loop is used when you want to loop through a list. Example:

```csharp
for (i in [1, 2, 3, 4, 5]) {
    out << i;
}
```

This will print out the numbers 1 to 5.

### Break and continue

The `break` keyword is used to stop a loop. Example:

```csharp
for (int i = 0 | i != 10 | i++) {
    if (i == 5) {
        break;
    }
    out << i;
}
```

This will print out the numbers 0 to 4. The `continue` keyword is used to skip the current iteration of a loop. Example:

```csharp
for (int i = 0 | i != 10 | i++) {
    if (i == 5) {
        continue;
    }
    out << i;
}
```

This will print out the numbers 0 to 4 and 6 to 9.

### Nested loops

A nested loop is a loop inside of a loop. Example:

```csharp
for (int i = 0 | i != 10 | i++) {
    for (int j = 0 | j != 10 | j++) {
        out << i << j;
    }
}
```

This will print out the numbers 0 to 99.

### Looping through a string

You can loop through a string by using a for loop. Example:

```csharp
for (i in "Hello") {
    out << i;
}
```

This will print out the letters H, e, l, l, and o.

### Looping through a dictionary

You can loop through a dictionary by using a for loop. Example:

```csharp
for (i in {"a": 1, "b": 2, "c": 3}) {
    out << i;
}
```

This will print out the keys a, b, and c.
