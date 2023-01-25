---
description: What are public functions and why are they useful in Versace.
---

# Public Functions

<details>

<summary>What are Public Functions</summary>

A public function is a function that can be called from outside the module. Public functions are declared using the `public` keyword. They also do not expect any parameters. If you do pass parameters to a public function, it will throw an error.

</details>

### What are the 3 types of public functions?

There are 3 types of public functions:

* `init` - This function is called when the file completes execution. The placement of this function is very important. Due to the fact that this function is called right after the place where the function is declared, it is important to place this function at the top of the file.
* `update` - This function is called every cpu clock. The placement of this function is also very important. Due to the fact that this function is called right after the place where the function is declared, it is important to place this function at the top of the file.
* `close` - This function is called right before the file completes execution.

### What are the other types of public functions?

Regular public functions are functions that are not `init`, `update`, or `close`. These functions act like normal functions. But they do not expect any parameters. If you do pass parameters to a regular public function, it will throw an error.

### Can I have the 3 types of public functions and regular functions with the same name?

Yes, you can have the 3 types of public functions and regular functions with the same name. It does not matter which of the 3 you have, you can still make a regular function with the same name. This is because the public functions are overloaded. This means that only these 3 public functions will not be called when you call the regular function. The regular function will be called instead.

### Examples

```csharp
// This is a public init function
public init() {
    out << "This runs where it is declared";
}
```

```csharp
// This is a public update function
public update() {
    out << "This runs on continuous loop";
}
```

```csharp
// This is a public close function
public close() {
    out << "This runs right before the file completes execution";
}
```

```csharp
// This is a regular public function
public function() {
    out << "This runs when it is called like a normal function";
}
```

```csharp
// This is a public init function and a regular function with the same name
public init() {
    out << "This runs where it is declared";
}
func init() {
    out << "This runs when it is called, and will not call the public init function";
}
init();
```

Example Program:

```csharp
int count = 0;
out << "This is a example program for public functions" << bright_blue;
public init() {
    out << "runs first" << bright_blue;
}

public close() {
    out << "runs last";
}

public update() {
    ref count;
    let count += 1;
    out << count << " Runs every clock" << bright_red;
}
func init() {
    out << "This runs when it is called, and will not call the public init function";
}
init();
```

Output:

```
This is a example program for public functions
runs first
1  Runs every clock
This runs when it is called, and will not call the public init function
2  Runs every clock
runs last
3  Runs every clock
```

{% hint style="info" %}
The colors are not shown in the example output here, but if you run that program, there are colors.
{% endhint %}
