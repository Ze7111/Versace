---
description: This post will teach you how to create a simple program in Versace.
---

# Creating your first program

## Let's create a simple "Hello, World" program in Versace

Before getting started, make sure you have completed the [**Installation** ](../getting-started/installation.md)process.

1. Open your code editor if you are using [**VS Code** ](https://code.visualstudio.com/download)with my [**extension** ](https://marketplace.visualstudio.com/items?itemName=ZE7111.Versace)installed you can follow along these steps to get your editor set up.
2. Create a new file ending with `.v`
3. Press (`ctrl + shit + p` -> `Change Language Mode`) and find `Versace`
4. Now that you have the correct syntax highlighting, open the file you have just created.
5. Paste the following code in:
6.  {% code title="helloworld.v" %}
    ```cpp
    public init() {
        out << "hello, world" << bold green;
    }
    ```
    {% endcode %}


7. Now open the terminal and type in the following:
8. ```
   versace.exe helloworld.v -exec
   ```

{% hint style="success" %}
You should see <mark style="color:green;">**hello world**</mark> in your terminal.
{% endhint %}

{% hint style="warning" %}
If you do not see what is listed above, please try the [**Installation** ](../getting-started/installation.md)process again..
{% endhint %}
