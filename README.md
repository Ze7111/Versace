<p align="center">
  <img src="images/logo.png">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Version-4.1.1-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/license-Creative%20Commons-green?style=for-the-badge">
  <img src="https://img.shields.io/github/stars/Ze7111/Versace?style=for-the-badge">
  <img src="https://img.shields.io/github/issues/Ze7111/Versace?color=red&style=for-the-badge">
  <img src="https://img.shields.io/github/forks/Ze7111/Versace?color=teal&style=for-the-badge">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Author-Ze7111-blue?style=flat-square">
  <img src="https://img.shields.io/badge/Open%20Source-Yes-darkgreen?style=flat-square">
  <img src="https://img.shields.io/badge/Maintained%3F-Maybe-yellow?style=flat-square">
  <img src="https://img.shields.io/badge/Written%20In-Python-darkcyan?style=flat-square">
  <img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FZe7111%2FVersace-Programing-language&title=Visitors&edge_flat=True"/>
  <a href="https://www.codefactor.io/repository/github/Ze7111/Versace/overview/master"><img src="https://www.codefactor.io/repository/github/Ze7111/Versace/badge/master" alt="CodeFactor" /></a>
</a>
</p>

<p align="center"><b>A beginners friendly, Programing language made from the ground up with pyhton.</b></p>

### This Language does ```NOT``` require indentation, however you ```can``` use it.
### This Language is also semicolon and comma friendly

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Install for Windows](#install-for-windows)
- [Install for Linux](#install-for-linux)
- [Install for Mac](#install-for-mac)
- [Visual Studio Code Extension for Syntax Highlighting](#visual-studio-code-extension-for-syntax-highlighting)
- [Wiki](#wiki)
- [Beginner's Guide](#beginners-guide)
- [Quick Start Guide](#quick-start-guide)
- [Syntax Diffrences Sheet](#syntax-diffrences-sheet)
- [Snippets](#snippets)
- [How to install the release version](#how-to-install-the-release-version)
  - [For Syntax highlighting](#for-syntax-highlighting)
- [How to install the source code and use it](#how-to-install-the-source-code-and-use-it)
  - [If you want to turn on DRAMATIC mode...](#if-you-want-to-turn-on-dramatic-mode)
  - [If you want to decompile the Versace file to python.](#if-you-want-to-decompile-the-versace-file-to-python)
- [Diffrences between Versace and Python](#diffrences-between-versace-and-python)
  - [At this point, you might be wondering, ghee, I have to give this language a try, but how do I do that?](#at-this-point-you-might-be-wondering-ghee-i-have-to-give-this-language-a-try-but-how-do-i-do-that)
- [Features](#features)
- [Currently Inbuilt Syntax](#currently-inbuilt-syntax)
  - [With a basic Description](#with-a-basic-description)
- [Dramatic Mode in action](#dramatic-mode-in-action)

## Install for Windows
- Open a non-admin powershell window
- Paste the following command
```powershell
New-Item "$HOME\versace" -ItemType "directory" -Force
Invoke-WebRequest "https://github.com/Ze7111/Versace/releases/latest/download/Windows-Versace-4.6.6.zip" -OutFile "$HOME\versace\versace.zip"
Expand-Archive "$HOME\versace\versace.zip" -DestinationPath "$HOME\versace" -Force
Remove-Item "$HOME\versace\versace.zip" -Force
[Environment]::SetEnvironmentVariable("Path", [Environment]::GetEnvironmentVariable("Path", "User") + ";$HOME\versace\Windows-Versace-4.6.6", "User")
```

## Install for Linux
- Open terminal
- Paste the following command into terminal and press enter
```bash
mkdir -p $HOME/versace
wget -O $HOME/versace/versace.zip
unzip $HOME/versace/versace.zip -d $HOME/versace
rm $HOME/versace/versace.zip
echo "export PATH=$PATH:$HOME/versace/Linux-Versace-4.6.6" >> $HOME/.bashrc
```
- Once done, restart the terminal or whatever you are using to run versace
- You can now test that versace is installed with `versace -v`
- If that does not work, you can download the zip manually from the releases below and extract it to `$HOME/versace/Linux-Versace-4.6.6`

## Install for Mac
- There is no binary for mac, you will need to install the python located in `src/versace.py` file along with the dependencies and use it with python

## Visual Studio Code Extension for Syntax Highlighting
- Download the extension from [here](https://marketplace.visualstudio.com/items?itemName=Ze7111.versace)
- Install the `.vsix` file to your VSCode

## [Wiki](https://github.com/Ze7111/Versace/wiki)
## [Beginner's Guide](docs/BEGINNERS%20GUIDE.md)
## [Quick Start Guide](docs/DOCUMENTATION.md)
## [Syntax Diffrences Sheet](docs/SYNTAX.md)
## [Snippets](docs/SNIPPETS.md)

## How to install the release version
- Download the latest release from [here](https://github.com/Ze7111/Versace-Programing-language/releases/latest)
- Extract the zip file
- Open the folder in vscode
- Read the README.md file there or [here](docs/RELEASE%20README.md)

### For Syntax highlighting
- Open a `.v` file in vscode
- Open the command pallete `(Ctrl+Shift+P)`
- Type `Select Language Mode`
- Select `Rust` or `Swift` (we dont have a syntax highlighter for versace yet)
- Enjoy

## How to install the source code and use it
- Clone the repo with the following command
```bash
git clone https://github.com/Ze7111/Versace-Programing-language
```
- Open the folder in vscode
- Open the command pallete `(Ctrl+Shift+P)`
- Type `Select Python Interpreter`
- Create a `.v` file in vscode
- and put the following code in it (this is a test program)
```swift
public main() {
  out < "Hello World" < blue < center < newl
}
```
- For the above code to work, you need to have the following python modules installed
  - `rich`
  - `pyinstaller`
  - `psutil`
  - `requests`

- For Syntax highlighting do the following
  - with the `.v` file open in vscode
  - Open the command pallete `(Ctrl+Shift+P)`
  - Type `Select Language Mode`
  - Select `Rust` or `Swift` (we dont have a syntax highlighter for versace yet)
  - Enjoy
  
- To run the program do the following
  - open the `.vscode` -> `tasks.json` file
  - save the file
  - open the command pallete `(Ctrl+Shift+P)`
  - type `Preferences: Open Keyboard Shortcuts (JSON)`
  - add the following code to the file
  - The VSCode keyboard shortcuts for **Windows** and **Linux** is:
```json
[
    {
        "key": "F6",
        "command": "workbench.action.terminal.sendSequence",
        "args": { "text": "versace '${file}'\u000D" }
    },
    {
        "key": "shift+F6",
        "command": "workbench.action.terminal.sendSequence",
        "args": { "text": "versace '${file}' -d\u000D" }
    },
    {
        "key": "ctrl+F6",
        "command": "workbench.action.terminal.sendSequence",
        "args": { "text": "versace '${file}' --debug\u000D" }
    }

]
```
- Now you can run the program by pressing `F6` and decompile it into a python file by pressing `Shift+F6`
- If you did everything correctly, you should see the following output
```bash
Hello World
```

### If you want to turn on DRAMATIC mode...
| Run the code normally but add a `-m` flag so like this: `versace "examples\\calculator.v" -m` 

### If you want to decompile the Versace file to python.
- While Running the file, add a True to the end, so the statemnt looks like the folloing (on windows)
```bat
$ versace "examples\calculator.v" True
```

## Diffrences between Versace and Python
- Versace is a ```beginners friendly``` language, so it has a lot of features that make it easier to learn.
- Versace is a non ```indentation based``` language, so you can use it without worrying about indentation.
- Versace is a ```semicolon and comma``` friendly language, so you can use it without worrying about semicolons and commas.
- Versace is non ```linear``` language, so you can use it without worrying about the order of the functions, classes, etc.
- Versace is a ```dramatic``` language, so you can use it in a ```dramatic``` way.
- Versace has a ```decompiler``` so you can decompile your versace code to python.
- Versace is a ```python``` based language, so you can use it with python.
- Versace has ```colors and emojis``` so you can use it with colors and emojis.
  
### At this point, you might be wondering, ghee, I have to give this language a try, but how do I do that?
- You can download the latest release from [here](https://github.com/Ze7111/Versace-Programing-language/releases/latest)
- Extract the zip and open the folder in vscode
- Read the README.md file there or read the [Release Documentation](docs/RELEASE%20README.md)
- Enjoy :D

## Features
- It natively works with python and python libraries
- The inbuilt syntax is very user friendly and easy to understand
- Inbuilt decompiler to converd Versace files to python code
- Dramatic Music and cool build style
- Crossover between Java, JavaScript and Python
- No indentaiton Required anywhere at anypoint (you can still indent for neatness)
- All string types work nativly

## Currently Inbuilt Syntax
### With a basic Description
Versace Code | Description
---|---
`try` | Tries to run the code in the try block
`if` | Runs the code in the if block if the condition is true
`else` | Runs the code in the else block if the condition is true
`for` | Runs the code in the for block for each item in the list
`while` | Runs the code in the while block while the condition is true
`class` | Defines a class
`new` | Creates a new instance of a class
`return` | Returns a value from a function
`from` | Imports a class from a module
`as` | Renames a module or class
`pass` | Does nothing
`break` | Breaks out of a loop
`continue` | Continues to the next iteration of a loop
`True` | A boolean value
`False` | A boolean value
`and` | A boolean operator
`or` | A boolean operator
`throw` | Throws an error
`include` | Imports a module
`else if` | Runs the code in the else if block if the condition is true
`catch` | Runs the code in the catch block if the code in the try block fails
`func` | Defines a function
`async func` | Defines a function that runs in the background (async)
`const` | Defines a constant variable
`null` | A null value
`include [function] from [module]` | Imports a function from a module
`from [file] include *` | (you can **NOT** yet import a specific function) Imports all the classes and functions from a file (the file can be a python file or a versace file)
`in name < "What is your name?" < (args) < (type)` | Asks the user for input and stores it in the variable `name`
`out < "Hello World" < (args)` |  Prints the text to the console with the given arguments
`public main()` | The main function that runs when the program starts

## Dramatic Mode in action
![image](images/Picture1.png)
