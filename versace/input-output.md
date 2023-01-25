---
description: What is Input/Output and how to you use them in Versace.
---

# Input/Output

<details>

<summary>What is input?</summary>

Input is the data that is fed into the program. It is the data that the program will use to do its job. Input is usually given to the program by the user. The user can give input in many ways, such as by typing it into the command line, or by selecting it from a menu. The program will then use this input to do its job.

</details>

<details>

<summary>What is output?</summary>

Output is the data that is produced by the program. It is the data that the program has produced after it has done its job. Output is usually given to the user by the program. The user can then use this output in many ways, such as by reading it, or by using it to do something else. The program will then use this output to do its job.

</details>

<details>

<summary>How do I get input from the user?</summary>

In Versace the main way to get inputs is the in following format:

```
in <variable name> << <prompt> << <any other argument you can use for out> << <OPTIONAL: data type>;
```

The variable name is the name of the variable that you want to store the input in. The prompt is the text that will be displayed to the user. The data type is the data type that you want the input to be. The data type can be any of the following:

* int
* float
* str
* bool
* list
* dict
* set
* tuple
* complex
* usize
* NULL

</details>

<details>

<summary>How do I output data to the user?</summary>

In Versace the main way to output data is the out following format:

```
out << <anything>;
```

The anything can be any data type, including variables, strings, numbers, lists, etc. The anything can also be a function call, such as `out << len("Hello World");`. The anything can also be a variable, such as `out << myVar;`.

</details>

{% hint style="info" %}
You can <mark style="color:red;">**NOT**</mark> specify a data type for outputs.
{% endhint %}

### How do I get input from a file?

In Versace the main way to get inputs from a file is the in following format:

```csharp
with open(<file name>, <mode>) as <file variable name>:
    <code>
```

The file name is the name of the file that you want to open. The mode is the mode that you want to open the file in. The mode can be any of the following:

| Mode | Description                                                       |
| ---- | ----------------------------------------------------------------- |
| r    | opens the file in read mode (not editable)                        |
| w    | opens the file in write mode (overwrites the file)                |
| a    | opens the file in append mode (adds to the end of the file)       |
| r+   | opens the file in read and write mode                             |
| w+   | opens the file in read and write mode                             |
| a+   | opens the file in read and write mode                             |
| rb   | opens the file in read bytes mode (not editable)                  |
| wb   | opens the file in write bytes mode (overwrites the file)          |
| ab   | opens the file in append bytes mode (adds to the end of the file) |
| rb+  | opens the file in read and write bytes mode                       |
| wb+  | opens the file in read and write bytes mode                       |
| ab+  | opens the file in read and write bytes mode                       |

### How do I redirect console output to a file?

Work in progress

### Examples

```csharp
in myVar << "Enter a number: " << int;
out << myVar;
```

```csharp
with open("test.txt", "r") as f:
    out << f::read();
```

```csharp
with open("test.txt", "w") as f:
    let f::write("Hello World");
```

```csharp
with open("test.txt", "a") as f:
    let f::write("Hello World");
```

```csharp
int myVar = 5;
out << myVar;

in myVar << "Enter a number: " << int;
out << myVar << "Changed";

with open("test.txt", "w") as f:
    let f::write(f"myVar = {myVar}");
```
