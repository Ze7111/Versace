---
description: This explains how/what type annotations are.
---

# Type annotations

<details>

<summary>What are type annotations?</summary>

Type annotations are used to enforce type checking. They are used to specify the type of a variable, function parameter, or function return value. Type annotations are required, because they are used to generate the type of information that is used by the type checker.

</details>

<details>

<summary>Type annotations in Versace</summary>

* **int**, integer value
* **float**, floating point value
* **complex**, complex value&#x20;
* **double**, double value
* **str**, string&#x20;
* **usize**, unknown type
* **bool**, boolean list,&#x20;
* **list**, (mutable, ordered)&#x20;
* **tuple**, (immutable, ordered)&#x20;
* **dict**, (mutable, unordered)&#x20;
* **set**, (mutable, unordered)&#x20;
* **bytes**, bytes string
* **char**, a single character
* **memoryview**, memory view&#x20;
* **bytearray**, byte array&#x20;
* **null**, null Type

</details>

{% hint style="danger" %}
Type annotations are required in Versace.
{% endhint %}

#### Type annotations are written like this...

```swift
type var_name = value
```

The type can be any valid type, including other variables, functions, and classes.\
You can also declare multiple variables at once by separating them with commas, you need the same number of values as to variables or none.

#### Here is an example of using an int type annotation...

```csharp
int myInt = 5
```

Try changing the value of myInt to a string, like this...

```csharp
int myInt = "hello"
```

You should see the error message

<mark style="color:red;">`Expected`</mark>` `<mark style="color:yellow;">`Integer`</mark>` `<mark style="color:red;">`value, but got`</mark>` `<mark style="color:yellow;">`String`</mark>` `<mark style="color:red;">`value instead`</mark>

This error message means that you tried to assign a string to a variable that is supposed to be an integer. This is a type error, and it will cause the program to crash. This type of error is called a "type mismatch" and will show up whenever there is a type of assignment error.

If you want to use a variable that's type is unknown to you, you can use the "usize" type. "usize" stands for "undefined size", and it is used for variables whom's data type is not known yet.

#### To assign a callable to a variable, you can use the "object" type. Here is a simple example...

```csharp
func Thisfunc() {
    out << "hello world";
}

usize SomeOtherName = Thisfunc;
SomeOtherName();
```

This code will print "hello". This is because the variable SomeOtherName is assigned to the function ThisFunction. When you call SomeOtherName(), it calls ThisFunction.

{% hint style="info" %}
Remember that you can call a function by adding parentheses after it.
{% endhint %}

### Return type specified functions

Versace has support for a specfic return type functions for example:

```csharp
int func Thisfunc() {
    int something = 19;
    out << something;
    let something += 1;
    return something;
}
```

This function basically specifies that it will return an integer value to the compiler, though if that value that's returned does not match the specified type, an error will be raised.

### Type annotations allowed in Versace (with examples)

| Type       | Description                             | Example                                           |
| ---------- | --------------------------------------- | ------------------------------------------------- |
| int        | Integer                                 | `int my_int = 5;`                                 |
| float      | Float                                   | `float my_float = 5.0;`                           |
| complex    | Complex                                 | `complex my_complex = 5 + 5i;`                    |
| double     | Double                                  | `double my_double = 5.0;`                         |
| str        | String                                  | `str my_str = "hello";`                           |
| usize      | Unknown types, usefull for polymorphism | `usize my_usize = <anything>;`                    |
| bool       | Boolean                                 | `bool my_bool = True;`                            |
| list       | List (mutable, ordered)                 | `list my_list = list(1, 2, 3);`                   |
| tuple      | Tuple (immutable, ordered)              | `tuple my_tuple = tuple(1, 2, 3);`                |
| dict       | Dictionary (mutable, unordered)         | `dict my_dict = dict("a" = 1, "b" = 2, "c" = 3);` |
| set        | Set (mutable, unordered)                | `set my_set = set(1, 2, 3);`                      |
| bytes      | Bytes                                   | `bytes my_bytes = b"hello";`                      |
| char       | Character                               | `char my_char = 'a';`                             |
| memoryview | Memory view                             | `memoryview my_memoryview = memoryview(func);`    |
| bytearray  | Byte array                              | `bytearray my_bytearray = bytearray(b"hello");`   |
| null       | NullType                                | `null my_null_object = null;`                     |

