from modules.include import Imports as include
from modules.iostream import IOStream as IO
from core.compile import main as compiler

def lexer(lines, filename, decomplie):
    io = IO()
    
    numtabs = 0
    tab = '    '
    
    final = ['from rich import console; print = console.Console().print\n']
    lines = [line.strip() for line in lines]
    lines = [line for line in lines if line != '']
    lines = [line for line in lines if line[0] != '//']
    lines = [line for line in lines if line[0] != '\n']
    
    for line in lines:
        # replace everything after \\ with nothing
        line = line.split('//')[0]
        
        if line.startswith('class'):
            line = line.replace('{', '')
            line = line.strip()
            line += ':'
            final.append(tab * numtabs + line + '\n')
            numtabs += 1
            continue
        
        elif line.startswith('func'):
            if 'repr' in line:
                line = line.replace('repr', '__innit__')
            line = line.replace('func', 'def')
            line = line.replace('{', '')
            line = line.strip()
            line += ':'
            final.append(tab * numtabs + line + '\n')
            numtabs += 1
            
        elif line.startswith('include'):
            tabs = tab*numtabs
            final.append(f"{tabs}{include.include(line)}\n")
        
        elif line.startswith('out'):
            tabs = tab*numtabs
            final.append(f"{tabs}{io.output(line)}")

        elif line.startswith('in'):
            tabs = tab*numtabs
            final.append(f"{tabs}{io.inp(line, tabs)}\n")
            
        elif line.startswith('return'):
            tabs = tab*numtabs
            final.append(f"{tabs}{line}\n")
            
        elif '}' in line:
            numtabs -= 1
            continue
        
        elif '{' in line:
            line = line.replace('{', '')
            line = line.strip()
            line = tab * numtabs + line + ':' + '\n'
            final.append(line)
            numtabs += 1
            continue
        
        else:
            tabs = tab*numtabs
            final.append(f"{tabs}{line}\n")
    
    compiler(final, decomplie, filename)
    
    
def main(filename, decomplie):
    with open(filename, 'r') as f:
        code = f.readlines()
        f.close
    lexer(code, filename, decomplie)