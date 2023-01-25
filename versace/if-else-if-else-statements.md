---
description: What are If, else if, else statements and how to you use them in Versace.
---

# If, else if, else Statements

<details>

<summary>What is an if statement?</summary>

An if statement is a conditional statement that executes a block of code if a condition is true. If the condition is false, the block of code will not be executed.

</details>

<details>

<summary>What is an else if statement?</summary>

An else if statement is a conditional statement that executes a block of code if the previous if or else if statement is false and the condition is true. If the condition is false, the block of code will not be executed.

</details>

<details>

<summary>What is an else statement?</summary>

An else statement is a conditional statement that executes a block of code if the previous if or else if statement is false. If the condition is true, the block of code will not be executed.

</details>

### How to use if, else if, else statements

```csharp
if (condition)
{
    // Code to execute if condition is true
}
else if (condition)
{
    // Code to execute if condition is true
}
else
{
    // Code to execute if condition is false
}
```

#### Example

```csharp
int x = 5;
int y = 10;

if (x > y) {
    out << "x is greater than y";
} else if (x < y) {
    out << "x is less than y";
} else {
    out << "x is equal to y";
}
```

### How to use if, else if, else statements with multiple conditions

```csharp
if (condition1 && condition2)
{
    // Code to execute if condition1 and condition2 are true
}
else if (condition1 || condition2)
{
    // Code to execute if condition1 or condition2 is true
}
else
{
    // Code to execute if condition1 and condition2 are false
}
```

#### Example

```csharp
int x = 5;
int y = 10;

if (x > 0 && y > 0) {
    out << "x and y are positive";
} else if (x > 0 || y > 0) {
    out << "x or y is positive";
} else {
    out << "x and y are negative";
}
```
