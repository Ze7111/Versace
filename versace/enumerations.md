---
description: What are Enumerations and how to use them in Versace.
---

# Enumerations

<details>

<summary>What is an Enumeration</summary>

An enumeration is a set of named values. In Versace, an enumeration is a value type that can be assigned an integer value. The values of an enumeration are called enumerators or enum members.

</details>

{% hint style="danger" %}
Value declarations are <mark style="color:red;">**required**</mark> for enumerators.
{% endhint %}

{% hint style="info" %}
Once an enumeration is declared, the number of enumerators in it cannot be changed. However, the values of the enumerators can be changed.
{% endhint %}

### What is the difference between an enumeration and a structure?

An enumeration is having predefined values, while a structure is a user-defined type that can have any values in post runtime.

### How to declare an enumeration?

An enumeration is declared using the `enum` keyword. The following example shows how to declare an enumeration:

```swift
enum <enum name> {
    <data type> <enumerator 1> = <value 1>;
    <data type> <enumerator 2> = <value 2>;
    ...
    <data type> <enumerator n> = <value n>;
}
```

### How to use an enumeration?

An enumeration can be used in the same way as any other value type. The following example shows how to use an enumeration:

```csharp
enum Direction {
    int north = 0;
    int south = 90;
    int east = 180;
    int west = 270;
}
int direction = Direction::east;
out << direction;
// you could also use the following syntax
out << Direction::south;
```

Output of the above example:

```swift
180
90
```

### How to iterate over an enumeration?

An enumeration can be iterated by using the `for` keyword. The following example shows how to iterate over an enumeration:

```csharp
enum Direction {
    int north = 0;
    int south = 90;
    int east = 180;
    int west = 270;
}
for (key, value in Direction::__dict__::items()) {
    if not key::startswith("__") {
        out << key << value << bright_yellow;
    }
}
```

Output of the above example:

```
north 0
south 90
east 180
west 270
```

### How to get the number of enumerators in an enumeration?

The number of enumerators in an enumeration can be obtained using the `len` function. The following example shows how to get the number of enumerators in an enumeration:

```csharp
enum Direction {
    int north = 0;
    int south = 90;
    int east = 180;
    int west = 270;
}
out << len(Direction::__dict__) << bright_yellow;
```

Output of the above example:

```
9
```

{% hint style="info" %}
The above output is 9 because the `__dict__` attribute of an enumeration contains the enumerators and the `__name__` and `__module__` attributes of the enumeration.
{% endhint %}
