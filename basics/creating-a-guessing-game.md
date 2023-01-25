---
description: We are going to be making a simple guessing game
---

# Creating a guessing game

### Introduction

We will be learning how to create a simple guessing game in Versace. This will be a simple game where the user will guess a number between 1 and 10. If the user guesses the correct number, they win. If they guess the wrong number, they try again. We will be using the `in` to get the user's guess and the `out` to display the result.

### Creating the game

We first need the `random` module, we can include it in our program, by using `include`, we will be including it as `random_int`:

```csharp
include "randint" from "random" as "random_int";
```

We now need to create the public init function, this will run first to initialize the program:

```csharp
public init() {
    // code
}
```

All of our code from now will be inside the init function. Our next step is to generate the random number, we can do this by using the `random_int` function:

```csharp
int number = random_int(1, 10);
```

Now we need to create a while loop, this will be used to keep the game running until the user guesses the correct number:

```csharp
while (true) {
    // code
}
```

Now we need to get the user's guess, we can do this by using the `in` function (This goes inside the while loop):

```csharp
in guess << "Enter a guess: " << int << bright_red;
```

Now we need to check if the user guessed the correct number, we can do this by using an if statement:

```csharp
if (guess == number) {
    // code
}
```

If the user guessed the correct number, we need to display a message, we can do this by using the `out` function (This goes inside the if statement):

```csharp
out << "You guessed it! The number was" << number << "." << bright_blue;
```

Now we need to break out of the while loop, we can do this by using the `break` keyword:

```csharp
break;
```

If the user guessed the wrong number, we need to display a message, we can do this by using the `out` function (This goes inside the while loop):

```csharp
out << "You guessed wrong! Try again." << bright_red;
```

Now we can run our program by going to the terminal and typing `versace guessing_game.vs`:

```bash
$ versace guessing_game.vs
```

### Conclusion

We have now created a simple guessing game in Versace. We have learned how to use the `in` and `out` functions, we have also learned how to use the `include` keyword and the `random_int` function. We have also learned how to use the `while` loop and the `if` statement. We have also learned how to use the `break` keyword.

### Full Game Code (made a little better)

```csharp
include "randint" from "random" as "random_int";

public init() {
    int number = random_int(1 | 10);
    out << "This is a guessing game. I'm thinking of a number between 1 and 10." << bright_green;
    out << "Try to guess it in as few attempts as possible." << bright_green;
    while (true) {
        in guess << "Enter a guess: " << int << bright_red;
        if (guess == number) {
            out << "You guessed it! The number was" << number << "." << bright_blue;
            break;
        } else if (guess < number) {
            out << "Your guess is too low." << bright_red;
        } else {
            out << "Your guess is too high." << bright_red;
        }
    }
}
```
