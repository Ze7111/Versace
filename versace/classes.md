---
description: What are classes and how to you use them in Versace.
---

# Classes

<details>

<summary>What is a class?</summary>

A class is a blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). The user-defined objects are created using the class keyword.

</details>

<details>

<summary>Class definition syntax</summary>

A class definition begins with the class keyword, which is followed by the name of the class and a colon. The class body is indented below the class definition line. The body can contain class methods and data attributes. The class body is terminated by a line containing only an unindented pass statement, which does nothing.

</details>

{% hint style="warning" %}
if you are creating a variable that has a **`,`** outside of a string, an error will be thrown. To fix this, you can use **`|`** instead of **`,`** separate objects.
{% endhint %}

### How to define a class in Versace?

```csharp
class ClassName {
    pass;
}
```

### How to create an object in Versace?

```csharp
class ClassName {
    pass;
}
usize someObject = ClassName();
```

### How to create a class with a constructor?

```csharp
class ClassName {
    func __init__(self | usize arg1 | usize arg2) {
        let self::arg1 = arg1;
        let self::arg2 = arg2;
    }
}
```

### How to create a class with a method?

```csharp
class ClassName {
    func __init__(self | usize arg1 | usize arg2) {
        let self::arg1 = arg1;
        let self::arg2 = arg2;
    }
    func someMethod(self) {
        pass;
    }
}
```

### Example

```csharp
class Person {
    func __init__(self | usize name | usize age) {
        let self::name = name;
        let self::age = age;
    }
    func sayHello(self) {
        out << "Hello, my name is" << self::name << "and I am" << self::age << "years old.";
    }
}
usize person = Person("John" | 20);
person::sayHello();
```

Output:

```
Hello, my name is John and I am 20 years old.
```
