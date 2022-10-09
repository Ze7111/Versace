music_option = False # change to False if you don't want want to play music while compling
Version = '4.0.0' # if you change this value, the compiler will cause an error but it will still compile the code

try: # Try to run the main function
    import rich # Import rich
    import playsound # Import playsound
    import os  # Import os
    import subprocess # Import subprocess
    import sys # Import sys
    import time # Import time
    import requests # Import requests
    import shutil # Import shutil
    from sys import exit
    
except ModuleNotFoundError as e: # If the module is not found
    import subprocess # Import subprocess
    for module in e.name.split(', '): # For each module in the error
        subprocess.call(f'pip install {module}', shell=False) # Install the module
    print('\u001b[41;1mRestart the compiler to continue\u001b[0m') # Print a message

os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen
compare_version = Version # Define the compare version
tab = '    ' # Tab
class C: # Class C
    def class_(line, numtabs): # Class class_
        line = line.replace('{', '') # Remove the { from the line
        line = line.strip() # Remove the spaces from the line
        line += ':' # Add a : to the line
        line = ((tab * numtabs) + line + '\n') # Add the line to the final list
        numtabs += 1 # Add 1 to the number of tabs
        return line, numtabs # Add the line to the final list
    
    def else_if(line, numtabs): # define the else if function
        line = line.replace('else if', 'elif') # Replace else if with elif
        line = line.replace('{', '') # Remove the { from the line
        line = line.strip() # Remove the spaces from the line
        line += ':' # Add a : to the line
        line = ((tab * numtabs) + line + '\n') # Add the line to the final list
        numtabs += 1 # Add 1 to the number of tabs
        return line, numtabs # Return the line and the number of tabs
    
    def public(line, numtabs): # Define the public function
        line = line.replace('public', 'def') # Replace public with def
        line = line.replace('{', '') # Remove the { from the line
        line = line.strip() # Remove the spaces from the line
        line += ':' # Add a : to the line
        line = ((tab * numtabs) + line + '\n') # Add the line to the final list
        numtabs += 1 # Add 1 to the number of tabs
        return line, numtabs # Return the line and the number of tabs
     
    def func(line, numtabs): # Define the function function
        if 'repr' in line: # Check if repr is in the line
            line = line.replace('repr', '__innit__') # Replace repr with __innit__
        line = line.replace('func', 'def') # Replace func with def
        line = line.replace('{', '') # Remove the { from the line
        line = line.strip() # Remove the spaces from the line
        line += ':' # Add a : to the line
        line = ((tab * numtabs) + line + '\n') # Add the line to the final list
        numtabs += 1 # Add 1 to the number of tabs
        return line, numtabs # Return the line and the number of tabs
    
    def catch(line, numtabs): # Define the catch function
        line = line.replace('catch', 'except') # Replace catch with except
        line = line.replace('{', '') # Remove the { from the line
        line = line.strip() # Remove the spaces from the line
        line += ':' # Add a : to the line
        line = ((tab * numtabs) + line + '\n') # Add the line to the final list
        numtabs += 1 # Add 1 to the number of tabs
        return line, numtabs # Return the line and the number of tabs
    
    def brace(line, numtabs): # Define the brace function
        line = line.replace('{', '') # Remove the { from the line
        line = line.strip() # Remove the spaces from the line
        line = tab * numtabs + line + ':' + '\n' # Add the line to the final list
        numtabs += 1 # Add 1 to the number of tabs
        return line, numtabs # Return the line and the number of tabs

class include: # Class include
    def include(line): # Define the include function
        line = line.replace('include', 'import').replace('[', '').replace(']', '') # Replace include with import and remove the [ and ]
        
        if '{' in line or '}' in line or '{}' in line: # Check if { or } or {} is in the line
            print('\u001b[41;1mINVALID SYNTAX\u001b[0m') # Print a message
            print('\u001b[31;1m You can\'t use {} in include statement.\u001b[0m') # Print a message
            exit() # Exit the program

        return line # Return the line
 
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
            'bright_red',
            'bright_green',
            'bright_yellow',
            'bright_blue',
            'bright_magenta',
            'bright_cyan',
            'bright_white',
            'bright_black',
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
            'newl' : r'\n',
            'tab' : r'\t',
            'rw' : r'\r',
            'space' : r' ',
            'endl' : r''
        } # Define the endtypes
    
    def output(self, text): # Define the output function
        line = '' # Define the line
        
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
            line = f'print("{parse}"{line})\n' # Set the line to the print statement
            return line # Return the line
    
    def inp(self, text, tabs): # Define the inp function
        line = '' # Define the line
        
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
        line = f'print("{parse}"{line.strip()})\n'  # Set the line to the print statement
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

def compiler(final, decomplie, filename='temp\\src\\output.v'): # Define the compiler function
    os.system('cls' if os.name == 'nt' else 'clear')    # Clear the screen
    current_time = time.time()  # Set the current time
    current_time = time.strftime('%d-%m-%Y %H-%M-%S', time.localtime(current_time)) # Set the current time
    
    if decomplie:   # Check if decomplie is True
        try:    # Try to open the file
            os.mkdir('build')  # Make the build folder
        except FileExistsError:     # If the folder already exists
            pass    # If the folder already exists pass
        
        print('\u001b[31;1mWhat do you want to call the new file (file will be save to python folder)? : \u001b[32;1m', end='') # Print the question
        name = input()  # Set the name to the input
        
        print('\u001b[0m')  # Print the reset color
        
        if name == '':  # Check if the name is ''
            if os.name == 'nt': # Check if the os is windows
                name = f'build\\{current_time}.py' # Set the name to the current time
            else:   # If the os is not windows
                name = f'build/{current_time}.py'  # Set the name to the current time
        else:   # If the name is not ''
            if os.name == 'nt': # Check if the os is windows
                name = f'build\\{name}.py' # Set the name to the name
            else:   # If the os is not windows
                name = f'build/{name}.py'  # Set the name to the name
        
        print('\u001b[41;1mDecompiling...\u001b[0m', end='\r')  # Print the decompiling message
        
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
            
        time.sleep(2)       # Sleep for 2 seconds
        print('\u001b[42;1mDecompiling Complete\u001b[0m')  # Print the decompiling complete message
        print(f'\u001b[42;1mFile saved to {name}\u001b[0m') # Print the file saved message
        
        print('\u001b[31;1mDo you want to run the file? (y/n) : \u001b[0m', end='') # Print the question
        if input().lower() == 'y':  # Check if the input is y
            pass    # If the input is y pass
        else:   # If the input is not y
            delete_temp()
            exit('\u001b[31;1mYOUR FILE IS SAVED!!\u001b[0m')   # Exit the program
    
    files = os.listdir('temp\\src') # Set the files to the files in the src folder
    files.sort()    # Sort the files
    
    for file in files[:-10]:    # For each file in the files
        os.remove(f'temp\\src\\{file}') # Remove the file
    
    if os.name == 'nt': # Check if the os is windows
        with open(f'temp\\src\\{current_time}.tmp', 'w') as f:  # Open the file
            for line in final:  # For each line in the final
                f.write(line)   # Write the line to the file
    else:   # If the os is not windows
        with open(f'temp/src/{current_time}.tmp', 'w') as f:    # Open the file
            for line in final:  # For each line in the final
                f.write(line)   # Write the line to the file
    
    try:    # Try to open the file
        try:    # Try to open the file
            if os.name == 'nt': # Check if the os is windows
                subprocess.call(f'python "temp\\src\\{current_time}.tmp"', shell=False) # Run the file
            else:   # If the os is not windows
                os.system(f'python "temp/src/{current_time}.tmp"') # Run the file
                
        except FileNotFoundError:   # If the file is not found
            if os.name == 'nt': # Check if the os is windows
                subprocess.call(f'python3 "temp\\src\\{current_time}.tmp"', shell=False)    # Run the file
            else:   # If the os is not windows
                os.system(f'python3 "temp/src/{current_time}.tmp"')  # Run the file
                
        except KeyboardInterrupt:  # If the user presses ctrl + c
            print(f'\u001b[41m\u001b[30mKeyboard Interrupt Detected\u001b[0m')  # Print the keyboard interrupt detected message
            delete_temp()   # Delete the temp folder
            exit()  # Exit the program
    
    except Exception:   # If there is an error
        print(f'\u001b[41m\u001b[30mError: {filename} Failed to run.\u001b[0m') # Print the error message
        exit()  # Exit the program
    
    finally:    # If there is an error or not
        os.remove(f'temp\\src\\{current_time}.tmp') # Remove the file
        delete_temp()   # Delete the temp folder
        exit()  # Exit the program

def lexer(lines, filename, decomplie): # Define the lexer function
    io = IO()  # Create an instance of the IOStream class
    
    numtabs = 0 # Define the number of tabs
    tab = '    ' # Define the tab
    foundMain = False # Define the foundMain variable
    
    final = ['from rich import console; print = console.Console().print\n'] # Add the import statement to the final line of the list
    lines = [line.strip() for line in lines] # Remove the spaces from the lines

    for line in lines:  # Loop through the lines
        # replace everything after \\ with nothing
        line = line.split('//')[0] # Remove the comments
        
        if line.startswith('\n'): # Check if the line is not empty
            if line.startswith(''): # Check if the line starts with a tab
                continue    # If the line starts with a tab continue
            if line.startswith('//'):
                continue     
            pass
        
        if line.endswith(';'):  # Check if the line ends with ;
            # remove only the last ;
            line = line[:-1]    # Remove the last ;

        try:
            if line.startswith('class'): # Check if the line starts with class
                line, numtabs = C.class_(line, numtabs) # Run the class_ function
                final.append(line) # Add the line to the final list
                continue # Continue the loop
            
            elif ': dict' in line: # Check if the line has : dict
                line = line.replace(': dict', '') # Replace
                continue
                
            elif ': list' in line: # Check if the line has : tuple
                line = line.replace(': list', '') # Replace
                continue
            
            elif line.startswith('else if'): # Check if the line starts with else if
                line, numtabs = C.else_if(line, numtabs) # Run the else_if function
                final.append(line) # Add the line to the final list
                continue
            
            elif line.startswith('public'): # Check if the line starts with public
                line, numtabs = C.public(line, numtabs) # Run the public function
                final.append(line)
                continue # Continue the loop
            
            elif line.startswith('func'): # Check if the line starts with func 
                line, numtabs = C.func(line, numtabs) # Run the public function
                final.append(line)
                continue # Continue the loop
                
            elif line.startswith('catch'): # Check if the line starts with catch
                line, numtabs = C.catch(line, numtabs) # Run the public function
                final.append(line)
                continue # Continue the loop
                
            elif line.startswith('include'): # Check if the line starts with include
                tabs = tab*numtabs # Define the tabs
                final.append(f"{tabs}{include.include(line)}\n") # Add the include statement to the final list
                continue
            
            elif line.startswith('out'): # Check if the line starts with out
                tabs = tab*numtabs # Define the tabs
                final.append(f"{tabs}{io.output(line)}") # Add the output statement to the final list
                continue

            elif line.startswith('in'): # Check if the line starts with in
                tabs = tab*numtabs # Define the tabs
                final.append(f"{tabs}{io.inp(line, tabs)}\n") # Add the input statement to the final list
                continue
                    
            elif line.startswith('def main'): # Check if the line starts with if
                raise Exception('Main function not found') # Raise an exception
            
            elif line.startswith('return'): # Check if the line starts with return
                tabs = tab*numtabs # Define the tabs
                final.append(f"{tabs}{line}\n") # Add the return statement to the final list
                continue
            
            elif '{' in line and '}' in line: # Check if the line has a } and a {
                tabs = tab*numtabs # Define the tabs
                final.append(f"{tabs}{line}\n") # Add the line to the final list
                continue
            
            elif '}' in line: # Check if } is in the line
                numtabs -= 1 # Subtract 1 from the number of tabs
                line = line.replace('}', '') # Remove the } from the line
                pass # Continue the loop
            
            elif '{' in line: # Check if { is in the line
                line, numtabs = C.brace(line, numtabs) # Run the brace function
                final.append(line) # Add the line to the final list
                pass # Continue the loop
            
            else: # If none of the above conditions are met
                tabs = tab*numtabs # Define the tabs
                final.append(f"{tabs}{line}\n") # Add the line to the final list
                continue
            
        except Exception as e:
            IO.error('Traceback: Most Recent Call') # Print the error message
            IO.error(f'Exception: {e}') # Print the error message
            IO.error('  File "temp/src/{}.tmp", line {}'.format(filename, lines.index(line)+1)) # Print the error message
            IO.error('    {}'.format(line)) # Print the error message
            symobol = '^'*len(line)
            IO.error('    {}'.format(symobol)) # Print the error message
            if 'int main()' in line: IO.error('Did you mean to use "public main()"')
            if 'def main()' in line: IO.error('Did you mean to use "public main()"')
            IO.error('\nError: Failed to build') # Print the error message
            exit()
        
    for i in final: # Loop through the final list
        if 'def main' in i: # Check if def main is in the line
            args = i.split('(')[1].split(')')[0] # Define the args
            foundMain = True # Define foundMain as True
            continue
        
        if numtabs != 0: # Check if the number of tabs is not 0
            IO.error('Error: Missing "}"') # Raise an error
            exit()
        
    if foundMain == False:
        IO.error('FATEL ERROR:') # Print the error
        IO.error('   No main function found') # Print the error
        IO.error('Failed to compile, exiting...') # Print the error
        exit() # Exit the program
    
    final.append(f'main({args})') # Add the main function to the final list
    compiler(final, decomplie, filename) # Compile the code
    
def main(filename, decomplie): # Define the main function
    with open(filename, 'r') as f: # Open the file
        code = f.readlines()    # Read the lines
        f.close # Close the file
    lexer(code, filename, decomplie) # Run the lexer function

def build(filename, music_option, Version, music_path, args=None):    # Define the build function
    decomplie = False
    global compare_version
    try:    # Try to run the code
        for i in sys.argv:  # Loop through the arguments
            if i == '-d':
                decomplie = True
    except IndexError:
        pass
    try:    # Try to run the code
        if Version != compare_version:  # Check if the version is not 3.0.1
            print('\u001b[41;1mYou are using an unsupported version of the compiler, please fix it. The complier will still work but it may not be as stable as the official version.\u001b[0m')
            time.sleep(2)  # Wait 2 seconds
            os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen
         
        if music_option:   # Check if the music option is True
            print('\u001b[32;1mDo you want to play music while compiling? (y/n): \u001b[0m', end='') # Print the question
            inp = input().lower() # Get the input
            
            if inp == 'y':  # Check if the input is y
                subprocess.call(f'start python -m playsound {music_path}', shell=True)  # Play the music
                
                print('\u001b[41;1mPlaying music.\u001b[0m', end='\r')  # Print the message
                time.sleep(0.5) # Wait 0.5 seconds
                print('\u001b[41;1mPlaying music..\u001b[0m', end='\r') # Print the message
                time.sleep(0.5) # Wait 0.5 seconds
                print('\u001b[41;1mPlaying music...\u001b[0m', end='\r')    # Print the message
                time.sleep(0.5) # Wait 0.5 seconds
                print('\u001b[42;1mMusic Started\u001b[0m    ', end='\n')   # Print the message
                time.sleep(4)   # Wait 4 seconds
                for i in range(10): # Loop 10 times
                    print('\u001b[41;1mBuilding' + '.'*i, '\u001b[0m', end='\r')    # Print the message
                    time.sleep(0.5) # Wait 0.5 seconds
                print('\u001b[42;1mBuild Complete\u001b[0m      ', end='\n')    # Print the message
                pass    # Continue the loop
            
            elif inp == 'e':    # Check if the input is e
                exit()  # Exit the program
                
            else:   # If none of the above conditions are met
                pass    # Continue the loop
                    
        main(filename, decomplie)   # Run the main function
        
    except KeyboardInterrupt:   # If the user presses ctrl+c
        print('\n\u001b[41;1mKeyboard Interrupt Detected\u001b[0m') # Print the message
        print('\u001b[1m\u001b[31mStopping Build...\u001b[0m')  # Print the message
        time.sleep(2)   # Wait 2 seconds
        print('\u001b[1m\u001b[31mBuild Stopped\u001b[0m')  # Print the message
        delete_temp()   # Run the delete_temp function
        exit()  # Exit the program

def starter(filename, music_option, Version, music_path, argv): # don't change this unless you know what you are doing
    try:    # Try to run the code
        try:
            response = requests.get("https://api.github.com/repos/Ze7111/Verscae-Programing-language/releases/latest")  # Get the latest release
            if response.status_code == 200: # Check if the status code is 200
                print('\u001b[42;1mChecking for updates...\u001b[0m', end='\r') # Print the message
            print('\u001b[42;1mCompleted\u001b[0m                  ', end='\r') # Print the message
                
            if response.json()['tag_name'] != Version:  # Check if the version is not the same as the latest version
                print('\u001b[41;1mA newer version of Verscae is available\u001b[0m')   # Print the message
                print('\u001b[31;1m  Please update to the latest version\u001b[0m') # Print the message
                print('\u001b[31;1m  You can Ctrl+click to open the link in a web browser \u001b[0m')   # Print the message
                print('\u001b[34;1m  https://github.com/Ze7111/Verscae-Programing-language/releases/latest \u001b[0m')  # Print the link
                time.sleep(5)   # Wait 5 seconds
        except KeyError:
            print('\u001b[41;1mError: Could not connect to the internet\u001b[0m') # Print the message
            time.sleep(1)
            pass

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
    except Exception as e:
        print(f'\u001b[41;1mAn error has occured: {e}\u001b[0m') # Print the message
        exit()

music_path = 'music.mp3' # change to the path of your music file    

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

# if this folder structure:
#  - temp
#   - python
#   - src
# does not exist, create it and then delete it after the program is run

def create_temp():      # Create the temp folder
    try:        # Try to run the code
        os.mkdir('temp')    # Create the temp folder
        os.mkdir('temp/src')    # Create the src folder
    except FileExistsError: # If the folder already exists
        pass    # Continue the loop

def delete_temp():    # Delete the temp folder
    try:    # Try to run the code
        shutil.rmtree('temp')   # Delete the temp folder
    except FileNotFoundError:   # If the folder does not exist
        pass    # Continue the loop

if __name__ == '__main__':  # If the file is run directly
    try:    # Try to run the code
        for i in sys.argv:  # Loop through the arguments
            if i == '-m':
                music_option = True
    except IndexError:
        pass
    create_temp()   # Run the create_temp function
    starter(filename, music_option, Version, music_path, sys.argv) # don't change this unless you know what you are doing

else:   # If the file is imported
    print('\u001b[41;1mYou are not allowed to import this file\u001b[0m') # don't change this unless you know what you are doing
    
delete_temp()   # Run the delete_temp function