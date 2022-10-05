class Imports:
    def include(line):
        line = line.replace('include', 'import').replace('[', '').replace(']', '')
        
        if '{' in line or '}' in line or '{}' in line:
            print('\u001b[41;1mINVALID SYNTAX\u001b[0m')
            print('\u001b[31;1m You can\'t use {} in include statement.\u001b[0m')
            exit()

        return line
        