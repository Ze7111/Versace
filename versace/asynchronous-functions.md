---
description: What are Asynchronous Functions and how to you use them in Versace.
---

# Asynchronous Functions

<details>

<summary>What is an asynchronous function?</summary>

An asynchronous function is a function that runs in the background and does not block the main thread. This means that the main thread can continue to run while the asynchronous function is running. This is useful for tasks that take a long time to complete, such as downloading a file from the internet.

</details>

{% hint style="info" %}
Asynchronous Functions work in the same namespace as the rest of the program so you can reference a variable used elsewhere in the code through `async`
{% endhint %}

### How to create an asynchronous function

To create an asynchronous function, you must use the `async` keyword before the function name. For example:

```csharp
async func <name>() {
    // Do something
}
```

You can not specify a return type for an asynchronous function. Instead, you must use the `await` keyword to wait for the asynchronous function to complete. For example:

```csharp
int count = 0;
async func someFunction() {
    ref count;
    for (int i = 0 | i < 100 | i++) {
        let count += 1;
        out << count << "count from someFunction";
    } 
}

await someFunction();
// The code below will not run until the asynchronous function has completed
await someFunction();
```

### How to use the `await` keyword

The `await` keyword is used to wait for an asynchronous function to complete. You can not `await` more than one asynchronous function at a time for example:

```csharp
await someFunction(), someOtherFunction();
```

will not work. You must use the `await` keyword for each asynchronous function. For example:

```csharp
await someFunction();
await someOtherFunction();
```

You cannot use the await keyword inside of an asynchronous function.

### There is a more complicated version of await called coroutines, you can find it [Here](coroutines.md).
