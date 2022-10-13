# Changes
- Fixed a lot of broken and buggy items.
- Added proper multi OS support, so now you can run the program on any OS without having to edit the code **(in theory)**.
- Added a new debug mode, so now you can debug your code and generate dump files. This is accessed by running the program with the `--debug` flag.
- Added a new `--version` flag, so now you can check the version of the program.
- Added a new `--help` flag, so if you want to know how to use the program, you can use the `--help` flag.
- You can now use `;` to separate statements on the same line. This is useful for when you want to write a lot of statements on the same line.
- You can now use `////` to show `//` inside a string or comment, before if you put `//` anywhere in a string or comment, it would break the code.
- You can now import functions and classes from python modules, and use them in your code. This is done by using the `include [function or class] from [module]` keyword.

### Make sure the `verscae.exe` is in your PATH or in the same dir as the file you want to run

- How to run on Linux or MacOS:
```bash
python3 verscae.py filename.v
```
### Make sure the `verscae` file for Linux is in your PATH or in the same dir as the file you want to run
## The rest of the readme is available [here](README.md) 

# Requirements
- Python 3.x is a must.
- The rest of the module requirements are installed automatically when you run the program for the first time.
- VScode is now optional but for the keyboard shortcuts it is recommended

# ---- READ EVERYTHING BELOW THIS LINE ----
- If you want music to play when compiling, you can add the music file in the same dir as the `verscae.py` file and name it `music.mp3`
- The command to play music while compiling is `verscae filename.v -m` on windows and `python3 verscae.py filename.v -m` on Linux or macOS

- If you want to decompile a file, you can use the command `verscae filename.v -d` on windows and `python3 verscae.py filename.v -d` on Linux or macOS
- If you want to decompile a file and play music while decompiling, you can use the command `verscae filename.v -d -m` on windows and `python3 verscae.py filename.v -d -m` on linux or macos (The order of the `-d` and `-m` dont matter)
- If you want to debug a file, you can use the command `verscae filename.v --debug` on windows or linux and `python3 verscae.py filename.v --debug` on macOS
- Remember each verscae file must have a `.v` extension and must start with the following:
```swift
public main() {
    // code here
}
```
- Functions can go anywhere, this is a non-linear language, so you can call a function before it is defined.
- You can also define a function inside another function, but you can't call it before it is defined.

- For macOS the `verscae.pyc` file must be in the same dir as the files you want to run.
- The VSCode keyboard shortcuts for **MacOS** is:
```json
[
    {
        "key": "F6",
        "command": "workbench.action.terminal.sendSequence",
        "args": { "text": "python3 verscae.pyc '${file}'\u000D" }
    },
    {
        "key": "shift+F6",
        "command": "workbench.action.terminal.sendSequence",
        "args": { "text": "python3 verscae.pyc '${file}' -d\u000D" }
    },
    {
        "key": "ctrl+F6",
        "command": "workbench.action.terminal.sendSequence",
        "args": { "text": "python3 verscae.pyc '${file}' --debug\u000D" }
    }
]
```

- For windows and linux you can add the `verscae.exe` and `verscae` files to your PATH and run from anywhere or you can add them to the same dir as the files you want to run.
- The VSCode keyboard shortcuts for **Windows** and **Linux** is:
```json
[
    {
        "key": "F6",
        "command": "workbench.action.terminal.sendSequence",
        "args": { "text": "verscae '${file}'\u000D" }
    },
    {
        "key": "shift+F6",
        "command": "workbench.action.terminal.sendSequence",
        "args": { "text": "verscae '${file}' -d\u000D" }
    },
    {
        "key": "ctrl+F6",
        "command": "workbench.action.terminal.sendSequence",
        "args": { "text": "verscae '${file}' --debug\u000D" }
    }

]
```

- Thats it, enjoy the language, and if you have any suggestions, please let me know in the issues tab.

# Notes
- The zip files contain examples and a README.
- The non-zip files are only for people who want the bare minium, so no music, no readme or any examples.