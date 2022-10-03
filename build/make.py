from modules.include import Imports as include # Path: build\compiler.py
from modules.iostream import IOStream as IO # Path: build\compiler.py
from core.compile import main as compiler # Path: build\compiler.py

def lexer(lines, filename, decomplie): # Define the lexer function
    io = IO()  # Create an instance of the IOStream class
    
    numtabs = 0 # Define the number of tabs
    tab = '    ' # Define the tab
    foundMain = False # Define the foundMain variable
    
    final = ['from rich import console; print = console.Console().print\n'] # Add the import statement to the final line of the list
    lines = [line.strip() for line in lines] # Remove the spaces from the lines
    lines = [line for line in lines if line != ''] # Remove the empty lines
    lines = [line for line in lines if line[0] != '//'] # Remove the comments
    lines = [line for line in lines if line[0] != '\n'] # Remove the empty lines
    
    for line in lines:  # Loop through the lines
        # replace everything after \\ with nothing
        line = line.split('//')[0] # Remove the comments
        
        if line.startswith('class'): # Check if the line starts with class
            line = line.replace('{', '') # Remove the { from the line
            line = line.strip() # Remove the spaces from the line
            line += ':' # Add a : to the line
            final.append(tab * numtabs + line + '\n') # Add the line to the final list
            numtabs += 1 # Add 1 to the number of tabs
            continue # Continue the loop
        
        elif line.startswith('else if'): # Check if the line starts with else if
            line = line.replace('else if', 'elif') # Replace else if with elif
            line = line.replace('{', '') # Remove the { from the line
            line = line.strip() # Remove the spaces from the line
            line += ':' # Add a : to the line
            final.append(tab * numtabs + line + '\n') # Add the line to the final list
            numtabs += 1 # Add 1 to the number of tabs
        
        elif line.startswith('public'): # Check if the line starts with public
            line = line.replace('public', 'def') # Replace public with def
            line = line.replace('{', '') # Remove the { from the line
            line = line.strip() # Remove the spaces from the line
            line += ':' # Add a : to the line
            final.append(tab * numtabs + line + '\n') # Add the line to the final list
            numtabs += 1 # Add 1 to the number of tabs
            continue # Continue the loop
        
        elif line.startswith('func'): # Check if the line starts with func 
            if 'repr' in line: # Check if repr is in the line
                line = line.replace('repr', '__innit__') # Replace repr with __innit__
            line = line.replace('func', 'def') # Replace func with def
            line = line.replace('{', '') # Remove the { from the line
            line = line.strip() # Remove the spaces from the line
            line += ':' # Add a : to the line
            final.append(tab * numtabs + line + '\n') # Add the line to the final list
            numtabs += 1 # Add 1 to the number of tabs
            
        elif line.startswith('include'): # Check if the line starts with include
            tabs = tab*numtabs # Define the tabs
            final.append(f"{tabs}{include.include(line)}\n") # Add the include statement to the final list
        
        elif line.startswith('out'): # Check if the line starts with out
            tabs = tab*numtabs # Define the tabs
            final.append(f"{tabs}{io.output(line)}") # Add the output statement to the final list

        elif line.startswith('in'): # Check if the line starts with in
            tabs = tab*numtabs # Define the tabs
            final.append(f"{tabs}{io.inp(line, tabs)}\n") # Add the input statement to the final list
            
        elif line.startswith('return'): # Check if the line starts with return
            tabs = tab*numtabs # Define the tabs
            final.append(f"{tabs}{line}\n") # Add the return statement to the final list
            
        elif '}' in line: # Check if } is in the line
            numtabs -= 1 # Subtract 1 from the number of tabs
            continue # Continue the loop
        
        elif '{' in line: # Check if { is in the line
            line = line.replace('{', '') # Remove the { from the line
            line = line.strip() # Remove the spaces from the line
            line = tab * numtabs + line + ':' + '\n' # Add the line to the final list
            final.append(line) # Add the line to the final list
            numtabs += 1 # Add 1 to the number of tabs
            continue # Continue the loop
        
        else: # If none of the above conditions are met
            tabs = tab*numtabs # Define the tabs
            final.append(f"{tabs}{line}\n") # Add the line to the final list
    
    for i in final: # Loop through the final list
        if 'def main' in i: # Check if def main is in the line
            args = i.split('(')[1].split(')')[0] # Define the args
            foundMain = True # Define foundMain as True
        
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