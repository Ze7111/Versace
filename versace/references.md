---
description: What are References and how to you use them in Versace.
---

# References

<details>

<summary>What is a reference?</summary>

A reference is keyword that allows a variable outside the local namespace to be modified in the local namespace, thats why its called a reference. It just references the variable outside the local namespace.

</details>

{% hint style="danger" %}
You can <mark style="color:red;">**NOT**</mark> reference a variable that is not declared. Or any of these types, functions, classes, etc.
{% endhint %}

{% hint style="warning" %}
You can reference a variable outside the local namespace, but you can <mark style="color:red;">**NOT**</mark> reference a variable inside the local namespace.
{% endhint %}

### How to use a reference?

To use a reference, you need to use the `ref` keyword before the variable name. For example:

```csharp
int a = 5;
func test() {
    ref a;
    let a = 10;
}
```

In this example, the variable `a` is referenced, and then the value of `a` is changed to 10. This is because the variable `a` is referenced, and the value of `a` is changed in the local namespace. This is useful for when you want to change a variable outside the local namespace, but you don't want to use a global variable.
