---
description: What are Modules and how to you use them in Versace.
---

# Including Modules and plug-ins

<details>

<summary>What is a module?</summary>

A module is a file that contains code to do a very specifc task. For example, the module `math` contains code to do math operations. Modules are imported using the `include` keyword.

</details>

{% hint style="warning" %}
The`include` keyword does look for files in the relative directory to the file you are working on, it also looks in the default python plug-ins directory, and the default Versace include directory.
{% endhint %}

### What are the 4 types of include supported in Versace?

#### 1. `include "python module";`

This is used to import a python module. For example, `include "math";` will import the python module `math`. This is the most common type of include.

#### 2. `include "versace file";`

This is used to import a Versace file. For example, `include "main.v";` will import the Versace file `main.v`. This is the second most common type of include.

#### 3. `include "python file";`

This is used to import a python file. For example, `include "main.py";` will import the python file `main.py`. This is the least common type of include.

#### 4. `include "versace header";`

This is used to import a Versace headder file. For example, `include "main.h";` will import the Versace module `main`. This is the least common type of include.

### How to include a specific function from a module?

You can include a specific function from a module by using the `from` keyword. For example, `include "sqrt" from "math";` will import the function `sqrt` from the module `math`. You can also import multiple functions from a module by separating them with a comma. For example, `include "sqrt, pow" from "math";` will import the functions `sqrt` and `pow` from the module `math`.

### How to change the name of a function when importing it?

You can change the name of a function when importing it by using the `as` keyword. For example, `include "sqrt" from "math" as "square_root";` will import the function `sqrt` from the module `math` and change its name to `square_root`. You can also change the name of multiple functions when importing them by separating them with a comma. For example, `include "sqrt" from "math" as "square_root";` will import the functions `sqrt` and `pow` from the module `math` and change their names to `square_root` and `power` respectively.

### Example

```csharp
include "math";
include "sqrt" from "math";
include "sqrt" from "math" as "square_root";
out << math::sqrt(4);
out << sqrt(4);
out << square_root(4);
```

{% hint style="danger" %}
You can <mark style="color:red;">**NOT**</mark> change the name of anything when importing it from a Versace file or a python file. You can only change the name of a function when importing it from a Versace header file or a python module.
{% endhint %}

{% hint style="danger" %}
You can <mark style="color:red;">**NOT**</mark> specify a specific function from a Versace file or a python file.
{% endhint %}
