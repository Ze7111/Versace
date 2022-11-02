import configparser, os, sys, random, time, tempfile

Version = '3.1.0a'   # Define the Version variable as 4.6.6

def makeconfigfile(configpath):
    data = r"""[Core-Config]
music-option = false
version = 3.1.0a
tab-style = "    "

start-indentation-level = 0
do-once = true
start-in-module-mode = false
recurse-from-function = false
no-args-start = false
always-monitor-performance = false
requests-made = 0"""
    if type(configpath) == bool:
        return data
    else:
        with open(configpath, 'w') as f:
            f.write(data)

def installmodules():  # Define the installmodules function
    try:   # Try to run the code
        subprocess.run('pip install rich requests psutil pyinstaller', shell=True)  # Install the modules
    except Exception as e:
        subprocess.run('pip3 install rich requests psutil pyinstaller', shell=True) # Install the modules        

def readconfig():   # Define the readconfig function
    config_obj = configparser.ConfigParser()  # Define the config variable as a ConfigParser object
    configpath = os.getcwd() + os.sep + 'config.ini'  # Define the configpath variable as the current working directory + the config.ini file
    if os.path.exists(configpath):
        pass
    else:
        makeconfigfile(configpath)
        #pass
    
    try:
        config_obj.read(f'{configpath}') # Read the config.ini file
        Core = config_obj["Core-Config"]   # Define the Core variable as the Core-Config section
    except Exception as e:
        os.system("")
        print(f'\u001b[31m' + 'Error: ' + '\u001b[0m' + f'The config file at: {configpath} is corrupted or non-accessible. Will revert to default settings.') # Print an error message
        print('\u001b[31m' + 'Reverting to default settings' + '\u001b[0m')
        print(f"\u001b[31m" + "Error: " + "\u001b[0m" + f"{e}")
        data = makeconfigfile(True)
        # make a temp file with the data
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write(data)
        
        # read the temp file
        config_obj.read(f.name)
        Core = config_obj["Core-Config"]   # Define the Core variable as the Core-Config section
        # delete the temp file
        os.remove(f.name)
        time.sleep(1)
    
    __B__MUSIC__OPTION__ = Core["music-option"] # Define the __B__MUSIC__OPTION__ variable as the music-option option
    __S__TAB__SPACING__ = Core["tab-style"] # Define the __S__TAB__SPACING__ variable as the __S__TAB__SPACING__-style option
    
    __I__NUM__TABS__ = Core["start-indentation-level"] # Define the __I__NUM__TABS__ variable as the start-indentation-level option
    __B__DO__ONCE__ = Core["do-once"]  # Define the __B__DO__ONCE__ variable as the do-once option
    __B__IN__MODULE__ = Core["start-in-module-mode"] # Get the start-in-module-mode value
    __B__RECURSE__ = Core["recurse-from-function"]  # Get the __B__RECURSE__ value
    __B__NO__ARGUMENTS__ = Core["no-args-start"] # Define the __B__NO__ARGUMENTS__ variable as the no-args-start value in the config file
    __B__PERFORMANCE__MONITOR__ = Core["always-monitor-performance"] # Define the __B__PERFORMANCE__MONITOR__ variable as the perf-monitor-always-on value in the config file
    __I__REQUESTS__MADE__ = Core["requests-made"] # Define the __I__REQUESTS__MADE__ variable as the requests-made value in the config file
    
    return __B__MUSIC__OPTION__, __S__TAB__SPACING__, __I__NUM__TABS__, __B__DO__ONCE__, __B__IN__MODULE__, __B__RECURSE__, __B__NO__ARGUMENTS__, __B__PERFORMANCE__MONITOR__, __I__REQUESTS__MADE__ # Return the variables

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

__B__MUSIC__OPTION__, __S__TAB__SPACING__, __I__NUM__TABS__, __B__DO__ONCE__, __B__IN__MODULE__, __B__RECURSE__, __B__NO__ARGUMENTS__, __B__PERFORMANCE__MONITOR__, __I__REQUESTS__MADE__ = readconfig() # Read the config file 

__B__MUSIC__OPTION__ = convert_to_bool(__B__MUSIC__OPTION__) # Define the __B__MUSIC__OPTION__ variable as a boolean
__S__TAB__SPACING__ = __S__TAB__SPACING__.replace('"', '')
__I__NUM__TABS__ = int(__I__NUM__TABS__)  # Convert the __I__NUM__TABS__ variable to an integer
__B__DO__ONCE__ = convert_to_bool(__B__DO__ONCE__) # Convert the __B__DO__ONCE__ variable to a bool
__B__IN__MODULE__ = convert_to_bool(__B__IN__MODULE__) # Convert the __B__IN__MODULE__ variable to a bool
__B__RECURSE__ = convert_to_bool(__B__RECURSE__) # Convert the __B__RECURSE__ variable to a bool
__B__NO__ARGUMENTS__ = convert_to_bool(__B__NO__ARGUMENTS__) # Convert the __B__NO__ARGUMENTS__ variable to a bool
__B__PERFORMANCE__MONITOR__ = convert_to_bool(__B__PERFORMANCE__MONITOR__) # Convert the __B__PERFORMANCE__MONITOR__ variable to a bool
__I__REQUESTS__MADE__ = int(__I__REQUESTS__MADE__) # Convert the __I__REQUESTS__MADE__ variable to an integer
compare_version = Version # Define the compare version

if len(sys.argv) == 1:  # If there are no arguments
    if __B__NO__ARGUMENTS__ == False:
        __B__NO__ARGUMENTS__ = True

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
    import tempfile # Import tempfile
    from sys import exit # Import exit from sys
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

class C: # Class C
    def class_(line, __I__NUM__TABS__): # Class class_
        global __S__TAB__SPACING__
        line.replace('public class', 'class')
        line = line.replace('{', '') # Remove the { from the line
        line = line.strip() # Remove the spaces from the line
        line += ':' # Add a : to the line
        line = ((__S__TAB__SPACING__ * __I__NUM__TABS__) + line + '\n') # Add the line to the final list
        __I__NUM__TABS__ += 1 # Add 1 to the number of tabs
        return line, __I__NUM__TABS__ # Add the line to the final list

    def else_if(line, __I__NUM__TABS__): # define the else if function
        global __S__TAB__SPACING__
        line = line.replace('else if', 'elif') # Replace else if with elif
        line = line.replace('{', '') # Remove the { from the line
        line = line.strip() # Remove the spaces from the line
        line += ':' # Add a : to the line
        line = ((__S__TAB__SPACING__ * __I__NUM__TABS__) + line + '\n') # Add the line to the final list
        __I__NUM__TABS__ += 1 # Add 1 to the number of tabs
        return line, __I__NUM__TABS__ # Return the line and the number of tabs

    def public(line, __I__NUM__TABS__): # Define the public function
        global __S__TAB__SPACING__
        # if __name__ == '__main__':
        if line.startswith('public'): # If the line starts with public
            # remove everyhting inside ()
            line = line.split('(')[0] # Split the line at the (
            line = line.replace('public', 'def') # Replace public with def
            line = line.replace('main', " main()") # Remove the { from the line
        line = line.replace('{', '') # Remove the { from the line
        line = line.strip() # Remove the spaces from the line
        line += ':' # Add a : to the line
        line = ((__S__TAB__SPACING__ * __I__NUM__TABS__) + line + '\n') # Add the line to the final list
        __I__NUM__TABS__ += 1 # Add 1 to the number of tabs
        return line, __I__NUM__TABS__ # Return the line and the number of tabs

    def func(line, __I__NUM__TABS__): # Define the function function
        global __S__TAB__SPACING__
        if 'repr' in line: # Check if repr is in the line
            line = line.replace('repr', '__innit__') # Replace repr with __innit__
        line = line.replace('func', 'def') # Replace func with def
        line = line.replace('{', '') # Remove the { from the line
        line = line.strip() # Remove the spaces from the line
        line += ':' # Add a : to the line
        line = ((__S__TAB__SPACING__ * __I__NUM__TABS__) + line + '\n') # Add the line to the final list
        __I__NUM__TABS__ += 1 # Add 1 to the number of tabs
        return line, __I__NUM__TABS__ # Return the line and the number of tabs

    def asyncfunc(line, __I__NUM__TABS__): # Define the async function
        global __S__TAB__SPACING__
        if 'repr' in line: # Check if repr is in the line
            line = line.replace('repr', '__innit__') # Replace repr with __innit__
        line = line.replace('async', 'def') # Replace func with def
        line = line.replace(' func', '') # Remove the { from the line
        line = line.replace('{', '') # Remove the { from the line
        line = line.strip() # Remove the spaces from the line
        line += ':' # Add a : to the line
        line = ((__S__TAB__SPACING__ * __I__NUM__TABS__) + line + '\n') # Add the line to the final list
        __I__NUM__TABS__ += 1 # Add 1 to the number of tabs
        return line, __I__NUM__TABS__ # Return the line and the number of tabs
    
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
    
    def catch(line, __I__NUM__TABS__): # Define the catch function
        global __S__TAB__SPACING__
        line = line.replace('catch', 'except') # Replace catch with except
        line = line.replace('{', '') # Remove the { from the line
        line = line.strip() # Remove the spaces from the line
        line += ':' # Add a : to the line
        line = ((__S__TAB__SPACING__ * __I__NUM__TABS__) + line + '\n') # Add the line to the final list
        __I__NUM__TABS__ += 1 # Add 1 to the number of tabs
        return line, __I__NUM__TABS__ # Return the line and the number of tabs

    def brace(line, __I__NUM__TABS__): # Define the brace function
        global __S__TAB__SPACING__
        line = line.replace('{', '') # Remove the { from the line
        line = line.strip() # Remove the spaces from the line
        line = __S__TAB__SPACING__ * __I__NUM__TABS__ + line + ':' + '\n' # Add the line to the final list
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
        global data, __B__RECURSE__
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
            __B__RECURSE__ = False
            for _ii in f.readlines():
                data.append(_ii)
                if _ii.startswith('from'):
                    __B__RECURSE__ = True
                    data.pop(-1)
                    include._from_Include(_ii)
                    continue
        
        if __B__RECURSE__:
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
            '__S__TAB__SPACING__' : r'\t',
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
    
    os.system('cls' if os.name == 'nt' else 'clear')    # Clear the screen
    # create a temp file
    tempfilething = tempfile.NamedTemporaryFile(mode='w', delete=False) # Create a temp file
    filename_only = ''
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
                name = f'{os.getcwd()}{os.sep}src{os.sep}{filename_only}.py'  # Set the name to the current time
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

    with open(tempfilething.name, 'w') as f:  # Open the file
        for line in final:  # For each line in the final
            f.write(line)   # Write the line to the file
    
    if '-o' in sys.argv:    # Check if -o is in the sys.argv
        if '-03' in sys.argv:   # Check if -01 is in the sys.argv
            pass
        elif '-02' in sys.argv:   # Check if -01 is in the sys.argv
            pass
        elif '-01' in sys.argv: # Check if -02 is in the sys.argv
            pass
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
            else:
                icon_choice = 'n'
                icon = ''
            
            filepath = tempfilething.name
            # copy filepath to src folder and add .py to the end
            if os.path.exists('src'): pass
            else: os.mkdir('src')
            shutil.copy(filepath, f'{os.getcwd()}{os.sep}src{os.sep}{filename_only}.py')
            filepath = f'{os.getcwd()}{os.sep}src{os.sep}.py'
            
            print('\u001b[31;1mWill this be an Window based application or a console based one? (w/c): \u001b[0m', end='')
            window_console = input().lower().strip()
            if window_console == 'w':
                window_console = '--windowed'
            else:
                window_console = '--console'  
            
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
            if os.name == 'nt':
                # keep only yhe file ext
                filename_only = '.' + filepath.split('.')[-1]
                try:
                    shutil.move(f'{os.getcwd()}{os.sep}dist{os.sep}{filename_only}.exe', f'{os.getcwd()}{os.sep}{filename_only}.exe')
                except FileNotFoundError:
                    shutil.move(f'{os.getcwd()}{os.sep}dist{os.sep}.{filename_only}', f'{os.getcwd()}{os.sep}{filename_only}')
            else:
                filename_only = '.' + filepath.split('.')[-1]
                try:
                    shutil.move(f'{os.getcwd()}{os.sep}dist{os.sep}{filename_only}', f'{os.getcwd()}{os.sep}{filename_only}')
                except FileNotFoundError:
                    shutil.move(f'{os.getcwd()}{os.sep}dist{os.sep}.{filename_only}', f'{os.getcwd()}{os.sep}{filename_only}')
            
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
            
            os.remove(filepath)
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
    
    def errorcalculate(topline):         # Function to calculate the error
        """
            code should do the following:
            There are 2 outputs expected, the top line, and the bottom line (the line we calculate)
            The top line is the line before the error pointing line and looks like this:
            isasn choice < "which question am I doing? (1, 2, 3, 4) : " < int < bold red
            The bottom line is the line with the error and looks like this:
            ^^^^^^^^^^^^^^^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
            notice how only where there is " " is where the char is ~ and the rest is ^
            heres a Second Example:
            out < "What is your name? : " < go < "Hello " < name < "!" < bold red
            ^^^^^^~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^~~~~~~~~^^^^^^^^^^~~~^^^^^^^^^^^
        """
        bottomline = ''    # The bottom line
        char = '"'   # The char to look for
        count = 0   # The count of the char
        in_string = False  # If the char is in a string
        for i in topline:  # Loop through the top line
            if "'" == i: # If the char is a '
                bottomline += '^' # Add a ^ to the bottom line
            else:  # If the char is not a '
                bottomline += ' ' # Add a space to the bottom line
        
        if "'" in topline: # If the char is in the top line
            if '\\' in topline[topline.index("'") - 1:]: # If the char is escaped
                pass # Do nothing
            else: # If the char is not escaped
                bottomline += '\nAdd a \ before the \' so the string would look like this: \\\'' # Add the error message to the bottom line
                return bottomline    # Return the bottom line
         
        bottomline = ''   # Reset the bottom line
        
        for i in range(len(topline)): # Loop through the top line
            if topline[i] == char: # If the char is the char we are looking for
                bottomline += '~' # Add a ~ to the bottom line
                if count == 1: # If the count is 1
                    in_string = False # Set the in string to False
                    count = 0 # Reset the count
                    continue  # Continue the loop
                in_string = True # Set the in string to True
                count += 1 # Add 1 to the count
                continue # Continue the loop
            else: # If the char is not the char we are looking for
                if in_string: # If the char is in a string
                    bottomline += '~' # Add a ~ to the bottom line
                    continue # Continue the loop
                else: # If the char is not in a string
                    bottomline += '^' # Add a ^ to the bottom line
                    continue # Continue the loop
        return bottomline   # Return the bottom line      
    
    def runfile(filename):  # Define the runfile function
        # compile the code in filename, and using the exec node execute it
        os.system("")  # This is to fix the bug in windows where the color doesnt work
        
        with open(filename, 'rb') as f: # Open the file in read binary mode
            code = compile(f.read(), filename, 'exec') # Compile the code in the file
            
        if os.name == 'nt': # If the os is windows
            if os.path.exists(f'{os.getenv("LOCALAPPDATA")}{os.sep}Programs{os.sep}Python'): # If the python folder exists in the localappdata
                exec(code, {'__file__': filename}) # Execute the code
                #os.system('python3 ' + filename)
                print("\u001b[0m") # Reset the color
            else: # If the python folder does not exist in the localappdata
                exec(code, {'__file__': filename}) # Execute the code
                #os.system('python ' + filename) # Run the file
                print("\u001b[0m") # Reset the color
        else: # If the os is not windows
            os.system('python3 ' + filename) # Run the file
            print("\u001b[0m") # reset the color
        return 0 # Return 0 
            
    try:   # Try to run the code
        filename = tempfilething.name # Get the filename of the temp file
        runfile(filename)   # Run the file
    except Exception as e: # If there is an error
        os.system("") # reset the color
        print(f'\u001b[41;1mError: {e}\u001b[0m')  # Print the error
        if 'line' in str(e):   # If the error is a syntax error
            lineno = str(e).split('line')[-1]  # Get the line number
            # remove everything other then the number
            lineno = ''.join([i for i in lineno if i.isdigit()]) # Get the line number
            lineno = int(lineno)   # Convert the line number to an int
        lineerror = final[lineno - 1].strip() # Get the line with the error
        bottomline = errorcalculate(lineerror) # Get the bottom line
        backline = f'Error in line {lineno} : ' # Get the line before the error
        print(f'\u001b[31;1m{backline}\u001b[33m{lineerror}\u001b[0m') # Print the line before the error
        print(f'\u001b[31;1m╰{"─"*(len(backline) - 3) }> {bottomline}\n\n\u001b[0m\u001b[31mThe line number is most likely in between {lineno-2} - {lineno+2}. But the line displayed is the line with the error.\u001b[0m') # Print the bottom line
    finally: # If there is an error or not
        # remove the temp file
        tempfilething.close()  # Close the temp file
        os.remove(filename) # Remove the temp file
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
        global __I__NUM__TABS__, final, __S__TAB__SPACING__ # Define the global variables
        line, __I__NUM__TABS__ = C.class_(line, __I__NUM__TABS__) # Run the class_ function
        final.append(line) # Add the line to the final list
        return # Continue the loop

    def ELSEIF(line): # Define the ELSEIF function
        global __I__NUM__TABS__, final, __S__TAB__SPACING__ # Define the global variables
        line, __I__NUM__TABS__ = C.else_if(line, __I__NUM__TABS__) # Run the else_if function
        final.append(line) # Add the line to the final list
        return # Continue the loop

    def PUBLIC(line): # Define the public function
        global __I__NUM__TABS__, final, __S__TAB__SPACING__ # Define the global variables
        line, __I__NUM__TABS__ = C.public(line, __I__NUM__TABS__) # Run the public function
        final.append(line)
        return

    def PUB(line):  # Define the PUB function
        global __I__NUM__TABS__, final, __S__TAB__SPACING__ # Define the global variables
        line, __I__NUM__TABS__ = C.public(line, __I__NUM__TABS__) # Run the public function
        final.append(line)
        return

    def FUNC(line): # Define the FUNC function
        global __I__NUM__TABS__, final, __S__TAB__SPACING__ # Define the global variables
        line, __I__NUM__TABS__ = C.func(line, __I__NUM__TABS__) # Run the public function
        final.append(line) # Add the line to the final list
        return

    def CATCH(line): # Define the catch function
        global __I__NUM__TABS__, final, __S__TAB__SPACING__ # Define the global variables
        line, __I__NUM__TABS__ = C.catch(line, __I__NUM__TABS__) # Run the public function
        final.append(line) # Add the line to the final list
        return

    def INCLUDE(line): # Define the include function
        global __I__NUM__TABS__, final, __S__TAB__SPACING__ # Define the global variables
        tabs = __S__TAB__SPACING__*__I__NUM__TABS__ # Define the tabs
        
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
        global __I__NUM__TABS__, final, __S__TAB__SPACING__
        io = IO()  # Create an instance of the IOStream class
        tabs = __S__TAB__SPACING__*__I__NUM__TABS__ # Define the tabs
        final.append(f"{tabs}{io.output(line)}") # Add the output statement to the final list
        return

    def IN(line):
        global __I__NUM__TABS__, final, __S__TAB__SPACING__
        io = IO()  # Create an instance of the IOStream class
        tabs = __S__TAB__SPACING__*__I__NUM__TABS__ # Define the tabs
        final.append(f"{tabs}{io.inp(line, tabs)}\n") # Add the input statement to the final list
        return

    def RETURN(line):
        global __I__NUM__TABS__, final, __S__TAB__SPACING__
        tabs = __S__TAB__SPACING__*__I__NUM__TABS__ # Define the tabs
        final.append(f"{tabs}{line}\n") # Add the return statement to the final list
        return

    def DEFMAIN(line):
        global __I__NUM__TABS__, final, __S__TAB__SPACING__
        raise Exception('Line: "def main()", Did you mean "public main()"?') # Raise an exception
    
    def VAR(line):
        global __I__NUM__TABS__, final, __S__TAB__SPACING__
        tabs = __S__TAB__SPACING__*__I__NUM__TABS__
        # line may look like: int x = 5 or str x = "Hello World"
        # line needs to become x: int = 5 or x: str = "Hello World"
        def get_type(line):
            # line may look like: int x = 5 or str x = "Hello World"
            # line needs to become int or str
            line = line.split(' ')
            line = [i for i in line if i != ''] # Remove empty spaces
            line = [i for i in line if i != ' '] # Remove empty spaces
            return line[0] # Return the type
        
        def get_name(line): # Define the get_name function
            # line may look like: int x = 5 or str x = "Hello World"
            # line needs to become x
            line = line.split(' ') # Split the line by spaces
            # remove all empty spaces from the list
            line = [i for i in line if i != ''] # Remove empty spaces
            line = [i for i in line if i != ' '] # Remove empty spaces
            return line[1] # Return the name
         
        def get_value(line):
            # line may look like: int x = 5 or str x = "Hello World"
            # line needs to become 5 or "Hello World"
            line = line.split('=')[1] # Split the line by the = sign and get the second part
            line = line.strip() # Remove the spaces from the start and end of the line
            return line
        
        line = f"{get_name(line)}: {get_type(line)} = {get_value(line)}" # Create the new line
        final.append(f"{tabs}{line}\n") # Add the line to the final list
        return # Continue the loop

    def THROW(line): # Define the throw function
        global __I__NUM__TABS__, final, __S__TAB__SPACING__ # Define the global variables
        tabs = __S__TAB__SPACING__*__I__NUM__TABS__ # Define the tabs
        line = line.replace('throw', 'raise') # Replace throw with raise
        final.append(f"{tabs}{line}\n") # Add the line to the final list
        return # Continue the loop

    def ASYNC(line): # Define the async function
        global __I__NUM__TABS__, final, __S__TAB__SPACING__ # Define the global variables
        tabs = __S__TAB__SPACING__*__I__NUM__TABS__ # Define the tabs
        funcname = line.split(' ')[2][:-1] # Get the function name
        async_code = C.asynccode() # Get the async code
        if async_code not in final: # If the async code is not in the final list
            indexxx = 0 # Define the indexxx variable
            for i in final: # Loop through the final list
                if i.startswith("\n") or i.startswith(""): # If the line starts with a new line or a space
                    final.insert(indexxx, async_code) # Insert the async code
                    break # Break the loop
                indexxx += 1 # Add 1 to the indexxx variable
                
        line, __I__NUM__TABS__ = C.asyncfunc(line, __I__NUM__TABS__) # Run the public function
        line = line.replace('def', f'{tabs}@_async\n{tabs}def')
        final.append(line) # Add the line to the final list
        # locate which line is this line at and insert @_async before it
        return # Continue the loop
    
    def GLOBAL(line): # Define the global function
        global __I__NUM__TABS__, final, __S__TAB__SPACING__ # Define the global variables
        tabs = __S__TAB__SPACING__*__I__NUM__TABS__ # Define the tabs
        line = line.replace('const ', '') # Remove the const from the line
        linetype = line.split(' ')[0] # Get the type of the line
        if linetype == 'int': # If the type is int
            line = line.replace('int ', '') # Remove the int from the line
            line = line.strip() # Remove the spaces from the start and end of the line
            type_ = 'int' # Set the type to int
        elif linetype == 'str': # If the type is str 
            line = line.replace('str ', '') # Remove the str from the line
            line = line.strip() # Remove the spaces from the start and end of the line
            type_ = 'str' # Set the type to str
        elif linetype == 'float': # If the type is float
            line = line.replace('float ', '') # Remove the float from the line
            line = line.strip() # Remove the spaces from the start and end of the line
            type_ = 'float' # Set the type to float
        elif linetype == 'bool': # If the type is bool
            line = line.replace('bool ', '') # Remove the bool from the line
            line = line.strip() # Remove the spaces from the start and end of the line
            type_ = 'bool' # Set the type to bool
        elif linetype == 'list': # If the type is list
            line = line.replace('list ', '') # Remove the list from the line
            line = line.strip() # Remove the spaces from the start and end of the line
            type_ = 'list' # Set the type to list
        elif linetype == 'dict': # If the type is dict
            line = line.replace('dict ', '') # Remove the dict from the line
            line = line.strip() # Remove the spaces from the start and end of the line
            type_ = 'dict' # Set the type to dict
        elif linetype == 'tuple': # If the type is tuple
            line = line.replace('tuple ', '') # Remove the tuple from the line
            line = line.strip()     # Remove the spaces from the start and end of the line
            type_ = 'tuple' # Set the type to tuple
        elif linetype == 'set': # If the type is set
            line = line.replace('set ', '') # Remove the set from the line
            line = line.strip() # Remove the spaces from the start and end of the line
            type_ = 'set' # Set the type to set
        else: # If the type is not any of the above
            raise Exception(f"Unknown type {linetype}") # Raise an exception
        
        if testType(type_, line): # If the type is correct
            final.insert(0, f"{line}\n") # Add the line to the final list
        else: # If the type is not correct
            raise Exception(f"Invalid type for {line}") # Raise an exception
        return # Continue the loop

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
    
    global __B__IN__MODULE__, private_vars, __I__NUM__TABS__, final, syntax, main_function_found, __B__NO__ARGUMENTS__, Version # Define the global variables
    newdata = [] # Define the newdata list
    for _line in lines:
        _line = _line.strip()
        if _line.startswith('from'):
            newdata = include._from_Include(_line)
    
    index = 0 # Define the index variable
    for _i in newdata:
        # insert the new data into the lines list from the srart but in the correct order
        lines.insert(index, _i) # Insert the new data into the lines list
        index += 1 # Add 1 to the index variable
    
    for iii in lines: # For each line in the lines list
        if '::' in iii and ':::' not in iii: # If the line has :: in it
            lines[lines.index(iii)] = iii.replace('::', '.') # Replace the :: with a .
    
    index = 0 # Define the index variable
    
    for _formlines in lines: # For each line in the lines list
        if _formlines.startswith('from'): # If the line starts with from
            lines.remove(_formlines) # Remove the line from the lines list
        elif _formlines.startswith('||'): # If the line starts with ||
            lines[lines.index(_formlines)] = _formlines.replace('||', '') # Replace the || with nothing
    
    orglines.append(lines) # Set the lines variable to the orglines variable
    if __B__NO__ARGUMENTS__ == True: # If the __B__NO__ARGUMENTS__ variable is True
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
    
    for i in lines: # For each line in the lines list
        index = 0 # Set the index variable to 0
        if '{' in i: # If the line has { in it
            index = lines.index(i) # Set the index variable to the index of the line
            i = i.strip()           # Strip the line   
            if i.startswith('{'): # If the line starts with {
                i = i.replace('\n', '') # Remove the new line
                if i.startswith('{') or i.endswith('{'): # If the line starts with { or ends with {
                    lines[index - 1] = lines[index - 1] + ' {' # Add a { to the end of the line
                    lines[index] = '' # Set the line to nothing
            else: # If the line does not start with {
                continue  # Continue the loop
        index += 1 # Add 1 to the index variable            
    index = 0 # Define the index variable
    
    for line in lines:  # For each line in the lines list
        line = line.strip() # Strip the line
        if line.startswith('/*') or line.endswith('/*'): # Check if the line starts with /*
            incomment = True # Set the incomment variable to True
            line = line.replace('/*', '"""') # Remove the /* from the line
            
        if line.endswith('*/') or line.startswith('*/'): # Check if the line ends with */
            incomment = False # Set the incomment variable to False
            line = line.replace('*/', '"""') # Remove the /* from the line
            
        if incomment: # If the incomment variable is True
            line = line.replace('*', '-') # Replace the * with -
            
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

        if '////' in line: # Check if the line has ////
            line = line.replace('////', '18@!%281&*&(&*#(!') # Replace the //// with 18@!%281&*&(&*#(!

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
                tabs = __S__TAB__SPACING__*__I__NUM__TABS__ # Define the tabs
                final.append(f"{tabs}{line}\n") # Add the line to the final list
                continue

            elif '{' in line: # Check if { is in the line
                line = C.brace(line, __I__NUM__TABS__) # Run the brace function
                final.append(line) # Add the line to the final list
                __I__NUM__TABS__ += 1 # Add 1 to the number of tabs
                pass # Continue the loop

            elif line.endswith('}'): # Check if the line ends with {
                __I__NUM__TABS__ -= 1 # Subtract 1 from the number of tabs
                line = line.replace('}', '') # Remove the } from the line
                pass # Continue the loop

            else: # If none of the above conditions are met
                tabs = __S__TAB__SPACING__*__I__NUM__TABS__ # Define the tabs
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
    
    for i in final: # For each item in the final list
        if '@_async' in i and C.asynccode() not in final:   # Check if @_async is in the item and if the async code is not in the final list
                code =  C.asynccode() # Define the code
                final.insert(0, code) # Insert the code into the final list
                final.insert(1, '\n') # Insert a new line into the final list
    
    if 'from rich import console; print = console.Console().print\n' not in final: # Check if the print function is not in the final list
        final.insert(0, 'from rich import console; print = console.Console().print\n') # Insert the print function into the final list
     
    
    for i in sys.argv: # For each item in the sys.argv list
        if i == '-d': # Check if the item is -d
            print("\n\u001b[1m\u001b[31m----------------- Compiled Python Code -----------------\u001b[0m") # Print the message
            from rich import console; syntaxprinting = console.Console().print # Define the syntaxprinting variable
            from rich.pretty import pprint # Import the pprint function

            _syntax = Syntax(''.join(final), "python", theme="one-dark", line_numbers=True, background_color="default") # Define the syntax variable
            syntaxprinting(_syntax) # Print the syntax

            if '-a' in sys.argv: # Check if -p and -a are in the sys.argv list
                print("\n\u001b[1m\u001b[31m----------------- Locals -----------------\u001b[0m") # Print the message
                pprint(locals()) # Print the locals

                print("\n\u001b[1m\u001b[31m----------------- Globals -----------------\u001b[0m") # Print the message
                pprint(globals()) # Print the globals

                print("\n\u001b[1m\u001b[31m----------------- Arguments -----------------\u001b[0m") # Print the message
                pprint(sys.argv) # Print the sys.argv list

                print("\n\u001b[1m\u001b[31m----------------- Paths -----------------\u001b[0m") # Print the message
                pprint(sys.path) # Print the sys.path list
            
            print("\n\u001b[1m\u001b[31m----------------- End of Data -----------------\u001b[0m") # Print the message
            print("\u001b[1m\u001b[31mIf you would like to see more data you can add the '-a' argument also...\u001b[0m\n") # Print the message
            numval = 3 # Define the numval variable
            lineno = 1 # Define the lineno variable

            # self test the new code in a subprocess and check if it works if it does not then print the error message
            create_temp() # Run the create_temp function
            tempfilething2 = tempfile.NamedTemporaryFile(mode='w', delete=False) # Create a temp file
            with open(tempfilething2.name, 'w') as f: # Open the file
                f.write(''.join(final)) # Write the final list to the file

            print("\u001b[1m\u001b[31mRunning Self Test...\u001b[0m") # Print the message
            if subprocess.run(['python3', tempfilething2.name], check=False, capture_output=True, text=False, timeout=5, encoding='utf-8', errors='ignore').returncode == 0:
                print("\u001b[1m\u001b[32mTest Success Your Code has no errors\u001b[0m") # Print the message
                pass # Break the loop
            else:
                # get the line only from the error message
                print("\u001b[1m\u001b[31mTest Failed Your Code has errors\u001b[0m") # Print the message
                error = subprocess.run(['python3', tempfilething2.name], check=False, capture_output=True, text=False).stderr.decode('utf-8') # Decode the error message
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
        else: # Else
            continue # Continue the loop


    if __B__IN__MODULE__ == False: # Check if the __B__IN__MODULE__ variable is False
        for i in final: # Loop through the final list
            if 'def' in i and "main()" in i:
                foundMain = True # Define the foundMain variable
                continue # Continue the loop

            if __I__NUM__TABS__ != 0: # Check if the number of tabs is not 0
                # figure out which line is the } missing
                IO.error('Error: Missing "}"') # Raise an error
                exit() # Exit the program

        if foundMain == False: # Check if foundMain is False
            IO.error('FATEL ERROR:') # Print the error
            IO.error('   No main function found') # Print the error
            IO.error("Failed to compile, exiting...") # Print the error
            exit() # Exit the program
        
        final.append("main()") # Append the main function to the final list
        compiler(final, decomplie, filename) # Call the compiler function
    else: # Else
        __B__IN__MODULE__ = False # Define __B__IN__MODULE__ as False
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
          __B__MUSIC__OPTION__, 
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
            __B__MUSIC__OPTION__, 
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
        try:    # Try to run the code
            line: str   = '' # Define the line variable as a string
            lineno: int = 0 # Define the lineno variable as an integer
            number: int = 0 # Define the number variable as an integer
            with open(os.getcwd() + os.sep + 'config.ini', 'r+') as f: # Open the config.ini file in read and write mode
                lines = f.readlines() # Read the lines
                for i in lines: # Loop through the lines
                    lines[lines.index(i)] = i.strip()   # Strip the lines
                
                for i in lines: # Loop through the lines
                    if 'requests-made' in i.strip(): # Check if requests-made is in the line
                        line = i.strip() # Set the line variable to the line
                        lineno = lines.index(i) # Set the lineno variable to the index of the line
                        break # Break the loop
                number = int(line.split('=')[1]) # Set the number variable to the number in the line
                number += 1 # Add 1 to the number variable
                lines[lineno] = f'requests-made = {number}' # Set the line in the lines list to the new line
                f.seek(0) # Go to the start of the file
                f.write('\n'.join(lines)) # Write the lines to the file
                f.close() # Close the file
                
            if __I__REQUESTS__MADE__ % 10 == 0: # Check if the number of requests made is divisible by 10
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
            else: pass
        except KeyError: # If there is a KeyError
            print('\u001b[41;1mError: Could not connect to the internet\u001b[0m') # Print the message
            time.sleep(1)  # Wait 1 second
            pass # Continue the loop

        try: # don't change this either
            if argv[1] != None or argv[1] != '': # don't change this unless you know what you are doing
                build(argv[1], __B__MUSIC__OPTION__, Version, music_path, argv) # don't change this unless you know what you are doing
                exit() # don't change this unless you know what you are doing
        except IndexError: # don't change this unless you know what you are doing
            build(filename, __B__MUSIC__OPTION__, Version, music_path) # don't change this unless you know what you are doing
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
    pass

def delete_temp():    # Delete the temp folder
    global ed_time  # Define the ed_time variable as global
    ed_time = perf_counter()    # Define the ed_time variable as the current time
    if '-f' in sys.argv:    # Check if -f is in the sys.argv list
        os.system('pause')  # Pause the program
    pass # Continue the loop

def debugmode(): # define debug mode function
    with open('selftest.v', 'w') as file: 
        file.write('public main() {; out < "This is the SELF TEST" < red < newl; in num < "Enter a number: " < endl < green < int; Check.numCheck(num); in string < "Enter a string: " < endl < green < str; Check.stringCheck(string); }; class Check {; func numCheck(num) {; if (num > 0) {; out < "The number is positive" < endl;  }; else if (num < 0) {; out < "The number is negative" < endl; }; else {; out < "The number is zero" < endl; }; return 0; }; func stringCheck(string) {; if (string == "Hello") {; out < "The string is Hello" < endl; }; else {; out < "The string is not Hello" < endl; };return 0; }; }')
        file.close()
    return 

def perf_monitor():
    import psutil; from rich import console; print = console.Console().print
    
    print(f'[green]Runtime: [bold yellow]{ed_time - st_time}s')
    # print all the performance data
    print(f'[green]Total Lines: [bold yellow]{len(final)}')
    # get the memory usage
    memory_usage = psutil.virtual_memory().percent
    print(f'[green]Memory Usage: [bold yellow]{memory_usage}%')
    # get the disk usage
    disk_usage = psutil.disk_usage('/').percent
    print(f'[green]Disk Usage: [bold yellow]{disk_usage}%')
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
            -cfg          | Opens the config file
            -f            | Forces the program to freeze before exiting
            -c <filename> | Compiles the file to a .py file
            -o <filename> | Compiles the file to a .exe file
            -01           | Must be used with -o, and cannot be directly infront of -o, it compiles the file to a single slow-ish .exe file
            -02           | Must be used with -o, and cannot be directly infront of -o, it compiles the file to a faster single directory with a .exe file
            -03           | Must be used with -o, and cannot be directly infront of -o, it compiles the file to a the fastest .exe file, but nested with a lot of directories
            """
        
        argvcommands = [
            '-p', '-h', '-v', '-d', '-o', '-c', '-cfg', '-f', '-01', '-02', '-03'
        ]  # List of all the commands
                
        for i in sys.argv:  # For every argument
            if '-' in i:   # If the argument starts with a -
                if i in argvcommands: # If the argument is -p, -h, -v, -d, -o, -c, or -cfg
                    continue   # Continue the loop

                elif i.count('"') == 2: # If the argument has 2 quotes
                    continue  # Continue the loop

                elif '\\' in i or '/' in i or '//' in i or '\\\\' in i: # If the argument has a \ or a / in it or // or \\
                    continue # Continue the loop

                else:  # If none of the above conditions are met
                    print('\u001b[31;1mInvalid argument provided\u001b[0m') # Print the message 
                    print('\u001b[32;1mWorking arguments:\u001b[0m') # Print the message
                    print('\u001b[32;1m-p            | Shows the performance statistics of the program\u001b[0m') # Print the message
                    print('\u001b[32;1m-d            | Runs the debug mode\u001b[0m') # Print the message
                    print('\u001b[32;1m-v            | Shows the version of the program\u001b[0m') # Print the message
                    print('\u001b[32;1m-h            | Shows the help menu\u001b[0m') # Print the message
                    print('\u001b[32;1m-cfg          | Allows you to edit the config file\u001b[0m') # Print the message
                    print('\u001b[32;1m-f            | Forces the program to freeze before exiting\u001b[0m') # Print the message
                    print('\u001b[32;1m-c <filename> | Compiles the versace code to a python file\u001b[0m') # Print the message
                    print('\u001b[32;1m-o <filename> | Compiles the versace code to a binary exe file\u001b[0m') # Print the message
                    print('\u001b[32;1m  -01**       | Must be used with -o, and cannot be directly infront of -o, it compiles the file to a single slow-ish .exe file\u001b[0m')
                    print('\u001b[32;1m  -02**       | Must be used with -o, and cannot be directly infront of -o, it compiles the file to a faster single directory with a .exe file\u001b[0m')
                    print('\u001b[32;1m  -03**       | Must be used with -o, and cannot be directly infront of -o, it compiles the file to a the fastest .exe file, but nested with a lot of directories\u001b[0m')
            
                    print('\u001b[32;1m*<filename> is an optianl argument\u001b[0m') # Print the message
                    print('\u001b[32;1m**Not implemented yet.\u001b[0m') # Print the message
                    print(f'\u001b[32;1mYou used {i}\u001b[0m') # Print the message
                    exit()  # Exit the program
        
        try:    # Try to run the code
            for i in sys.argv:  # Loop through the arguments
                if i == '-m':  # Check if the argument is -m
                    __B__MUSIC__OPTION__ = True # Set the __B__MUSIC__OPTION__ to True
                if i == '-h': # Check if the argument is -h
                    print('\u001b[41;1mYou can read the entire documentation\u001b[0m')   # Print the message
                    print('\u001b[31;1m  In you browser, just ctrl + click this link\u001b[0m') # Print the message
                    print('\u001b[34;1m  https://github.com/Ze7111/Verscae/wiki \u001b[0m')  # Print the link
                    print('\u001b[31;1m  If you have a question that is not answred there, you can open an issue or email me at \u001b[0m')   # Print the message
                    print('\u001b[31;1m  ze7111@gmail.com \u001b[0m')   # Print the message
                    exit() # Exit the program

                if i == '-v':  # Check if the argument is -v
                    print(f'\u001b[41;1mYou are using Verscae version {Version}\u001b[0m')  # Print the message
                    exit() # Exit the program
                
                if i == '-cfg': # If the argument is -cfg
                    print('\u001b[41;1mOpening config file\u001b[0m') # Print the message
                    configpath = f"config.ini" # Set the configpath to the config.json file
                    if os.path.exists(configpath): # If the config.json file exists
                        os.system(f'start {configpath}') # Open the config.json file
                    else:  # If the config.json file does not exist
                        makeconfigfile(configpath) # Run the makeconfigfile function
                        os.system(f'start {configpath}') # Open the config.json file
                    exit() # Exit the program
                
        except IndexError: # If there is an IndexError
            pass   # Continue the loop
        create_temp()   # Run the create_temp function
        starter(filename, __B__MUSIC__OPTION__, Version, music_path, sys.argv) # don't change this unless you know what you are doing

    else:   # If the file is imported
        print('\u001b[41;1mYou are not allowed to import this file\u001b[0m') # don't change this unless you know what you are doing

except KeyboardInterrupt:   # If the user presses ctrl+c
    print('\u001b[41;1mKeyboard Interrupt Detected\u001b[0m')   # Print the message
    print('\u001b[1m\u001b[31mExiting ...\u001b[0m')  # Print the message
    exit() # Exit the program
    
finally:   # Run this code no matter what
    delete_temp()   # Run the delete_temp function
    for i in sys.argv:  # Loop through the sys.argv list
        if i == '-p':  # If the argument is -p
            perf_monitor() # Run the perf_monitor function
    if __B__PERFORMANCE__MONITOR__: # If the __B__PERFORMANCE__MONITOR__ is True
        perf_monitor()  # Run the perf_monitor function
