tab = '    '
class C:
    def class_(line, numtabs):
        line = line.replace('{', '') # Remove the { from the line
        line = line.strip() # Remove the spaces from the line
        line += ':' # Add a : to the line
        line = ((tab * numtabs) + line + '\n') # Add the line to the final list
        numtabs += 1 # Add 1 to the number of tabs
        return line, numtabs # Add the line to the final list
    
    def else_if(line, numtabs):
        line = line.replace('else if', 'elif') # Replace else if with elif
        line = line.replace('{', '') # Remove the { from the line
        line = line.strip() # Remove the spaces from the line
        line += ':' # Add a : to the line
        line = ((tab * numtabs) + line + '\n') # Add the line to the final list
        numtabs += 1 # Add 1 to the number of tabs
        return line, numtabs # Return the line and the number of tabs
    
    def public(line, numtabs):
        line = line.replace('public', 'def') # Replace public with def
        line = line.replace('{', '') # Remove the { from the line
        line = line.strip() # Remove the spaces from the line
        line += ':' # Add a : to the line
        line = ((tab * numtabs) + line + '\n') # Add the line to the final list
        numtabs += 1 # Add 1 to the number of tabs
        return line, numtabs # Return the line and the number of tabs
    
    def func(line, numtabs):
        if 'repr' in line: # Check if repr is in the line
            line = line.replace('repr', '__innit__') # Replace repr with __innit__
        line = line.replace('func', 'def') # Replace func with def
        line = line.replace('{', '') # Remove the { from the line
        line = line.strip() # Remove the spaces from the line
        line += ':' # Add a : to the line
        line = ((tab * numtabs) + line + '\n') # Add the line to the final list
        numtabs += 1 # Add 1 to the number of tabs
        return line, numtabs # Return the line and the number of tabs
    
    def catch(line, numtabs):
        line = line.replace('catch', 'except') # Replace catch with except
        line = line.replace('{', '') # Remove the { from the line
        line = line.strip() # Remove the spaces from the line
        line += ':' # Add a : to the line
        line = ((tab * numtabs) + line + '\n') # Add the line to the final list
        numtabs += 1 # Add 1 to the number of tabs
        return line, numtabs # Return the line and the number of tabs
    
    def brace(line, numtabs):
        line = line.replace('{', '') # Remove the { from the line
        line = line.strip() # Remove the spaces from the line
        line = tab * numtabs + line + ':' + '\n' # Add the line to the final list
        numtabs += 1 # Add 1 to the number of tabs
        return line, numtabs # Return the line and the number of tabs