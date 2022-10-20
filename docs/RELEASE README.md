# Versace Release 3.0.1
## Instructions
- Downlaod the zip
- Extract the zip anywhere
- Open the dir of the new folder in vs code
- Open the `.vscode` folder
- Open the `tasks.json` file
- Press `Ctrl+S` to save the file

- Open the command palette `(Ctrl+Shift+P)`
- Type `Preferences: Open Keyboard Shortcuts (JSON)` and press enter
- Add the following code to the file
```json
    {
        "key": "F6",
        "command": "workbench.action.tasks.runTask",
        "args": "Run Versace File"
    },
    {
        "key": "shift+F6",
        "command": "workbench.action.tasks.runTask",
        "args": "Decompile Versace File"
    }
```

- So the file should look like this:

```jsonc
[
    // Your other keybindings if you have any
    {
        "key": "F6",
        "command": "workbench.action.tasks.runTask",
        "args": "Run Versace File"
    },
    {
        "key": "shift+F6",
        "command": "workbench.action.tasks.runTask",
        "args": "Decompile Versace File"
    }
]
```
- Save the file
- And you're done!

- Now you can press `F6` to run the file and `Shift+F6` to decompile the versace file
- You can also run the file by pressing `Ctrl+Shift+B` and selecting the task

- Remember wherever you have a versace file, you should have the versace folder in the same directory

- If you need help coding a [DOCUMENTATION.md](DOCUMENTATION.md) file is there in the versace folder
