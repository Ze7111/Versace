---
description: >-
  In Versace you can specify optional arguments that will be used before the
  file is transpiled.
---

# Optional Arguments

## What are the optional arguments you can use in Versace?

In Versace you can use the following optional arguments to be used during execution...

* ```java
  -*- no color -*-
  ```
* ```java
  -*- no indent -*-
  ```
* ```java
  -*- no newline -*-
  ```
* ```java
  -*- cache -*-
  ```
* ```java
  -*- py -*-
  ```
* ```java
  -*- exec -*-
  ```

Do note, they should be added to the top of the file in this format **\[\<argument>]**, you can not add more than one argument per line.

### What do each of the optional arguments do?

<details>

<summary>-*- no color -*-</summary>

This removes all color from the code you will be running.

#### Example code...

```csharp
out << "juice wrld" << bold red;
```

Without the **-\*- no color -\*-** argument the code will print - <mark style="color:red;">**juice wrld**</mark> - but with the argument it will print - juice wrld - with no color.

Same rule applies for any statement in your code that uses color/special characters such as emojis.

</details>

<details>

<summary>-*- no indent -*-</summary>

This will remove all the indentation from your transpiled/executed code and may or may not make it run depending on your use case.

</details>

<details>

<summary>-*- no newline -*-</summary>

This will allow the missing semicolon checker to work on a per line basis

Without this optional argument you can write code like this:

```csharp
public init() {
    out
    <<
    "NLE CHOPPA!"
    <<
    bold green;
}
```

The above code will <mark style="color:red;">NOT</mark> work if <mark style="color:red;"></mark> **\[-\*- no newline -\*-]** is present on the top of the file.

So the new code will look look like this:

```csharp
public init() {
    out << "NLE CHOPPA!" << bold green;
}
```

If a semi-colon is missing it will raise an error, saying missing semi-colon.

</details>

<details>

<summary>-*- py -*- </summary>

This is a slow method of execution, as it will use python to execute the transpiled code.

Error reporting will be perfect if you use this.

You should only use this when the in-built error reporter fails, or if your code does not run as expected.

This argument **CAN NOT** be used in conjunction with **-\*- exec -\*-**.

</details>

<details>

<summary>-*- exec -*-</summary>

This the fastest method of execution.&#x20;

It may not get all the errors in your code though and might make some small errors.

This argument **CAN NOT** be used in conjunction with **`-*- py -*-`**.

</details>

<details>

<summary>-*- cache -*-</summary>

This will allow caching of the output of the program, and print that if nothing has changed in the code, if there is any user input questions in the code, if you use this it will not work.

To clear the cache, if there are any problems, you can run this command:

```bash
$ versace <filename> -ctemp
```

This will clear the temp files before execution.

</details>
