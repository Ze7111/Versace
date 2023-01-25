---
description: What are Coroutines and how to you use them in Versace.
---

# Coroutines

### To use coroutines you must have a complete understanding of [Asynchronous Functions](asynchronous-functions.md).

<details>

<summary>What are coroutines?</summary>

In Versace, coroutines are a way to run multiple functions at the same time. They are similar to threads, but they are much lighter and easier to use.

</details>

{% hint style="danger" %}
You can <mark style="color:red;">**NOT**</mark> use coroutines and await.
{% endhint %}

### How do I use them?

In order to use coroutines, you must first create an `async` function. This is done by adding the `async` keyword before the function name. For this section, we will use the following code:

```csharp
async func myFunction() {
    // code
}

async func myFunction2() {
    // code
}
 
async func myFunction3() {
    // code
}
```

Once you have created more than 1 `async` functions (1 is ok but coroutines are better with more), you can use the `coroutine` keyword to create a coroutine. For example:

```csharp
coroutine myFunction() | myFunction2();
```

There are 2 ways to execute coroutines, the first is to use the `coroutine exec()` keyword. This will execute all the coroutines at the same time. For example:

```csharp
coroutine myFunction() | myFunction2();
coroutine exec();
```

The second way to execute coroutines is to use the `coroutine exec(<function name> | ...)` keyword. This will execute only the coroutines you specify. For example:

```csharp
coroutine myFunction() | myFunction2() | myFunction3(); 
coroutine exec(myFunction() | myFunction2());
```

### How do I clear coroutines?

For this section, we will use the following code:

```csharp
async func myFunction() {
    // code
}

async func myFunction2() {
    // code
}
 
async func myFunction3() {
    // code
}
```

In order to clear coroutines, you must use the `coroutine clear()` keyword. This will clear all the coroutines. For example:

```csharp
coroutine myFunction() | myFunction2() | myFunction3(); 
coroutine exec(myFunction() | myFunction2());
coroutine clear();
```

You can also clear specific coroutines by using the `coroutine delete(<function name> | ...)` keyword. For example:

```csharp
coroutine myFunction() | myFunction2() | myFunction3(); 
coroutine exec(myFunction() | myFunction2());
coroutine delete(myFunction());
```

### How do I automatically clear coroutines?

In order to automatically clear coroutines, you must use the `coroutine auto_clear = True;` keyword. This will automatically clear all the coroutines that executes.

{% hint style="danger" %}
You can <mark style="color:red;">**NOT**</mark> use `auto_clear`after you have set coroutines to execute.
{% endhint %}
