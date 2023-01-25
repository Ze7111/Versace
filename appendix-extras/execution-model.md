---
description: The execution model of Versace
---

# Execution Model

## Execution Model (Versace)

1. Tokenize
2. Parse
3. Transpiler
4. Execute/Compile/Translate

### Tokenize

#### The tokenizer in Versace is different from most other languages.

It works by reading all the code from the file as one continuous string without leading/trailing whitespace. it then reads each character, and if it a part of the alphabet, it will read the next character until it is not unless it starts with ("). it will then merge all the newly read characters into one token(list) and repeat the process until it reaches the end of the file. It will also look for (;) and if it finds one, it will split that token into two tokens with the first one being the token before the (;) and the second one being the token after the (;). Finally, it will make a nested list of all the tokens, and then move on to the next step.

**Example of a line getting tokenized:**

```python
int a = 1;

Stage 1: ['i', 'n', 't', 'a', '=', '1', ';']
Stage 2: [['int', 'a', '=', '1', ';']]
```

**Result: \[\['int', 'a', '=', '1']]**

**Example of multiple lines getting tokenized:**

```python
int a = 1;
str b = "hello world";

Stage 1: ['i', 'n', 't', 'a', '=', '1', ';', 's', 't', 'r', 'b', '=', '"', 'h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd', '"', ';']
Stage 2: [['int', 'a', '=', '1', ';', 'str', 'b', '=', '"hello world"', ';']]
```

**Result: \[\['int', 'a', '=', '1'], \['str', 'b', '=', '"hello world"']]**

### Parse

#### The parser in Versace is different from most other languages.

It will always check the first word in the token list, and if it is a keyword, if it is a keyword, it will then send that token list to the function that handles that keyword. if it is not a keyword it will then check if a class with that name exists, and if not, it will throw an error.

**Example of a token getting parsed:**

```python
['int', 'a', '=', '1']

Stage 1: keyword = 'int'
Stage 2: boolean (does 'int' exist in the keywords list) = True
Stage 3: send token list to the function that handles the 'int' keyword
```

**Result: a: int = 1 (with type checking)**

**Example of multiple tokens getting parsed:**

```python
[['int', 'a', '=', '1'], ['str', 'b', '=', '"hello world"']]

Stage 1: keyword = 'int'
Stage 2: boolean (does 'int' exist in the keywords list) = True
Stage 3: send token list to the function that handles the 'int' keyword
```

**Result: a: int = 1 (with type checking)**

```python
Stage 1: keyword = 'str'
Stage 2: boolean (does 'str' exist in the keywords list) = True
Stage 3: send token list to the function that handles the 'str' keyword
```

**Result: b: str = "hello world" (with type checking)**

### Parse Tree:

<details>

<summary>All the keywords currently in Versace:</summary>

1. `public`
2. `priv`
3. `method`
4. `with`
5. `call`
6. `if`
7. `else`
8. `else if`
9. `for`
10. `while`
11. `return`
12. `class`
13. `struct`
14. `static`
15. `enum`
16. `func`
17. `async`
18. `await`
19. `coroutine`
20. `const`
21. `ref`
22. `let`
23. `final`
24. `out`
25. `in`
26. `include`
27. `import`
28. `from`
29. `pyc`
30. `@`
31. `int`
32. `float`
33. `complex`
34. `double`
35. `str`
36. `usize`
37. `bool`
38. `list`
39. `map`
40. `array`
41. `set`
42. `bytes`
43. `char`
44. `memoryview`
45. `bytearray`
46. `frozenset`
47. `range`
48. `None`
49. `NoneType`
50. `u8`
51. `u16`
52. `u32`
53. `u64`
54. `u128`
55. `i8`
56. `i16`
57. `i32`
58. `i64`
59. `i128`
60. `f32`
61. `f64`

</details>

### Transpile

#### The transpiler in Versace is different from most other languages.

It will work by taking the parse tree and converting it into a string of python code. It will then write that string to a file and then run it using the python interpreter.

**Example of a parse tree getting transpiled:**

```python
a: int = 1
Stage 1: check if 'a' is a variable, if yes throw an error as we tried to declare a variable that already exists without using the `let` keyword
Stage 2: check if 'a' is a variable, if no, check if '1' matches the type of 'int'
Stage 3: check if '1' is a variable, if yes, get the type of '1' and check if it matches the type of 'int'
Stage 4: repeat stage 3 until it reaches the end of the parse tree
```

* Result: a: int = 1 # the: int means we are declaring a variable with the type of int, and not assigning an already existing variable

### Execute/Compile/Translate

#### The execution stage in Versace is different from most other languages.

It will work by taking the transpiled code and running it using the python interpreter (with the extra lines in the code, to make it execute a lot faster). It will securely run the code using the python interpreter, and then print the output (Versace uses `subprocess` to run the code on any platform and uses `_winapi` to run the code on windows). The code will be run in a separate process and will not be able to access any program in the main process (unless specified).

#### The compiler stage in Versace is different from most other languages.

The Versace compiler uses `pyinstaller` to compile the code into a .exe file. Or cx\_freeze to compile the code into a .exe file. The compiler takes the transpiled code and executes a `pyinstaller/cx_freeze` command in a separate process (hence why you see a loading bar and not the raw output of the command). If the compilation is successful, it will then move the .exe file to the directory of the Versace file. If the compilation is not successful, it will then print the error message and delete any files that were created during the compilation process.

#### The translator stage works in the following way.

It will save the transpiled code to a file.
