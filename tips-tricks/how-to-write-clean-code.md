# How to write clean code

### 1. Use the right indentation

Use 4 spaces for indentation. Do not use tabs.

### 2. Use the right naming

Use camelCase for variables and functions. Use PascalCase for classes.

### 3. Use the right spacing

Always add a space between operators and operands. For example:

```csharp
int a = 1 + 2;
```

Do not add a space between a function name and the opening parenthesis. For example:

```csharp
int a = Add(1, 2);
```

This is an example of a bad spacing:

```csharp
int a=1+2;
int a=Add (1, 2);
```

### 4. Use the right comments

Use `//` for single line comments. Use `/* */` for multi line comments.

### 5. Use the right casing

Use PascalCase for classes. Use camelCase for variables and functions.

### 6. Use the right line endings

Use Unix line endings. Do not use Windows line endings.

### 7. Use the right line length

Use a maximum line length of 80 characters.

### 8. Use the right braces

Always use braces for if statements, for loops, while loops, etc.

### 9. Use the right newlines

Always add a newline at the end of the file.

### 10. Use the right file encoding

Use UTF-8 for file encoding.

### 11. Use the right file extension

Use `.v` for Versace files. Use `.vh` for Versace header files. Use `.md` for Markdown files.

### 13. Use the right file structure

Use the following structure for Versace files:

```
root directory
├── documentation.md
├── main.v
├── main.vh
└── README.md
```

Do not use the following structure:

```
root directory
├── documentation.md 
├── README.md
code directory
    ├── main.v
    └──  main.vh 
```

This is because, the user that downloads the code will not know where to put the header file or where the code is. The only time you should use the second structure is if you are making a library. In that case, you should use the following structure:

```tremor
root directory
├── documentation.md
├── README.md 
├── main.v
headder files
    ├── main.vh
    ├── second.vh
    ├── third.vh
some method folder
    ├── some_method_one.v
    └── some_method_two.v
```

### 14. Use the right file names

Use `main.v` for the main file. Use `main.vh` for the main header file. Use `README.md` for the README file. Use `documentation.md` for the documentation file.
