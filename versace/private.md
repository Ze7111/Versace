---
description: What are privates in Versace
---

# Private

<details>

<summary>What is a Private Object?</summary>

A private object is an object that is not visible to other objects in the local namespace. It is only visible in the local namespace it was created in. Private objects are created by using the `priv` keyword.

</details>

<details>

<summary>How to access a private variable?</summary>

In Versace you can only output a private object to the console. You cannot use it in any other way. I am working on a way to access private objects with other ways.

</details>

<details>

<summary>How to access a private function?</summary>

&#x20;In Versace you can only output a private function to the console. You can not use it in any other way. I am working on a way to access private functions with other ways.

</details>

{% hint style="danger" %}
In Versace if you are declaring a private you can <mark style="color:red;">**NOT**</mark> add a type to it. It will automatically be set to the type of the value you are assigning to it.
{% endhint %}

### How to create a private variable?

```rust
priv somevar = 5
```

### What is a private function?

A private function is a function that is not visible to other objects in the local namespace. It is only visible in the local namespace it was created in. Private functions are created by using the `priv` keyword. They can only be called from within the local namespace they were created in. They cannot be called with anything other than outputting them to the console.

### How to create a private function?

```rust
// using no specific return type
priv func myPrivateFunction() {
    out << "Hello World!";
}
out << myPrivateFunction();

// using a specific return type
priv str func myPrivateFunction() {
    out << "Hello World!";
    return "Hello";
}
out << myPrivateFunction();
```

Output of the above code:

```
Hello World!
Hello World!
Hello
```

{% hint style="info" %}
In Versace if you are declaring a private function, you can add a type to it.
{% endhint %}
