import random
import sys

Version = '4.6.6'   # Define the Version variable as 4.6.6

def makeconfigfile(configpath):
    data = """[Core-Config]
music-option = false
version = 4.6.6
tab-style = "    "

start-indentation-level = 0
do-once = true
start-in-module-mode = false
recurse-from-function = false
no-args-start = false
always-monitor-performance = false"""
    with open(configpath, 'w') as f:
        f.write(data)

def installmodules():  # Define the installmodules function
    try:   # Try to run the code
        subprocess.run('pip install rich requests psutil pyinstaller', shell=True)  # Install the modules
    except Exception as e:
        subprocess.run('pip3 install rich requests psutil pyinstaller', shell=True) # Install the modules        

def readconfig():   # Define the readconfig function
    import configparser, os
    config_obj = configparser.ConfigParser()  # Define the config variable as a ConfigParser object
    
    if os.name == 'nt': # Check if the OS is Windows
        if os.path.exists(f"C:{os.sep}Users{os.sep}{os.getlogin()}{os.sep}versace{os.sep}Windows-Versace-{Version}{os.sep}config.ini"):
            configpath = f"C:{os.sep}Users{os.sep}{os.getlogin()}{os.sep}versace{os.sep}Windows-Versace-{Version}{os.sep}config.ini"  # Define the configpath variable as the path to the config file
        else:
            if os.path.exists(f"C:{os.sep}Users{os.sep}{os.getlogin()}{os.sep}versace{os.sep}Windows-Versace-{Version}"):
                configpath = f"C:{os.sep}Users{os.sep}{os.getlogin()}{os.sep}versace{os.sep}Windows-Versace-{Version}{os.sep}config.ini"  # Define the configpath variable as the path to the config file
                makeconfigfile(configpath)
            else:
                makeconfigfile("config.ini")
    elif os.name == 'posix':
        if os.path.exists(f"{os.sep}home{os.sep}{os.getlogin()}{os.sep}versace{os.sep}Linux-Versace-{Version}{os.sep}config.ini"):
            configpath = f"{os.sep}home{os.sep}{os.getlogin()}{os.sep}versace{os.sep}Linux-Versace-{Version}{os.sep}config.ini"
        else:
            if os.path.exists(f"{os.sep}home{os.sep}{os.getlogin()}{os.sep}versace{os.sep}Linux-Versace-{Version}"):
                configpath = f"{os.sep}home{os.sep}{os.getlogin()}{os.sep}versace{os.sep}Linux-Versace-{Version}{os.sep}config.ini"
                makeconfigfile(configpath)
            else:
                makeconfigfile("config.ini")
    elif os.name == 'mac':
        if os.path.exists(f'{os.path.dirname(os.path.realpath(__file__))}{os.sep}config.ini"'):
            configpath = f"{os.sep}Users{os.sep}{os.getlogin()}{os.sep}versace{os.sep}Mac-Versace-{Version}{os.sep}config.ini"
        else:
            configpath = os.path.dirname(os.path.realpath(__file__)) + f"{os.sep}config.ini"
            makeconfigfile(configpath)
    else:
        print('Error: Could not locate the config file please add it to the same directory where you installed Versace')
        exit()
    
    try:
        config_obj.read(f'{configpath}')   # Read the config.ini file
        Core = config_obj["Core-Config"]   # Define the Core variable as the Core-Config section

        music_option = Core["music-option"] # Define the music_option variable as the music-option option
        tab = Core["tab-style"] # Define the tab variable as the tab-style option
        
        numtabs = Core["start-indentation-level"] # Define the numtabs variable as the start-indentation-level option
        do_once = Core["do-once"]  # Define the do_once variable as the do-once option
        in_module = Core["start-in-module-mode"] # Get the start-in-module-mode value
        recurse = Core["recurse-from-function"]  # Get the recurse value
        noargs = Core["no-args-start"] # Define the noargs variable as the no-args-start value in the config file
        perf_monitor_always_on = Core["always-monitor-performance"] # Define the perf_monitor_always_on variable as the perf-monitor-always-on value in the config file
    except Exception as e:
        print('Error: Could not read the config file from {}'.format(configpath))
        print(f"Error: {e}")
        exit()
    
    return music_option, tab, numtabs, do_once, in_module, recurse, noargs, perf_monitor_always_on # Return the variables

def convert_to_bool(string):    # Define the convert_to_bool function
    import os
    if string.lower() == 'true':    # If the string is True
        return True
    elif string.lower() == 'false': # If the string is False
        return False
    else:
        os.system("")
        # find where in the config file is the string
        print('\u001b[41;1m' + f'Error: Could not read a line in the config file as it is not a valid statemnt' + '\u001b[0m')  # Print an error message
        print('\u001b[31;1m' + f'Expected : a boolean value not "{string}"' + '\u001b[0m')  # Print an error message
        exit()

music_option, tab, numtabs, do_once, in_module, recurse, noargs, perf_monitor_always_on = readconfig() # Read the config file 

music_option = convert_to_bool(music_option) # Define the music_option variable as a boolean
tab = tab.replace('"', '')
numtabs = int(numtabs)  # Convert the numtabs variable to an integer
do_once = convert_to_bool(do_once) # Convert the do_once variable to a bool
in_module = convert_to_bool(in_module) # Convert the in_module variable to a bool
recurse = convert_to_bool(recurse) # Convert the recurse variable to a bool
noargs = convert_to_bool(noargs) # Convert the noargs variable to a bool
perf_monitor_always_on = convert_to_bool(perf_monitor_always_on) # Convert the perf_monitor_always_on variable to a bool
compare_version = Version # Define the compare version

if len(sys.argv) == 1:  # If there are no arguments
    if noargs == False:
        noargs = True

st_time: float # create the start time variable
ed_time: float # Create the end function
main_function_found = False # Define the main function found variable
org_final = [] # Define the final list
private_vars = [] # Define the private_vars list
data = [] # Define the data list
final = [] # Add the import statement to the final line of the list

try: # Try to run the main function
    import rich # Import rich
    import os  # Import os
    import subprocess # Import subprocess
    import configparser
    import sys # Import sys
    import time # Import time
    import requests # Import requests
    import shutil # Import shutil
    import psutil # Import psutil
    from sys import exit
    from time import perf_counter   # Import the perf_counter function from the time module

except ModuleNotFoundError as e: # If the module is not found
    import subprocess, os # Import subprocess
    from sys import exit
    os.system('')
    print('\u001b[41;1mModules Not Found \u001b[0m') # Print the message
    print('\u001b[32;1mWould you like to auto-install the following modules? \u001b[0m') # Print the message
    print('\u001b[31;1m    rich\n    psutil\n    requests\n    pyinstaller\n\u001b[0m') # Print the message
    print('\u001b[32;1m(y/n) : \u001b[0m', end='') # Print the message
    if input().lower() == 'y':
        installmodules()
        print('\u001b[32;1mModules Installed \u001b[0m') # Print the message
        print('\u001b[31;1mPlease re-run Versace to continue\u001b[0m') # Print the message
        exit()
    else: # If the user does not want to install the modules
        print('\u001b[32;1mInvalid Input\u001b[0m') # Print the message
        print('\u001b[32;1mPlease install the modules manually\u001b[0m') # Print the message
        print('\u001b[32;1mGoodbye...\u001b[0m') # Print the message
        exit() # Exit the program

os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen

def memoize(func):
    cache = {}
    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func

class C: # Class C
    def class_(line, numtabs): # Class class_
        global tab
        line.replace('public class', 'class')
        line = line.replace('{', '') # Remove the { from the line
        line = line.strip() # Remove the spaces from the line
        line += ':' # Add a : to the line
        line = ((tab * numtabs) + line + '\n') # Add the line to the final list
        numtabs += 1 # Add 1 to the number of tabs
        return line, numtabs # Add the line to the final list

    def else_if(line, numtabs): # define the else if function
        global tab
        line = line.replace('else if', 'elif') # Replace else if with elif
        line = line.replace('{', '') # Remove the { from the line
        line = line.strip() # Remove the spaces from the line
        line += ':' # Add a : to the line
        line = ((tab * numtabs) + line + '\n') # Add the line to the final list
        numtabs += 1 # Add 1 to the number of tabs
        return line, numtabs # Return the line and the number of tabs

    def public(line, numtabs): # Define the public function
        global tab
        if line.startswith('public'): # If the line starts with public
            line = line.replace('public', 'def') # Replace public with def
        elif line.startswith('pub'):
            line = line.replace('pub', 'def') # Replace public with def
        line = line.replace('{', '') # Remove the { from the line
        line = line.strip() # Remove the spaces from the line
        line += ':' # Add a : to the line
        line = ((tab * numtabs) + line + '\n') # Add the line to the final list
        numtabs += 1 # Add 1 to the number of tabs
        return line, numtabs # Return the line and the number of tabs

    def func(line, numtabs): # Define the function function
        global tab
        if 'repr' in line: # Check if repr is in the line
            line = line.replace('repr', '__innit__') # Replace repr with __innit__
        line = line.replace('func', 'def') # Replace func with def
        line = line.replace('{', '') # Remove the { from the line
        line = line.strip() # Remove the spaces from the line
        line += ':' # Add a : to the line
        line = ((tab * numtabs) + line + '\n') # Add the line to the final list
        numtabs += 1 # Add 1 to the number of tabs
        return line, numtabs # Return the line and the number of tabs

    def asyncfunc(line, numtabs): # Define the async function
        global tab
        if 'repr' in line: # Check if repr is in the line
            line = line.replace('repr', '__innit__') # Replace repr with __innit__
        line = line.replace('async func', 'def') # Replace func with def
        line = line.replace('{', '') # Remove the { from the line
        line = line.strip() # Remove the spaces from the line
        line += ':' # Add a : to the line
        line = ((tab * numtabs) + line + '\n') # Add the line to the final list
        numtabs += 1 # Add 1 to the number of tabs
        return line, numtabs # Return the line and the number of tabs
    
    def asynccode() -> str:
        async_code = """import threading # import threading
def _async(func): # decorator for async function
    \"\"\"
        DO NOT EDIT THIS CODE
        The following code is what allows for the use of async functions in Versace
        if you do not use this code, async functions and thier associated decorators will not work
    \"\"\"
    def wrapper(*args, **kwargs): # the wrapper function that will be returned
        thread = threading.Thread(target=func, args=args, kwargs=kwargs) # create a thread
        thread.start() # start the thread
        return thread # return the thread
    
    return wrapper # return the wrapper function
\"\"\"
            You can edit any code below this line
\"\"\"
"""
        return async_code
    
    def catch(line, numtabs): # Define the catch function
        global tab
        line = line.replace('catch', 'except') # Replace catch with except
        line = line.replace('{', '') # Remove the { from the line
        line = line.strip() # Remove the spaces from the line
        line += ':' # Add a : to the line
        line = ((tab * numtabs) + line + '\n') # Add the line to the final list
        numtabs += 1 # Add 1 to the number of tabs
        return line, numtabs # Return the line and the number of tabs

    def brace(line, numtabs): # Define the brace function
        global tab
        line = line.replace('{', '') # Remove the { from the line
        line = line.strip() # Remove the spaces from the line
        line = tab * numtabs + line + ':' + '\n' # Add the line to the final list
        return line # Return the line

class include: # Class include
    def include(line): # Define the include function
        if 'from' in line: # Check if from is in the line
            # include [sleep] from [time]
            # from time import sleep
            line = line.replace('include', '')
            line = line.replace('from', '')
            line = line.split('[')[1].split(']')[0] + '893498*&(@*(&&(**' + line.split('[')[2].split(']')[0]
            line = line.split('893498*&(@*(&&(**')
            line = 'from ' + line[1] + ' import ' + line[0]
            pass

        else: # If from is not in the line
            line = line.replace('include', 'import').replace('[', '').replace(']', '') # Replace include with import and remove the [ and ]
            pass

        if '{' in line or '}' in line or '{}' in line: # Check if { or } or {} is in the line
            print('\u001b[41;1mINVALID SYNTAX\u001b[0m') # Print a message
            print('\u001b[31;1m You can\'t use {} in include statement.\u001b[0m') # Print a message
            exit() # Exit the program

        return line # Return the line

    def _from_Include(line):
        global data, recurse
        # line will be something like this
        # from [file] include *
        lineargs = line.split(' ') # Split the line by spaces
        filename = lineargs[1].replace('[', '').replace(']', '') # Get the filename
        lineargs.pop(1) # Remove the filename from the lineargs
        lineargs.pop(-1)
        lineargs = ' '.join(lineargs) # Join the lineargs
        lineargs = lineargs.strip()
        if lineargs == 'from include':
            filename = filename.replace('.', os.sep)
            if os.path.exists(filename + '.v'):
                filename = filename + '.v'
            elif os.path.exists(filename + '.py'):
                filename = filename + '.py'
            elif os.path.exists(filename + '.vh'):
                filename = filename + '.vh'
            elif os.path.exists(filename + '.vs'):
                filename = filename + '.vs'
            else:
                raise FileNotFoundError(f'File {filename} not found')
        
        with open(filename, 'r') as f:
            recurse = False
            for _ii in f.readlines():
                data.append(_ii)
                if _ii.startswith('from'):
                    recurse = True
                    data.pop(-1)
                    include._from_Include(_ii)
                    continue
        
        if recurse:
            return
        else:
            return data        
        
        


class IO: # Class IO
    def __init__(self): # Define the __init__ function
        self.colors = {
            'red',
            'green',
            'yellow',
            'blue',
            'magenta',
            'cyan',
            'white',
            'black',
            'bold red',
            'bold green',
            'bold yellow',
            'bold blue',
            'bold magenta',
            'bold cyan',
            'bold white',
            'bold black',
            'bright_red',
            'bright_green',
            'bright_yellow',
            'bright_blue',
            'bright_magenta',
            'bright_cyan',
            'bright_white',
            'bright_black',
            '#',
            'rgb',
        } # Define the colors
        self.styles = {
            'bold',
            'dim',
            'italic',
            'underline',
            'blink',
            'reverse',
            'hidden'
        } # Define the styles
        self.justify = {
            'left',
            'center',
            'right',
            'justify'
        } # Define the justify
        self.datatypes = {
            'int',
            'float',
            'str'
        } # Define the datatypes
        self.endtypes = {
            'newl' : r'\n\n',
            'tab' : r'\t',
            'rw' : r'\r',
            'space' : r' ',
            'endl' : r'',
        } # Define the endtypes

    def output(self, text): # Define the output function
        line = '' # Define the line
        if '"' not in text:
            args = text.split('<') # Split the text
            text = text.replace('<', '') # Replace the text
            text = text.replace(args[0], '') # Replace the text
            # remove the first < from the text
            text = text.replace(args[1], '') # Replace the text
            arg = args[2:] # Remove the first 2 items
            arg = '<'.join(arg) # Join the list
            text = f'out < f"{{{args[1]}}}" {"<" + arg if len(arg) >= 1 else ""}' # Set the text

        try : parse = text.split('"')[1] if '"' in text else text.split("'")[1] # Try to parse the text
        except IndexError:  # If there is an error
            parse = ''        # Set the parse to ''

        try : statements = text.split('"')[2] if '"' in text else text.split("'")[2] # Try to parse the text
        except IndexError:  # If there is an error
            statements = text.split('<')[1].strip()  # Set the statements to the text after the <
        try: statements = statements.split('<') # Try to split the statements
        except IndexError: pass # If there is an error pass
    
        statements = [statement.strip() for statement in statements] # Strip the statements
        statements = [statement for statement in statements if statement != ''] # Remove the empty statements
        statements = [statement for statement in statements if statement[0] != ' '] # Remove the empty statements
        statements = [statement for statement in statements if statement[0] != '\n'] # Remove the empty statements
        statements = [statement for statement in statements if statement[0] != ' '] # Remove the empty statements

        for i in statements: # For each statement in the statements
            line += ',' # Add a , to the line
            if i in self.colors: # Check if the statement is a color
                line += f' style="{i}"' # Add the color to the line
            elif i in self.styles: # Check if the statement is a style
                line += f' style="{i}"' # Add the style to the line
            elif i in self.justify: # Check if the statement is a justify
                line += f' justify="{i}"' # Add the justify to the line
            elif i in self.endtypes: # Check if the statement is a endtype
                line += f' end="{self.endtypes[i]}"' # Add the endtype to the line
            elif i in self.datatypes: # Check if the statement is a datatype
                continue # Continue the loop
            else: # If the statement is not a color, style, justify, endtype or datatype
                line += f' {i}' # Add the statement to the line

        line = line.rstrip(',') # Remove the , from the line
        
        if '{' or '}' in text: # Check if { or } is in the text
            additive = text.split('"' or "'")[0] # Set the additive to the text before the "
            additive = additive.split('<')[1].strip() # Set the additive to the text after the <
            line = f'print({additive}"{parse}"{line.strip()})\n' # Set the line to the print statement
            return line # Return the line

        else: # If { or } is not in the text
            line = f'print("{parse}",{line})\n' # Set the line to the print statement
            return line # Return the line

    def inp(self, text, tabs): # Define the inp function
        line = '' # Define the line
        indess = 0
        
        for i in text.split('<'): # For each item in the text
            # check if i in a endtype
            if i.strip() in self.endtypes: # Check if the statement is a endtype
                indess += 1
        
        if indess == 0: # Check if the indess is 0
            text += '< endl' # Add endl to the text
        
        try : parse = text.split('"')[1] if '"' in text else text.split("'")[1] # Try to parse the text
        except IndexError:  # If there is an error
            parse = ''        # Set the parse to ''

        try : statements = text.split('"')[2] if '"' in text else text.split("'")[2] # Try to parse the text
        except IndexError:  # If there is an error
            statements = text.split('<')[1].strip() # Set the statements to the text after the <

        try: statements = statements.split('<') # Try to split the statements
        except IndexError: pass # If there is an error pass

        var = text.split(' ')[1] # Set the var to the text after the first space

        statements = [statement.strip() for statement in statements] # Strip the statements
        statements = [statement for statement in statements if statement != ''] # Remove the empty statements
        statements = [statement for statement in statements if statement[0] != ' ']  # Remove the empty statements
        statements = [statement for statement in statements if statement[0] != '\n'] # Remove the empty statements
        statements = [statement for statement in statements if statement[0] != ' '] # Remove the empty statements
        for i in statements: # For each statement in the statements
            line += ',' # Add a , to the line
            if i in self.colors: # Check if the statement is a color
                line += f' style="{i}"' # Add the color to the line
            elif i in self.styles: # Check if the statement is a style
                line += f' style="{i}"' # Add the style to the line
            elif i in self.justify: # Check if the statement is a justify
                line += f' justify="{i}"'   # Add the justify to the line
            elif i in self.endtypes:    # Check if the statement is a endtype
                line += f' end="{self.endtypes[i]}"'    # Add the endtype to the line
            elif i in self.datatypes:   # Check if the statement is a datatype
                continue    # Continue the loop
            else:   # If the statement is not a color, style, justify, endtype or datatype
                line += f' {i}' # Add the statement to the line
        
        line = line.rstrip(',') # Remove the , from the line
        line = f'print("{parse}"{line.strip().replace(",,", ",")})\n'  # Set the line to the print statement
        if 'int' in statements: # Check if int is in the statements
            line += f'{tabs}{var} = int(input())'   # Add the input statement to the line
        elif 'float' in statements: # Check if float is in the statements
            line += f'{tabs}{var} = float(input())'     # Add the input statement to the line
        elif 'str' in statements:   # Check if str is in the statements
            line += f'{tabs}{var} = str(input())'   # Add the input statement to the line
        else:   # If int, float or str is not in the statements
            line += f'{tabs}{var} = input()'    # Add the input statement to the line

        return line     # Return the line

    def error(text):    # Define the error function
        print(f"\u001b[41;1m{text}\u001b[0m")   # Print the error

def compiler(final, 
             decomplie, 
             filename=None): # Define the compiler function
    
    filename_only = ''
    os.system('cls' if os.name == 'nt' else 'clear')    # Clear the screen
    current_time = time.time()  # Set the current time
    current_time = time.strftime('%d-%m-%Y %H-%M-%S', time.localtime(current_time)) # Set the current time

    if decomplie:   # Check if decomplie is True
        try:    # Try to open the file
            os.mkdir('src')  # Make the build folder
        except FileExistsError:     # If the folder already exists
            pass    # If the folder already exists pass
        
        filename_only = filename.split(os.sep)[-1] # Set the filename only to the filename without the extension
        filename_only = filename_only.split('.')[0]    # Set the filename only to the filename without the extension
        
        for i in sys.argv:
            if i == '-c':
                try:
                    name = sys.argv[sys.argv.index(i)+1]
                    if '.' in name:
                        file_ext = name.split('.')[1]
                        name = name.split('.')[0]
                    else:
                        file_ext = 'py'
                        name = name
                    break
                except IndexError:
                    name = ''
                    break

        print('\u001b[0m')  # Print the reset color

        if name == '':  # Check if the name is ''
            if os.name == 'nt': # Check if the os is windows
                name = f'{os.getcwd()}{os.sep}src{os.sep}{filename_only}.py' # Set the name to the current time
            else:   # If the os is not windows
                name = f'{os.getcwd()}{os.sep}src{os.sep}{current_time}.py'  # Set the name to the current time
        else:   # If the name is not ''
            if os.name == 'nt': # Check if the os is windows
                name = f'{os.getcwd()}{os.sep}src{os.sep}{name}.{file_ext}' # Set the name to the name
            else:   # If the os is not windows
                name = f'{os.getcwd()}{os.sep}src{os.sep}{name}.{file_ext}'  # Set the name to the name
        
        delete_temp()
        times = 0
        os.system('cls' if os.name == 'nt' else 'clear')    # Clear the screen
        for i in range(5):
            print(f'\u001b[41;1mDecompiling.{"."*times}\u001b[0m', end='\r')  # Print the decompiling message
            time.sleep(random.randint(3, 10)/10) # Sleep for a random amount of time
            times += 1
        print('\t\t\t\t\t\t\t\t\t\t\t', end='\r') # Print a blank line

        try:    # Try to open the file
            with open(name, 'w') as f:  # Open the file
                for line in final:  # For each line in the final
                    if line == '\n' and line == final[final.index(line) + 1]:   # Check if the line is '' and the next line is ''
                        final.remove(line)  # Remove the line
                    elif line == '\t' and line == final[final.index(line) + 1]: # Check if the line is '\t' and the next line is '\t'
                        final.remove(line)  # Remove the line
                    elif line == '   ' and line == final[final.index(line) + 1]:    # Check if the line is '   ' and the next line is '   '
                        final.remove(line)  # Remove the line
                    
                    
                    f.write(line)   # Write the line to the file

        except KeyboardInterrupt:   # If the user presses ctrl + c
            print('\n\u001b[41;1mKeyboard Interrupt Detected\u001b[0m')  # Print the keyboard interrupt detected message
            print('\u001b[1m\u001b[31mDecompile Canclled\u001b[0m') # Print the decompile canclled message
            os.remove(name) # Remove the file
            delete_temp()   # Delete the temp folder
            exit()  # Exit the program

        print('\u001b[32;1mDecompiling Complete\u001b[0m')  # Print the decompiling complete message
        print(f'\u001b[32;1mFile saved to {name}\u001b[0m') # Print the file saved message
        print('\u001b[31;1mDo you want to run the file? (y/n) : \u001b[0m', end='') # Print the question
        if input().lower() == 'y':  # Check if the input is y
            create_temp()
            pass    # If the input is y pass
        else:   # If the input is not y
            delete_temp()
            exit('\u001b[31;1mYOUR FILE IS SAVED!!\u001b[0m')   # Exit the program

    with open(f'{os.getcwd()}{os.sep}temp{os.sep}src{os.sep}{filename_only}.tmp', 'w') as f:  # Open the file
        for line in final:  # For each line in the final
            f.write(line)   # Write the line to the file
    
    if '-o' in sys.argv:    # Check if -o is in the sys.argv
        try:    # Try to open the file
            # rename the file in the temp folder to .py
            # run this command with subprocess pyinstaller --noconfirm --onefile --console --icon "C:/Users/dhruv/Downloads/logo.ico"  "Z:\GitHub\Repos\BrainLuck2.0\versace.py"
            print('\u001b[31;1mDo you want to put an icon for the file? (y/n) : \u001b[0m', end='') # Print the question
            icon_choice = input().lower().strip()
            if icon_choice == 'y':
                print('\u001b[31;1mEnter the icon path ("path\\to\\icon.ico"): \u001b[0m', end='')
                icon = input()
                if icon.count('"') != 2:
                    icon = f'"{icon}"'
            elif icon_choice == 'n':
                icon = ''
            else:
                icon_choice = 'n'
                icon = ''
                
            filepath = f'"{os.getcwd()}{os.sep}temp{os.sep}src{os.sep}{filename_only}.tmp"'
            
            print('\u001b[31;1mWill this be an Window based application or a console based one? (w/c): \u001b[0m', end='')
            window_console = input().lower().strip()
            if window_console == 'w':
                window_console = '--windowed'
            elif window_console == 'c':
                window_console = '--console'
            else:
                window_console = ''  
            
            if icon_choice == 'y':
                command = f'pyinstaller --noconfirm --onefile {window_console} --icon {icon} {filepath}'
            elif icon_choice == 'n':
                command = f'pyinstaller --noconfirm --onefile {window_console} {filepath}'
            else:
                delete_temp()
                exit('\u001b[31;1mInvalid Input\u001b[0m')
                
            # move the .tmp file to the rood dir
            os.system(command)
            # move the exe from the dist folder to the root dir
            # delete the build and dist folder
            try:
                shutil.move(f'{os.getcwd()}{os.sep}dist{os.sep}{filename_only}.exe', f'{os.getcwd()}{os.sep}{filename_only}.exe')
            except FileNotFoundError:
                shutil.move(f'{os.getcwd()}{os.sep}dist{os.sep}{filename_only}', f'{os.getcwd()}{os.sep}{filename_only}')
            
            shutil.rmtree(f'{os.getcwd()}{os.sep}build')
            shutil.rmtree(f'{os.getcwd()}{os.sep}dist')
            os.remove(f'{os.getcwd()}{os.sep}{filename_only}.spec')
            # is something is after the -o in the sys.argv
            try:
                if sys.argv[sys.argv.index('-o') + 1] != '-o':  # Check if the sys.argv is not -o
                    # rename the exe to the name after the -o
                    os.rename(f'{os.getcwd()}{os.sep}{filename_only}.exe', f'{os.getcwd()}{os.sep}{sys.argv[sys.argv.index("-o") + 1]}')
            except IndexError:
                pass
            
            os.system('cls' if os.name == 'nt' else 'clear')
            
            if os.name == 'nt':
                filename_only = filename_only + '.exe'
            
            print('\u001b[32;1mFile Compiled\u001b[0m')
            print(f'\u001b[32;1mFile saved to the root directory as "{filename_only}"\u001b[0m')
            print('\u001b[31;1mDo you want to run the binary compiled file? (y/n) : \u001b[0m', end='')
            
            if input().lower() == 'y':
                if os.name == 'nt':
                    os.system(f'start {filename_only}.exe')
                else:
                    os.system(f'{filename_only}')
            else:
                delete_temp()
                exit('\u001b[31;1mYOUR FILE IS SAVED!!\u001b[0m')
            exit()
            
        except Exception as e:
            raise Exception(e)
        except FileNotFoundError:   # If the file is not found
            raise FileNotFoundError('Failure File not found in the temp dir')    # Raise the file not found error
        except KeyboardInterrupt:   # If the user presses ctrl + c
            raise KeyboardInterrupt('Keyboard Interrupt Detected')  # Raise the keyboard interrupt detected error
        except ModuleNotFoundError:
            raise ModuleNotFoundError('Pyinstaller is not installed, plase install it with "pip install pyinstaller" or "pip3 install pyinstaller"')

    for i in range(20):
        print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n')
        
    os.system('cls' if os.name == 'nt' else 'clear')
    
    def runfile(filename):  # Define the runfile function
        try:    # Try to open the file
            os.system(f'python "{filename}"')  # Run the file

        except Exception:   # If the file is not found
            os.system(f'python3 "{filename}"')  # Run the file

        except KeyboardInterrupt:  # If the user presses ctrl + c
            print(f'\u001b[41m\u001b[30mKeyboard Interrupt Detected\u001b[0m')  # Print the keyboard interrupt detected message
            delete_temp()   # Delete the temp folder
            exit()  # Exit the program
        finally:
            return
        
    
    try:    # Try to open the file
        filename = f"{os.getcwd()}{os.sep}temp{os.sep}src{os.sep}{filename_only}.tmp"
        runfile(filename)   # Run the file

    except Exception:   # If there is an error
        print(f'\u001b[41m\u001b[30mError: {filename} Failed to run.\u001b[0m') # Print the error message
        exit()  # Exit the program

    finally:    # If there is an error or not
        os.remove(f'{os.getcwd()}{os.sep}temp{os.sep}src{os.sep}{filename_only}.tmp') # Remove the file
        delete_temp()   # Delete the temp folder
        exit()  # Exit the program

from rich.syntax import Syntax # Import the syntax from rich

def testType(_type, line):  # Define the testType function
    if _type == 'int':    # Check if the type is string
        line = line.split('=')[-1]  # Split the line by spaces
        line = line.strip() # Strip the line
        if type(eval(line)) == int:  # Check if the type is int
            return True # Return True
        else:  # If the type is not int
            raise Exception(f'{line} is not a int') # Raise an exception

    elif _type == 'str': # Check if the type is string
        line = line.split('=')[-1]  # Split the line by spaces
        line = line.strip() # Strip the line
        # check if line has 2 " or '
        if line.count('"') == 2 or line.count("'") == 2: # Check if the line has 2 " or '
            return True # Return True
        else:  # If the line does not have 2 " or '
            raise Exception(f'{line} is not a string') # Raise an exception

    elif _type == 'float':   # Check if the type is float
        line = line.split('=')[-1]  # Split the line by spaces
        line = line.strip() # Strip the line 
        if type(eval(line)) == float: # Check if the type is float
            return True # Return True
        else:  # If the type is not float
            raise Exception(f'{line} is not a float') # Raise an exception

    elif _type == 'bool':    # Check if the type is bool
        line = line.split('=')[-1]  # Split the line by spaces
        line = line.strip() # Strip the line
        if 'true' in line or 'false' in line:
            if 'true' in line:
                raise Exception(f'Did you mean True?')
            elif 'false' in line:
                raise Exception(f'Did you mean False?')
            
        if type(eval(line)) == bool: # Check if the type is bool
            return True # Return True
        else: # If the type is not bool
            raise Exception(f'{line} is not a bool') # Raise an exception

    elif _type == 'list': # Check if the type is list
        line = line.split('=')[-1]  # Split the line by spaces
        line = line.strip() # Strip the line
        if type(eval(line)) == list: # Check if the type is list
            return True # Return True
        else: # If the type is not list
            raise Exception(f'{line} is not a list') # Raise an exception
    
    elif _type == 'dict':    # Check if the type is dict
        line = line.split('=')[-1]  # Split the line by spaces
        line = line.strip() # Strip the line
        if type(eval(line)) == dict: # Check if the type is dict
            return True # Return True
        else: # If the type is not dict
            raise Exception(f'{line} is not a dict') # Raise an exception
        
    elif _type == 'tuple':    # Check if the type is tuple
        line = line.split('=')[-1]  # Split the line by spaces
        line = line.strip() # Strip the line
        if type(eval(line)) == tuple: # Check if the type is tuple
            return True # Return True
        else: # If the type is not tuple
            raise Exception(f'{line} is not a tuple') # Raise an exception
    
    elif _type == 'set':    # Check if the type is set
        line = line.split('=')[-1]  # Split the line by spaces
        line = line.strip() # Strip the line
        if type(eval(line)) == set: # Check if the type is set
            return True # Return True
        else:  # If the type is not set
            raise Exception(f'{line} is not a set') # Raise an exception
        
    elif _type == 'complex':    # Check if the type is complex
        line = line.split('=')[-1]  # Split the line by spaces
        line = line.strip() # Strip the line
        if type(eval(line)) == complex: # Check if the type is complex
            return True # Return True
        else:  # If the type is not complex
            raise Exception(f'{line} is not a complex') # Raise an exception


class _SYNTAX: # Create the _SYNTAX class
    def CLASS(line): # Define the CLASS function
        global numtabs, final, tab # Define the global variables
        line, numtabs = C.class_(line, numtabs) # Run the class_ function
        final.append(line) # Add the line to the final list
        return # Continue the loop

    def ELSEIF(line): # Define the ELSEIF function
        global numtabs, final, tab # Define the global variables
        line, numtabs = C.else_if(line, numtabs) # Run the else_if function
        final.append(line) # Add the line to the final list
        return # Continue the loop

    def PUBLIC(line): # Define the public function
        global numtabs, final, tab # Define the global variables
        line, numtabs = C.public(line, numtabs) # Run the public function
        final.append(line)
        return

    def PUB(line):  # Define the PUB function
        global numtabs, final, tab # Define the global variables
        line, numtabs = C.public(line, numtabs) # Run the public function
        final.append(line)
        return

    def FUNC(line): # Define the FUNC function
        global numtabs, final, tab # Define the global variables
        line, numtabs = C.func(line, numtabs) # Run the public function
        final.append(line) # Add the line to the final list
        return

    def CATCH(line): # Define the catch function
        global numtabs, final, tab # Define the global variables
        line, numtabs = C.catch(line, numtabs) # Run the public function
        final.append(line) # Add the line to the final list
        return

    def INCLUDE(line): # Define the include function
        global numtabs, final, tab # Define the global variables
        tabs = tab*numtabs # Define the tabs
        
        if line.endswith("||"):
            keepinline = True
            line = line.replace("||", "")
        else:
            keepinline = False
        
        if keepinline:
            final.append(f"{tabs}{include.include(line)}\n") # Add the include statement to the final list
        else:
            if '# --------- Code Start --------- #' not in final:
                final.insert(0, '# --------- Code Start --------- #\n')
            final.append(f"{tabs}{include.include(line)}\n") # Add the include statement to the final list
        return

    def OUT(line):
        global numtabs, final, tab
        io = IO()  # Create an instance of the IOStream class
        tabs = tab*numtabs # Define the tabs
        final.append(f"{tabs}{io.output(line)}") # Add the output statement to the final list
        return

    def IN(line):
        global numtabs, final, tab
        io = IO()  # Create an instance of the IOStream class
        tabs = tab*numtabs # Define the tabs
        final.append(f"{tabs}{io.inp(line, tabs)}\n") # Add the input statement to the final list
        return

    def RETURN(line):
        global numtabs, final, tab
        tabs = tab*numtabs # Define the tabs
        final.append(f"{tabs}{line}\n") # Add the return statement to the final list
        return

    def DEFMAIN(line):
        global numtabs, final, tab
        raise Exception('Line: "def main()", Did you mean "public main()"?') # Raise an exception
    
    def VAR(line):
        global numtabs, final, tab
        tabs = tab*numtabs
        # line may look like: int x = 5 or str x = "Hello World"
        # line needs to become x: int = 5 or x: str = "Hello World"
        def get_type(line):
            # line may look like: int x = 5 or str x = "Hello World"
            # line needs to become int or str
            line = line.split(' ')
            return line[0]
        
        def get_name(line):
            # line may look like: int x = 5 or str x = "Hello World"
            # line needs to become x
            line = line.split(' ')
            return line[1]
        def get_value(line):
            # line may look like: int x = 5 or str x = "Hello World"
            # line needs to become 5 or "Hello World"
            line = line.split('=')
            return line[1]
        
        line = f"{get_name(line)}: {get_type(line)} = {get_value(line)}"
        final.append(f"{tabs}{line}\n")
        return

    def THROW(line):
        global numtabs, final, tab
        tabs = tab*numtabs
        line = line.replace('throw', 'raise')
        final.append(f"{tabs}{line}\n")
        return

    def ASYNC(line):
        global numtabs, final, tab
        tabs = tab*numtabs
        funcname = line.split(' ')[2][:-1]
        async_code = C.asynccode()
        if async_code not in final:
            indexxx = 0
            for i in final:
                if i.startswith("\n") or i.startswith(""):
                    final.insert(indexxx, async_code)
                    break
                indexxx += 1
                
        line, numtabs = C.asyncfunc(line, numtabs) # Run the public function
        line = line.replace('def', f'{tabs}@_async\n{tabs}def')
        final.append(line) # Add the line to the final list
        # locate which line is this line at and insert @_async before it
        return
    
    def GLOBAL(line):
        global numtabs, final, tab
        tabs = tab*numtabs
        line = line.replace('const ', '')
        linetype = line.split(' ')[0]
        if linetype == 'int':
            line = line.replace('int ', '')
            line = line.strip()
            type_ = 'int'
        elif linetype == 'str':
            line = line.replace('str ', '')
            line = line.strip()
            type_ = 'str'
        elif linetype == 'float':
            line = line.replace('float ', '')
            line = line.strip()
            type_ = 'float'
        elif linetype == 'bool':
            line = line.replace('bool ', '')
            line = line.strip()
            type_ = 'bool'
        elif linetype == 'list':
            line = line.replace('list ', '')
            line = line.strip()
            type_ = 'list'
        elif linetype == 'dict':
            line = line.replace('dict ', '')
            line = line.strip()
            type_ = 'dict'
        elif linetype == 'tuple':
            line = line.replace('tuple ', '')
            line = line.strip()
            type_ = 'tuple'
        elif linetype == 'set':
            line = line.replace('set ', '')
            line = line.strip()
            type_ = 'set'
        else:
            raise Exception(f"Unknown type {linetype}")
        
        if testType(type_, line):
            final.insert(0, f"{line}\n")
        else:
            raise Exception(f"Invalid type for {line}")
        return

syntax = {
    'public class' : _SYNTAX.CLASS,
    'func' : _SYNTAX.FUNC,
    'catch' : _SYNTAX.CATCH,
    'include' : _SYNTAX.INCLUDE,
    'pub' : _SYNTAX.PUB,
    'out' : _SYNTAX.OUT,
    'public' : _SYNTAX.PUBLIC,
    'in' : _SYNTAX.IN,
    'retrun' : _SYNTAX.RETURN,
    'throw' : _SYNTAX.THROW,
    'def main' : _SYNTAX.DEFMAIN,
    'async' : _SYNTAX.ASYNC,
    'str' : _SYNTAX.VAR,
    'int' : _SYNTAX.VAR,
    'float' : _SYNTAX.VAR,
    'str' : _SYNTAX.VAR,
    'bool' : _SYNTAX.VAR,
    'list' : _SYNTAX.VAR,
    'dict' : _SYNTAX.VAR,
    'const' : _SYNTAX.GLOBAL,
# TODO: add more syntax keywords here --------------------------------------------------------------------------------------------------------------------------------------------
} # Define the syntax dictionary

def intrepedmode(line): # Define the intrepedmode function
    if line.startswith('out'): # If the line starts with out
        line = line.replace('"', '') # Remove the quotes
        print(f"{line.replace('out < ', '')}") # Print the line
    elif line.startswith('in'): # If the line starts with in 
        line = line.replace('"', '') # Remove the quotes 
        print(f"{line.replace('in > ', '')}") # Print the line 
        input() # Wait for the user to press enter
    elif line.startswith('exit()'): # If the line starts with exit()
        exit() # Exit the program 
    elif line.startswith('clear()'): # If the line starts with clear()
        os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen
    elif line.startswith('help()'): # If the line starts with help()
        print(''' 
only syntax that works in intreped mode is:
    out < "Hello World"
    in > "Hello World"
    exit()
    clear()
    help()

any python syntax will work
variables will not work
functions will not work
classes will not work
anything with more then one line will not work
        ''') # Print the help message
    else: # If the line does not start with any of the above
        try: # Try to run the line
            exec(line) # Run the line
        except Exception as e:  # If there is an error
            print(e) # Print the error
            pass # Pass the error
    return # Return

def lexer(lines=[], 
          filename='', 
          decomplie=False, 
          orglines=[]): # Define the lexer function
    
    global in_module, private_vars, numtabs, final, syntax, main_function_found, noargs, Version # Define the global variables
    newdata = [] # Define the newdata list
    for _line in lines:
        _line = _line.strip()
        if _line.startswith('from'):
            newdata = include._from_Include(_line)
    
    index = 0 # Define the index variable
    for _i in newdata:
        # insert the new data into the lines list from the srart but in the correct order
        lines.insert(index, _i)
        index += 1
    
    index = 0 # Define the index variable
    
    for _formlines in lines:
        if _formlines.startswith('from'):
            lines.remove(_formlines)
    
    orglines.append(lines) # Set the lines variable to the orglines variable
    if noargs == True: # If the noargs variable is True
        print(f"Verscape Interpreter v{Version}") # Print the versin
        print("This also gives you low level access to all variables and functions in Verscae Code") # Print the low level access message
        print('Type "exit()" to exit the interpreter') # Print the exit message
        print('Type "help()" to see the help menu') # Print the help message
        line = ''
        while line != 'exit()': # While the line is not equal to exit
            line = input('>> ') # Get the input
            intrepedmode(line) # Run the lexer function
        print('Exiting...') # Print exiting
        exit() # Exit the program
        
    foundMain = False # Define the foundMain variable
    index = 0   # Define the index
    incomment = False  # Define the incomment variable            
    
    for i in lines:
        index = 0
        if '{' in i:
            index = lines.index(i)
            i = i.strip()            
            if i.startswith('{'):
                i = i.replace('\n', '')
                if i.startswith('{') or i.endswith('{'):
                    lines[index - 1] = lines[index - 1] + ' {'
                    lines[index] = ''
            else:
                continue
        index += 1        
    index = 0
    
    for line in lines:  # For each line in the lines list
        line = line.strip() # Strip the line
        if line.startswith('/*') or line.endswith('/*'): # Check if the line starts with /*
            incomment = True
            line = line.replace('/*', '"""') # Remove the /* from the line
            
        if line.endswith('*/') or line.startswith('*/'): # Check if the line ends with */
            incomment = False
            line = line.replace('*/', '"""') # Remove the /* from the line
            
        if incomment:
            line = line.replace('*', '-')
            
        lines[index] = line # Set the line in the lines list to the line variable

        index += 1  # Add 1 to the index
        
    index = 0   # Define the index

    for line in lines: # For each line in the lines list
        index += 1 # Add 1 to the index variable
        try: # Try to run the code
            if '!' in line:     # Check if the line contains a !   
                if '!' in line.split(' ')[0]: # Check if the ! is in the first word of the line
                    orgvar = line.split(' ')[0].strip() # Set the orgvar variable to the line split by the space and remove the !
                    private_vars.append(orgvar) # Add the orgvar to the private_vars list'
                    newvar = orgvar.replace('!', '') # Remove the ! from the orgvar
                    newvar = f'_{newvar}' # Add a _ in front of the newvar
                    line = line.replace(orgvar, newvar) # Replace the orgvar with the newvar                
                    lines[index-1] = line # Set the line to the line in the lines list
                else: # If the ! is not in the first word of the line
                    for i in private_vars: # For each item in the private_vars list
                        if i in line: # Check if the private variable is in the line
                            line = line.replace(i, f'_{i[:-1]}') # Replace the i with the i with a _ in front of it
                            lines[index-1] = line # Set the line to the line in the lines list
                                        
        except IndexError: # If there is an index error 
            raise Exception('SyntaxError: Unexpected EOF while parsing') # Raise an exception
                 
        if ';' in line: # Check if the line has a ;
            # split the line by the '"' and still keep the '"' in the list
            something = line.split('"').copy() # Set the something variable to the line split by the "
            for i in range(len(something)): # For each item in the something list
                if i % 2 == 0: # Check if the index is even
                    something[i] = something[i].replace(';', '\n') # Remove the ; from the item
            line = '"'.join(something) # Join the something list by the "
            line = line.split('\n') # Split the line by the ;
            for i in line:
                line[line.index(i)] = i.strip() # Remove the spaces from the line

            line = [i for i in line if i != ''] # Remove the '' from the line

            for i in range(len(line)): # For each item in the line
                if line[i] != '': # Check if the item is not ''
                    lines.insert(index+i, line[i]) # Insert the item into the lines list
            lines.remove(lines[index-1]) # Remove the line from the lines list
        # if the line looks like this: name! = "something" remove the ! and add a _ in front of the name so it looks like this: _name = "something", but if the ! is in a string, ignore it
    
    ii = 0 # Define the ii variable
    line2 = '' # Define the line2 variable
    
    newlines = [line.strip() for line in lines] # Remove the spaces from the lines

    for i in sys.argv: # For each item in the sys.argv list
        if i == '-d': # Check if the item is -d
            from rich import console; syntaxprinting = console.Console().print # Set the syntaxprinting variable to the print function
            _syntax = Syntax('\n'.join(newlines), "swift", theme="one-dark", line_numbers=True, background_color="default") # Set the syntax variable to the Syntax class
            print("\n\u001b[1m\u001b[31m----------------- Orginal Verscae Code -----------------\u001b[0m") # Print the orginal verscae code message
            syntaxprinting(_syntax) # Print the syntax

    for line in newlines:  # Loop through the lines
        # replace everything after \\ with nothing
        if line.startswith('\n'): # Check if the line is not empty
            final.append(' ')   # Add a space to the final list

        if '////' in line:
            line = line.replace('////', '18@!%281&*&(&*#(!')

        if line.startswith('//'): # Check if the line starts with //
            line = line.replace('//', '#') # Replace the // with #

        if '//' in line: # Check if the line has a //
            line = line.split('//') # Split the line by the // and set the line to the first item in the list
            line.pop()  # Remove the last item in the list
            line = ''.join(line) # Join the line list by nothing
            line = line.strip() # Remove the spaces from the line

        if '18@!%281&*&(&*#(!' in line: # Check if the line has a 18@!%281&*&(&*#(!
            line = line.replace('18@!%281&*&(&*#(!', '//') # Replace the // with #

        inas = 0    # Define the inas variable
        try: # Try to do this
            # check if the line starts with a keyword from syntax list
            if line.split(' ')[0] in syntax: # Check if the first word in the line is in the syntax list
                fun = syntax.get(line.split(' ')[0]) # Set the fun variable to the syntax dictionary with the first word of the line as the key
                # check how many arguments the function takes
                try:
                    fun(line, orglines) # Run the functio
                    continue
                except Exception as e:
                    fun(line)
                    continue                    
                    
            elif 'else if' in line: # Check if the line has a else if
                _SYNTAX.ELSEIF(line) # Run the ELSEIF function
                            
            elif ': dict' in line: # Check if the line has : dict
                line = line.replace(': dict', '') # Replace
                continue # Continue the loop

            elif ': list' in line: # Check if the line has : tuple
                line = line.replace(': list', '') # Replace
                continue

            elif '{' in line and '}' in line: # Check if the line has a } and a {
                tabs = tab*numtabs # Define the tabs
                final.append(f"{tabs}{line}\n") # Add the line to the final list
                continue

            elif '{' in line: # Check if { is in the line
                line = C.brace(line, numtabs) # Run the brace function
                final.append(line) # Add the line to the final list
                numtabs += 1 # Add 1 to the number of tabs
                pass # Continue the loop

            elif line.endswith('}'): # Check if the line ends with {
                numtabs -= 1 # Subtract 1 from the number of tabs
                line = line.replace('}', '') # Remove the } from the line
                pass # Continue the loop

            else: # If none of the above conditions are met
                tabs = tab*numtabs # Define the tabs
                final.append(f"{tabs}{line}\n") # Add the line to the final list
                continue

        except Exception as e: # If an exception is raised
            IO.error('Traceback: Most Recent Call') # Print the error message
            IO.error(f'Exception: {e}') # Print the error message
            IO.error('  File "temp/src/{}.tmp", line {}'.format(filename, lines.index(line)+1)) # Print the error message
            IO.error('    {}'.format(line)) # Print the error message
            symobol = '^'*len(line) # Define the symbol
            IO.error('    {}'.format(symobol)) # Print the error message
            if 'int main()' in line: IO.error('Did you mean to use "public main()"')
            if 'def main()' in line: IO.error('Did you mean to use "public main()"')
            IO.error('\nError: Failed to build') # Print the error message
            exit()
    
    for i in final:
        if '@_async' in i and C.asynccode() not in final:
                code =  C.asynccode()
                final.insert(0, code)
                final.insert(1, '\n')
    
    if 'from rich import console; print = console.Console().print\n' not in final:
        final.insert(0, 'from rich import console; print = console.Console().print\n')
    
    
    for i in sys.argv: # For each item in the sys.argv list
        if i == '-d': # Check if the item is -d
            print("\n\u001b[1m\u001b[31m----------------- Compiled Python Code -----------------\u001b[0m") # Print the message
            from rich import console; syntaxprinting = console.Console().print # Define the syntaxprinting variable
            from rich.pretty import pprint # Import the pprint function

            _syntax = Syntax(''.join(final), "python", theme="one-dark", line_numbers=True, background_color="default") # Define the syntax variable
            syntaxprinting(_syntax) # Print the syntax

            print("\n\u001b[1m\u001b[31m----------------- Locals -----------------\u001b[0m") # Print the message
            pprint(locals()) # Print the locals

            print("\n\u001b[1m\u001b[31m----------------- Globals -----------------\u001b[0m") # Print the message
            pprint(globals()) # Print the globals

            print("\n\u001b[1m\u001b[31m----------------- Arguments -----------------\u001b[0m") # Print the message
            pprint(sys.argv) # Print the sys.argv list

            print("\n\u001b[1m\u001b[31m----------------- Paths -----------------\u001b[0m") # Print the message
            pprint(sys.path) # Print the sys.path list

            print("\n\u001b[1m\u001b[31m----------------- End of Data -----------------\u001b[0m") # Print the message

            numval = 3 # Define the numval variable
            lineno = 1 # Define the lineno variable

            # self test the new code in a subprocess and check if it works if it does not then print the error message
            create_temp() # Run the create_temp function
            
            with open(f'temp{os.sep}src{os.sep}debug.tmp', 'w') as f: # Open the file in write mode
                f.write(''.join(final)) # Write the final list to the file

            print("\u001b[1m\u001b[31mRunning Self Test...\u001b[0m") # Print the message
            if subprocess.run(['python3', 'temp{}src{}debug.tmp'.format(os.sep, os.sep)], check=False, capture_output=True, text=False, timeout=5, encoding='utf-8', errors='ignore').returncode == 0:
                print("\u001b[1m\u001b[32mTest Success Your Code has no errors\u001b[0m") # Print the message
                pass # Break the loop
            else:
                # get the line only from the error message
                print("\u001b[1m\u001b[31mTest Failed Your Code has errors\u001b[0m") # Print the message
                error = subprocess.run(['python3', 'temp{}src{}debug.tmp'.format(os.sep, os.sep)], check=False, capture_output=True, text=False).stderr.decode('utf-8') # Decode the error message
                error = error.split('\n')[1].split("^")[0].strip() # Split the error message
                for i in final: # For each item in the final list
                    if error in i: # Check if the error is in the line
                        lineno = final.index(i) # Define the lineno variable
                
                orglines.append('') # Add a blank line to the orglines list
                orglines.append('') # Add a new line to the orglines list 
                orglines.append('') # Add 3 empty lines to the orglines list
                
                error = f"{lineno} | {orglines[lineno - 1]}" # Define the error variable
                print(f"\u001b[1m\u001b[31mError Found in line {lineno}:\n\t{error}\u001b[0m") # Print the error message
            
            delete_temp() # Delete the temp folder
             
            print("\u001b[1m\u001b[31mDo you want to create a dmp file? (y/n) : \u001b[0m", end='') # Print the message
            if input().lower() == 'y': # Check if the user input is y
                if not os.path.exists('debug'): # Check if the debug folder exists
                    os.mkdir('debug') # Create the debug folder
                
                with open(filename, 'r') as f2: # Open the file in read mode
                        data = f2.readlines() # Read the file
                        f2.close() # Close the file
                
                with open(f'{os.getcwd()}{os.sep}debug{os.sep}{filename.split(os.sep)[-1]}.dmp', 'w') as f: # Open the file in write mode
                    lineno = 1 # Define the lineno variable
                    numval = 3 # Define the numval variable
                    f.write("========================= RAW Verscae Code ========================\n") # Write to the file
                    for i in newlines: # For each item in the newlines list
                        if lineno > 9: # Check if the lineno is greater than 9
                            numval = 2 # Define the numval variable
                            if lineno+1 > 99: # Check if the lineno is greater than 99
                                numval = 1 # Define the numval variable

                        numspaces = ' '*numval # Define the numspaces variable
                        data = f'{lineno}{numspaces}| {time.strftime("%H:%M:%S")} | {i} \n' # Define the data variable
                        lineno += 1 # Add 1 to the lineno variable
                        f.write(data) # Write to the file

                    f.write("========================= Verscae Code ========================\n") # Write to the file
                    for i in newlines: # For each item in the newlines list
                        if lineno > 9: # Check if the lineno is greater than 9
                            numval = 2 # Define the numval variable
                            if lineno+1 > 99: # Check if the lineno is greater than 99
                                numval = 1 # Define the numval variable

                        numspaces = ' '*numval # Define the numspaces variable
                        data = f'{lineno}{numspaces}| {time.strftime("%H:%M:%S")} | {i} \n' # Define the data variable
                        lineno += 1 # Add 1 to the lineno variable
                        f.write(data) # Write to the file

                    numval = 3 # Define the numval variable
                    lineno = 1 # Define the lineno variable
                    f.write("\n====================== Compiled Python ======================\n") # Write to the file
                    for i in final: # For each item in the final list
                        if lineno > 9: # Check if the lineno is greater than 9
                            numval = 2 # Define the numval variable
                            if lineno+1 > 99: # Check if the lineno is greater than 99
                                numval = 1 # Define the numval variable

                        numspaces = ' '*numval # Define the numspaces variable
                        data = f'{lineno}{numspaces}| {time.strftime("%H:%M:%S")} | {i}' # Define the data variable
                        lineno += 1 # Add 1 to the lineno variable
                        f.write(data) # Write to the file

                    numval = 3 # Define the numval variable
                    lineno = 1 # Define the lineno variable
                    f.write("\n=========================== Locals ==========================\n") # Write to the file
                    for i in locals(): # For each item in the locals
                        data = f'| {i} | {locals()[i]} \n' # Define the data variable
                        f.write(data) # Write to the file

                    f.write("\n========================== Globals ==========================\n") # Write to the file
                    for i in globals(): # For each item in the globals
                        data = f'| {i} | {globals()[i]} \n' # Define the data variable
                        f.write(data) # Write to the file

                    f.write("\n=========================== Modules =========================\n") # Write to the file
                    for i in sys.modules: # For each item in the sys.modules list
                        data = f'| {i} | {sys.modules[i]} \n' # Define the data variable
                        f.write(data) # Write to the file

                    f.write("\n=========================== Path ============================\n") # Write to the file
                    for i in sys.path: # For each item in the sys.path list
                        data = f'| {i} \n' # Define the data variable
                        f.write(data) # Write to the file

                    f.write("\n=========================== Args ============================\n") # Write to the file
                    for i in sys.argv: # For each item in the sys.argv list
                        data = f'| {i} \n' # Define the data variable
                        f.write(data) # Write to the file

                    f.write("\n========================= End of Data ========================\n") # Write to the file
                    f.close() # Close the file
            exit() # Exit the program
        else:
            continue


    if in_module == False: # Check if the in_module variable is False
        for i in final: # Loop through the final list
            if 'def main' in i: # Check if def main is in the line
                args = i.split('(')[1].split(')')[0] # Define the args
                foundMain = True # Define foundMain as True
                continue

            if numtabs != 0: # Check if the number of tabs is not 0
                # figure out which line is the } missing
                def findMissingBrace():
                    for i in newlines:
                        pass

                IO.error('Error: Missing "}"') # Raise an error
                exit()

        if foundMain == False: # Check if foundMain is False
            IO.error('FATEL ERROR:') # Print the error
            IO.error('   No main function found') # Print the error
            IO.error("Failed to compile, exiting...") # Print the error
            exit() # Exit the program

        final.append(f'main({args})') # Add the main function to the final list
        compiler(final, decomplie, filename)
    else: # Else
        in_module = False # Define in_module as False
        return final # Return the final list


def main(filename,
         decomplie): # Define the main function
    # what ever the path of filename is change it to be os independent
    seperator = os.sep
    # check if this dir matches the filename dir
    # os path = /mnt/z/Verscae-Code
    # filename = Z:/Verscae-Code/test.v
    # replace everthing before the filename folder with everything before the os path folder
    if '\\' in filename: # Check if the filename contains a \
        filename = filename.split('\\') # Split the filename by \
    elif '/' in filename: # Check if the filename contains a /
        filename = filename.split('/') # Split the filename by /
    elif seperator in filename: # Check if the filename contains a seperator
        filename = filename.split(seperator) # Split the filename by the seperator

    if type(filename) == list: # Check if the filename is a list
        filename = filename[-1] # Set the filename to the last item in the list

    filename = os.getcwd() + seperator + filename # Set the filename to the current working directory + the filename

    with open(filename, 'r') as f: # Open the file in read mode
        code = f.readlines()    # Read the lines
        f.close # Close the file
    
    orglines = [line.strip() for line in code]  # Strip the lines
    
    if filename == 'selftest.v': # Check if the filename is selftest.v
        os.remove(filename) # Remove the file
        
    lexer(code, filename, decomplie, orglines) # Run the lexer function

def build(filename, 
          music_option, 
          Version, 
          music_path, 
          args=None):    # Define the build function
    
    decomplie = False # Define decomplie as False
    global compare_version # Define the compare_version variable
    try:    # Try to run the code
        for i in sys.argv:  # Loop through the arguments
            if i == '-c':  # Check if the argument is -c
                decomplie = True # Define decomplie as True
    except IndexError: # If there is an IndexError
        pass # Pass
    try:    # Try to run the code
        if Version != compare_version:  # Check if the version is not 3.0.1
            print('\u001b[41;1mYou are using an unsupported version of the compiler, please fix it. The complier will still work but it may not be as stable as the official version.\u001b[0m')
            time.sleep(2)  # Wait 2 seconds
            os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen

        main(filename, decomplie)   # Run the main function

    except KeyboardInterrupt:   # If the user presses ctrl+c
        print('\n\u001b[41;1mKeyboard Interrupt Detected\u001b[0m') # Print the message
        print('\u001b[1m\u001b[31mStopping Build...\u001b[0m')  # Print the message
        time.sleep(2)   # Wait 2 seconds
        print('\u001b[1m\u001b[31mBuild Stopped\u001b[0m')  # Print the message
        delete_temp()   # Run the delete_temp function
        exit()  # Exit the program

def starter(filename, 
            music_option, 
            Version, 
            music_path, 
            argv): # don't change this unless you know what you are doing
    
    try:   # Try to run the code
        sys.argv[1] = filename.replace("'", '') # Remove the .py from the filename
    except IndexError: # If there is an IndexError
        print('\u001b[41;1mNo file specified\u001b[0m') # Print the message
    try:    # Try to run the code
        path = os.getcwd() # Define the path variable as the current working directory
        try:   # Try to run the code
            os.system(f'cd {path}') # Change the directory
        except FileNotFoundError: # If the file is not found
            print('\u001b[41;1mFile not found\u001b[0m') # Print the error
            print('\u001b[41;1mFatel Error Exiting...\u001b[0m') # Print the message
            exit() # Exit the program
        try:
            response = requests.get("https://api.github.com/repos/Ze7111/Verscae-Programing-language/releases/latest")  # Get the latest release
            if response.status_code == 200: # Check if the status code is 200
                print('\u001b[42;1mChecking for updates...\u001b[0m', end='\r') # Print the message
            print('\u001b[42;1mCompleted\u001b[0m                  ', end='\r') # Print the message
            os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen

            if response.json()['tag_name'] != Version:  # Check if the version is not the same as the latest version
                print('\u001b[41;1m This version of Verscae is not supported \u001b[0m')   # Print the message
                print('\u001b[31;1m   Please update to the latest version\u001b[0m') # Print the message
                print('\u001b[31;1m   You can Ctrl+click to open the link in a web browser \u001b[0m')   # Print the message
                print('\u001b[34;1m   https://github.com/Ze7111/Verscae-Programing-language/releases/latest \u001b[0m')  # Print the link
                time.sleep(5)   # Wait 5 seconds
        except KeyError: # If there is a KeyError
            print('\u001b[41;1mError: Could not connect to the internet\u001b[0m') # Print the message
            time.sleep(1)  # Wait 1 second
            pass # Continue the loop

        try: # don't change this either
            if argv[1] != None or argv[1] != '': # don't change this unless you know what you are doing
                build(argv[1], music_option, Version, music_path, argv) # don't change this unless you know what you are doing
                exit() # don't change this unless you know what you are doing
        except IndexError: # don't change this unless you know what you are doing
            build(filename, music_option, Version, music_path) # don't change this unless you know what you are doing
    except KeyboardInterrupt:   # If the user presses ctrl+c
        print('\u001b[41;1mKeyboard Interrupt Detected\u001b[0m')   # Print the message
        delete_temp()   # Run the delete_temp function
        exit()  # Exit the program
    except Exception as e: # If there is an error
        print(f'\u001b[41;1mAn error has occured: {e}\u001b[0m') # Print the message
        exit() # Exit the program

music_path = os.sep.join(__file__.split(os.sep)[:-1]) + os.sep + 'music.mp3' # change to the path of your music file

# if this folder structure:
#  - temp
#   - python
#   - src
# does not exist, create it and then delete it after the program is run

def create_temp():      # Create the temp folder
    global st_time      # Define the st_time variable as global
    st_time = perf_counter()  # Define the st_ti variable as the current time
    try:        # Try to run the code
        os.mkdir('temp')    # Create the temp folder
        os.mkdir('temp/src')    # Create the src folder
    except FileExistsError: # If the folder already exists
        pass    # Continue the loop

def delete_temp():    # Delete the temp folder
    global ed_time  # Define the ed_time variable as global
    ed_time = perf_counter()    # Define the ed_time variable as the current time
    
    if '-f' in sys.argv:    # Check if -f is in the sys.argv list
        os.system('pause')  # Pause the program
    
    try:    # Try to run the code
        shutil.rmtree('temp')   # Delete the temp folder
    except FileNotFoundError:   # If the folder does not exist
        pass    # Continue the loop

def debugmode():
    with open('selftest.v', 'w') as file:
        file.write('public main() {; out < "This is the SELF TEST" < red < newl; in num < "Enter a number: " < endl < green < int; Check.numCheck(num); in string < "Enter a string: " < endl < green < str; Check.stringCheck(string); }; class Check {; func numCheck(num) {; if (num > 0) {; out < "The number is positive" < endl;  }; else if (num < 0) {; out < "The number is negative" < endl; }; else {; out < "The number is zero" < endl; }; return 0; }; func stringCheck(string) {; if (string == "Hello") {; out < "The string is Hello" < endl; }; else {; out < "The string is not Hello" < endl; };return 0; }; }')
        file.close()
    return

def perf_monitor():
    import psutil
    print(f'\u001b[1m\u001b[32mRuntime: {ed_time - st_time}s\u001b[0m')
    # print all the performance data
    print(f'\u001b[1m\u001b[32mTotal Lines: {len(final)}\u001b[0m')
    # get the memory usage
    memory_usage = psutil.virtual_memory().percent
    print(f'\u001b[1m\u001b[32mMemory Usage: {memory_usage}%\u001b[0m')
    # get the disk usage
    disk_usage = psutil.disk_usage('/').percent
    print(f'\u001b[1m\u001b[32mDisk Usage: {disk_usage}%\u001b[0m')
    # check if a debug folder exists
    # get the time in DD-MM-YY HH-MM-SS format 
    import time
    
    def writestart(file):
        data0 = " This file contains the performance data for Verscae "
        data01 = " This file is generated when you run Verscae with the -p argument "
        data02 = " This file may be used by the Performance Analyzer "
        data03 = " Do not delete or modify this file unless you know what you are doing "
        file.write(f"{data0: ^70}\n")
        file.write(f"{data01: ^70}\n")
        file.write(f"{data02: ^70}\n")
        file.write(f"{data03: ^70}\n\n")
        return
    
    def writedata(file):
        data1 = f" Data was generated on {time.strftime('%d/%m/%Y %H:%M:%S', time.localtime())} "
        file.write(f"{data1:-^70}\n")
        data2 = f'Runtime: "{ed_time - st_time}s"'
        file.write(f"1 | {data2:<60}{endsep: >6}\n")
        data3 = f'Total Lines: "{len(final)}"'
        file.write(f"2 | {data3:<60}{endsep: >6}\n")
        data4 = f'Memory Usage: "{memory_usage}%"'
        file.write(f"3 | {data4:<60}{endsep: >6}\n")
        data5 = f'Disk Usage: "{disk_usage}%"'
        file.write(f"4 | {data5:<60}{endsep: >6}\n")
        data6 = f" END OF DATA "
        file.write(f"{data6:-^70}\n\n")
        return
    
    if os.path.exists('debug'):
        if os.path.exists(f'debug{os.sep}performance.rt'):
            with open(f'debug{os.sep}performance.rt', 'r') as file:
                dataformfile = file.readlines()
            with open(f'debug{os.sep}performance.rt', 'a+') as f:
                endsep = "|"
                try:
                    if "This file contains the performance data for Verscae" not in dataformfile[0]:
                        writestart(f)
                except IndexError:
                    writestart(f)
                writedata(f)
                f.close()
        else:
            with open(f'debug{os.sep}performance.rt', 'w') as f:
                endsep = "|"
                writestart(f)
                writedata(f)
                f.close()

try:   # Try to run the code
    if len(sys.argv) == 1:   # If there are more than 2 arguments
        filename = ''
        lexer(filename) # Run the lexer function
        exit()
    try:    # Try to run the code
        if sys.argv[1] == '':   # Check if the first argument is empty
            print('\u001b[31;1mThe filename you put was either invalid or mismathced, enter file to run : \u001b[32;1m', end='')    # Print the message
            filename = input()  # Get the input
            print('\u001b[0m')  # Reset the color
        else:   # If none of the above conditions are met
            filename = sys.argv[1]  # Set the filename to the first argument
    except IndexError:  # If the user does not put any arguments
        print('\u001b[31;1mYou did not put a filename, enter file to run : \u001b[32;1m', end='')   # Print the message
        filename = input()  # Get the input
        print('\u001b[0m')  # Reset the color

    except KeyboardInterrupt:   # If the user presses ctrl+c
        print('\u001b[41;1mKeyboard Interrupt Detected\u001b[0m')   # Print the message
        delete_temp()   # Run the delete_temp function
        exit()  # Exit the program

    if __name__ == '__main__':  # If the file is run directly
        if sys.argv[1] == '-d':    # If the user puts -d as the first argument
            print('\u001b[32;1mDebug mode started\u001b[0m') # Print the message
            debugmode() # Run the debugmode function
            filename = 'selftest.v' # Set the filename to selftest.v
            sys.argv.append('-d')   # Append the filename to the arguments
            pass
        
            """
            All SYS.ARGV Comands
            -p            | Shows performance stats
            -h            | Shows help
            -v            | Shows version
            -d            | Shows debug mode
            -o <filename> | Compiles the file to a .exe file
            -c <filename> | Compiles the file to a .py file
            -cfg          | Opens the config file
            """
                
        for i in sys.argv:  # For every argument
            if '-' in i:   # If the argument starts with a -
                if '-p' in i or '-h' in i or '-v' in i or '-d' in i or '-o' in i or '-c' in i or '-cfg' in i or '-f' in i: # If the argument is -p, -h, -v, -d, -o, -c, or -cfg
                    pass   # Continue the loop
                elif i.count('"') == 2: # If the argument has 2 quotes
                    pass  # Continue the loop
                else:  # If none of the above conditions are met
                    print('\u001b[31;1mInvalid argument provided\u001b[0m') # Print the message 
                    print('\u001b[32;1mWorking arguments:\u001b[0m') # Print the message
                    print('\u001b[32;1m-p            | Shows the performance statistics of the program\u001b[0m') # Print the message
                    print('\u001b[32;1m-d            | Runs the debug mode\u001b[0m') # Print the message
                    print('\u001b[32;1m-v            | Shows the version of the program\u001b[0m') # Print the message
                    print('\u001b[32;1m-h            | Shows the help menu\u001b[0m') # Print the message
                    print('\u001b[32;1m-o <filename> | Compiles the versace code to a binary exe file\u001b[0m') # Print the message
                    print('\u001b[32;1m-c <filename> | Compiles the versace code to a python file\u001b[0m') # Print the message
                    print('\u001b[32;1m-cfg          | Allows you to edit the config file\u001b[0m') # Print the message
                    print('\u001b[32;1m-f            | Forces the program to freeze before exiting\u001b[0m') # Print the message
                    print('\u001b[32;1m*<filename> is an optianl argument\u001b[0m') # Print the message
                    exit()  # Exit the program
        
        try:    # Try to run the code
            for i in sys.argv:  # Loop through the arguments
                if i == '-m':  # Check if the argument is -m
                    music_option = True # Set the music_option to True
                if i == '-h':
                    print('\u001b[41;1mYou can read the entire documentation\u001b[0m')   # Print the message
                    print('\u001b[31;1m  In you browser, just ctrl + click this link\u001b[0m') # Print the message
                    print('\u001b[34;1m  https://github.com/Ze7111/Verscae/wiki \u001b[0m')  # Print the link
                    print('\u001b[31;1m  If you have a question that is not answred there, you can open an issue or email me at \u001b[0m')   # Print the message
                    print('\u001b[31;1m  ze7111@gmail.com \u001b[0m')   # Print the message
                    exit()

                if i == '-v':
                    print(f'\u001b[41;1mYou are using Verscae version {Version}\u001b[0m')
                    exit()
        except IndexError: # If there is an IndexError
            pass   # Continue the loop
        create_temp()   # Run the create_temp function
        starter(filename, music_option, Version, music_path, sys.argv) # don't change this unless you know what you are doing

    else:   # If the file is imported
        print('\u001b[41;1mYou are not allowed to import this file\u001b[0m') # don't change this unless you know what you are doing

except KeyboardInterrupt:   # If the user presses ctrl+c
    print('\u001b[41;1mKeyboard Interrupt Detected\u001b[0m')   # Print the message
    print('\u001b[1m\u001b[31mExiting ...\u001b[0m')  # Print the message
    exit() # Exit the program
    
finally:   # Run this code no matter what
    delete_temp()   # Run the delete_temp function
    for i in sys.argv:  # Loop through the sys.argv list
        if i == '-p':
            perf_monitor()
    if perf_monitor_always_on:
        perf_monitor()