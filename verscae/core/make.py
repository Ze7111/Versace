from modules.include import Imports as include # Path: build\compiler.py
from modules.iostream import IOStream as IO # Path: build\compiler.py
from backend.compile import main as compiler # Path: build\compiler.py
from modules.syntax_correcting import C

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