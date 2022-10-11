# Verscae Release 3.0.1
## Instructions
- Downlaod the zip for your system
- Then Follow the README.md inside the extracted path
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
        "args": "Run Verscae File"
    },
    {
        "key": "shift+F6",
        "command": "workbench.action.tasks.runTask",
        "args": "Decompile Verscae File"
    }
```

- So the file should look like this:

```jsonc
[
    // Your other keybindings if you have any
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
- Save the file
- And you're done!

- Now you can press `F6` to run the file and `Shift+F6` to decompile the verscae file
- You can also run the file by pressing `Ctrl+Shift+B` and selecting the task

- Remember wherever you have a verscae file, you should have the verscae folder in the same directory

- If you need help coding a [DOCUMENTATION.md](DOCUMENTATION.md) file is there in the verscae folder
