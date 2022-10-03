# Quick Start Guide
### Installation
- In VSCode, open the command palette (Ctrl+Shift+P) and type `Tasks: Configure Tasks` -> `Create tasks.json file from template` -> `Others` -> `Python: Current File`

- Now open the new `tasks.json` in the `.vscode` folder and replace the contents with the following:
```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Run Verscae File",
            "type": "shell",
            "command": "python verscae.py ${file}",
        },
        {
            "label": "Decompile Verscae File",
            "type": "shell",
            "command": "python verscae.py ${file} True",
        }
    ]
}
```
#### IF YOU HAVE PYTHON INSTALLED FROM THE MICROSOFT STORE, YOU MUST CHANGE THE COMMAND TO `python3` INSTEAD OF `python` 
#### If you installed python in a different directory, change the `python` in the `command` to the path to your python executable. 

- Now open the command palette again and type `Run Task` and select `Run Verscae File` or `Decompile Verscae File` depending on what you want to do.
- If you want to use a keyboard shortcut, you can do that by going to `File` -> `Preferences` -> `JSON Keyboard Shortcuts` and add the following:
```json
[
    {
        "key": "F6",
        "command": "workbench.action.tasks.runTask",
        "args": "Run Verscae File"
    },
    {
        "key": "shift+F6",
        "command": "workbench.action.tasks.runTask",
        "args": "Decompile Verscae File"
    }
]
```
- Remember to add the trailing comma to the last line of the original file if you don't have one already.
- Now you can run the verscae file by pressing F6 or decompile it by pressing Shift+F6.

## How to use
| There are example files located in the example folder
- The file name must end with `.v` and can be in any directory as long as you have the path to it.

## How to write a code in Verscae
- The syntax is very similar to python, but there are some differences.
- The syntax is also very similar to JavaScript and C++.
- In the following anywhere you see `()` you can replace it with an appropriate value.

### Basics
- You can use `,` to seperate things in `{}` and it will not cause any errors.
- You can use `;` at the end of lines, and it will not cause any errors.

- Heres 2 fully working examples:
```Swift
class Person {
    func say_hi() {
        out < "Hello, my name is Jhon" | red;
    },
    func say_bye() {
        out < "Goodbye" | green;
    },
},
```
- Using `,` will also work as seen as on the example above.

```Swift
class Person {
    func say_hi() {
        out < "Hello, my name is Jhon" | red
    }
    func say_bye() {
        out < "Goodbye" | green
    }
}
```
- Not using `,` will also work as seen as on the example above.

### Classes
- Classes are written in the following format:
```Swift
class (name) {
    (statements)
}
```

### Functions
- Functions are written in the following format:
```Swift
func (name)(args) {
    (statements)
}
```

### Variables
- Variables are written in the following format:
```Swift
var (name) = (value)
```

### If statements
- The conditions in an if statement can follow the python syntax.
- If statements are written in the following format:
```Swift
if (condition) {
    (statements)
}
```

### For loops
- For loops are written in the following format:
```Swift
for (variable) in (range) {
    (statements)
}
```

### While loops
- The conditions in a while loop can follow the python syntax.
- While loops are written in the following format:
```Swift
while (condition) {
    (statements)
}
```

### Importing
- You can import python modules using the `include` keyword. (in the future you will be able to import other verscae files)
- Importing is written in the following format:
```ruby
include [(module)]
```
- For multiple imports, you can use the following format:
```ruby
include [(module1), (module2), (module3)]
```


### Printing
- You can print to the console using the `out` keyword.
- Printing is written in the following format:
```Swift
out < (value or string) | (args)
```
- For printing you can use `f` strings in the following format:
```Swift
out < f"(data)" | (args)
```
- These are the folloing arguments you can use for colors:
```Swift
red
green
yellow
blue
magenta
cyan
white
black
bright_red
bright_green
bright_yellow
bright_blue
bright_magenta
bright_cyan
bright_white
bright_black
```

- These are the folloing arguments you can use for styles:
```Swift
bold
dim
italic
underline
blink
reverse
hidden
```

- These are the folloing arguments you can use for aligning:
```Swift
left
center
right
justify
```

- These are the folloing arguments you can use for ending:
```Swift
newl
tab
rw
space
endl
```

- Here are some examples of printing with arguments:
```Swift
out < "Hello" | red | center | newl
out < "Hello" | bold
out < "Hello" | center | tab
out < "Hello" | center | endl | green
```
- You can also print without arguments:
```Swift
out < "Hello"
```

### Input
- You can get input from the user using the `in` keyword.
- Input is written in the following format:
```Swift
in (variable) < (string) | (args)
```
- Input arguments are the same as the print arguments.

### Any python syntax
- You can use any python syntax in the verscae file, and it will work as expected.
- As long as you replace all the `:` with `{` and the indented part with `}`.
- Here is an example of a python function in verscae:
```python
def say_hi() {
    print("Hello")
}
```
```python
for i in range(10) {
    print(i)
}
```

- Bellows are some examples of python syntax mixed with verscae syntax:
```r
for i in range(10) {
    out < i | red
}
```

### Comments
- Comments are written in the following format:
```rust
// (comment)
```
- You can put comments anywhere in the code.

### Other
- You can use `return` to return a value from a function.
- You can use `break` to break out of a loop.
- You can use `continue` to continue to the next iteration of a loop.
- You can use `pass` to do nothing.

### Running the code
- You have to have a public function called `main` in the file.
- The `main` function will be called when you run the file.
- You can call other functions from the `main` function.
- If you do not have a `main` function, the file will not run.

### Example Program
- Here is an example program that takes input from the user and prints it back to the user.
```rust:
class Person {
    func say_hi() {
        out < "Hello, my name is Jhon" | red
    }
    
    func say_bye() {
        out < "Goodbye" | green
    }
}

public main() {
    var name = "";
    
    in name < "What is your name? " | green
    
    Person.say_hi()
    
    out < f"Hello {name}" | red

    Person.say_bye()
}
```

## Dont forget Indentation is optional, but you can still use it for readability.
