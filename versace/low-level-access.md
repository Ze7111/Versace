---
description: What is Low Level Access and how to you use them in Versace.
---

# Low Level Access

{% hint style="success" %}
Versace does have support for low level capability.
{% endhint %}

<details>

<summary>What is Low Level Access?</summary>

Low level access is the ability to access the hardware of a computer directly. This is done by writing code that directly interacts with the hardware. This is in contrast to high level languages, which are designed to abstract away the hardware and allow the programmer to focus on the problem at hand. Low level languages are often used for performance critical applications, such as games, or for applications that require direct access to the hardware, such as drivers.

</details>

<details>

<summary>Why use Low Level Access?</summary>

Low level access is useful for a number of reasons. The first is that it allows you to write code that is very close to the hardware. This means that you can write code that is very fast, and that is very efficient. This is useful for applications that require a lot of processing power, such as games. The second reason is that it allows you to write code that is very portable. This means that you can write code that will run on any computer, regardless of the hardware that it has. This is useful for applications that require a lot of processing power, such as games. The third reason is that it allows you to write code that is very portable. This means that you can write code that will run on any computer, regardless of the hardware that it has. This is useful for applications that require a lot of processing power, such as games.

</details>

### What Low Level access is available in Versace?

Versace has the ability to allocate and deallocate memory, along with access to make Signed or Unsigned Integers/Floats.

| Data Type | Description     | Signed/Unsigned |
| --------- | --------------- | --------------- |
| i8        | 8-bit integer   | Signed          |
| u8        | 8-bit integer   | Unsigned        |
| i16       | 16-bit integer  | Signed          |
| u16       | 16-bit integer  | Unsigned        |
| i32       | 32-bit integer  | Signed          |
| u32       | 32-bit integer  | Unsigned        |
| i64       | 64-bit integer  | Signed          |
| u64       | 64-bit integer  | Unsigned        |
| i128      | 128-bit integer | Signed          |
| u128      | 128-bit integer | Unsigned        |
| f32       | 32-bit float    | Signed          |
| f64       | 64-bit float    | Signed          |

### How do I use Low Level Access?

In Versace You can allocate memory by using the `alloc` keyword like follows:

```cs
alloc(10); // Allocates 10 MB of memory
```

You can deallocate memory by using the `dealloc` keyword like follows:

{% code fullWidth="false" %}
```cs
dealloc(5); // Deallocates 5 MB out of the 10 MB allocated
dealloc(); // Deallocates all allocated memory
```
{% endcode %}

{% hint style="danger" %}
You can <mark style="color:red;">**NOT**</mark> allocate more memory then is available on the computer. If you try to allocate more memory then is available, it will throw an error. This also happens Vice Versa, if you try to deallocate more memory then is allocated, it will throw an error.
{% endhint %}

You can make a Signed or Unsigned Integer/Float by using the data type like follows:

```cs
i32 a = 10; // Makes a signed 32 bit integer
u32 b; // Makes a unsigned 32 bit integer
f32 c = 10.5; // Makes a signed 32 bit float
```

You can change the value of a Signed or Unsigned Integer/Float by using the `let` keyword (this applies to all variables) like follows:

{% hint style="danger" %}
You can <mark style="color:red;">**NOT**</mark> assign a value to an unsigned integer while declaring it. This is because they are unsigned, and therefore cannot be negative. If you try to assign a value to any unsigned integer, it will throw an error.
{% endhint %}

```cs
let a = 11; // Changes the value of a to 10
```
