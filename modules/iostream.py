class IOStream:
    def __init__(self):
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
        }
        self.styles = {
            'bold',
            'dim',
            'italic',
            'underline',
            'blink',
            'reverse',
            'hidden'
        }
        self.justify = {
            'left',
            'center',
            'right',
            'justify'
        }
        self.datatypes = {
            'int',
            'float',
            'str'
        }
        self.endtypes = {
            'newl' : r'\n',
            'tab' : r'\t',
            'rw' : r'\r',
            'space' : r' ',
            'endl' : r''
        }
    
    def output(self, text):
        #out < "lamo asf" | endl | green
        line = ''
        
        try : parse = text.split('"')[1] if '"' in text else text.split("'")[1]
        except IndexError: 
            parse = ''       
             
        try : statements = text.split('"')[2] if '"' in text else text.split("'")[2]
        except IndexError: 
            statements = text.split('<')[1].strip()
        try: statements = statements.split('|')
        except IndexError: pass
            
        statements = [statement.strip() for statement in statements]
        statements = [statement for statement in statements if statement != '']
        statements = [statement for statement in statements if statement[0] != ' ']
        statements = [statement for statement in statements if statement[0] != '\n']
        statements = [statement for statement in statements if statement[0] != ' ']
        
        for i in statements:
            line += ','
            if i in self.colors:
                line += f' style="{i}"'
            elif i in self.styles:
                line += f' style="{i}"'
            elif i in self.justify:
                line += f' justify="{i}"'
            elif i in self.endtypes:
                line += f' end="{self.endtypes[i]}"'
            elif i in self.datatypes:
                continue
            else:
                line += f' {i}'
            
        line = line.rstrip(',')
        if '{' or '}' in text:
            additive = text.split('"' or "'")[0]
            additive = additive.split('<')[1].strip()
            line = f'print({additive}"{parse}"{line.strip()})\n'
            return line
        
        else:
            line = f'print("{parse}"{line})\n'
            return line
        
    
    def inp(self, text, tabs):
        line = ''
        # in a < "question" | red
        # print("question", end="", style="red")
        # a = input()
        try : parse = text.split('"')[1] if '"' in text else text.split("'")[1]
        except IndexError: 
            parse = ''       
             
        try : statements = text.split('"')[2] if '"' in text else text.split("'")[2]
        except IndexError: 
            statements = text.split('<')[1].strip()
            
        try: statements = statements.split('|')
        except IndexError: pass
        
        var = text.split(' ')[1]
        
        statements = [statement.strip() for statement in statements]
        statements = [statement for statement in statements if statement != '']
        statements = [statement for statement in statements if statement[0] != ' ']
        statements = [statement for statement in statements if statement[0] != '\n']
        statements = [statement for statement in statements if statement[0] != ' ']
        for i in statements:
            line += ','
            if i in self.colors:
                line += f' style="{i}"'
            elif i in self.styles:
                line += f' style="{i}"'
            elif i in self.justify:
                line += f' justify="{i}"'
            elif i in self.endtypes:
                line += f' end="{self.endtypes[i]}"'
            elif i in self.datatypes:
                continue
            else:
                line += f' {i}'
                
        line = line.rstrip(',')
        line = f'print("{parse}"{line.strip()})\n'
        if 'int' in statements:
            line += f'{tabs}{var} = int(input())'
        elif 'float' in statements:
            line += f'{tabs}{var} = float(input())'
        elif 'str' in statements:
            line += f'{tabs}{var} = str(input())'
        else:
            line += f'{tabs}{var} = input()'
        
        return line   