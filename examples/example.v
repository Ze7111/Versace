" This is an example of a Verscae file. "

" To run this file, use the command: verscae examples\\example.v "
" if in MacOS or Linux, use the command: python3 verscae.pyc examples/example.v "

" To decompile this file, use the command: verscae examples\\example.v -d "
" if in MacOS or Linux, use the command: python3 verscae.pyc examples/example.v -d "

" if your using vscode, you can use the task runner to decompile the file. "

include [time] // time is a python module but it will work with verscae

from examples.example_module include * // This is how you import a function from another file
from examples.example_module_py include * // This is how you import a function from another file

public main() {
    out < "Hello World!" < newl < blue
    out < f"The time is {time.strftime('%H:%M:%S')}" < newl < red
    out < "This is an example of a Verscae file." < newl < blue
    out < "we will now import a module made with verscae" < newl < blue
    num1 = start()
    out < "The number you entered was " < num1 < newl < blue
    out < "now we will import a module made with python" < newl < blue
    something()
}