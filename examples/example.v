" This is an example of a Verscae file. "

" To run this file, use the command: verscae example.v "
" if in MacOS or Linux, use the command: python3 verscae.py example.v "

" if your using vscode, you can use the task runner to run the file. "

" To decompile this file, use the command: verscae example.v -d "
" if in MacOS or Linux, use the command: python3 verscae.py example.v -d "

public main() { // The main function is the entry point of the program.
    out < "Hello, World!" < red < newl // Prints "Hello, World!" in red.
    in name < "What is your name? " < green < endl // Asks for the user's name and greets them.
    out < "Hello, " < name < "!" < newl; // Semi-colons are optional.
    out < f"Goodbye, {name}!" < newl // f-strings are supported.
    return 0; // The return value of the main function is the exit code of the program.
} // The semicolon is optional as well.
