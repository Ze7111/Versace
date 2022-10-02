import os, time
def main(final, decomplie, filename='src\\output.v'):
    os.system('cls' if os.name == 'nt' else 'clear')
    current_time = time.time()
    current_time = time.strftime('%d-%m-%Y %H-%M-%S', time.localtime(current_time))
    
    if decomplie:
        print('\u001b[31;1mWhat do you want to call the new file (file will be save to python folder)? : \u001b[32;1m', end='')
        name = input()
        print('\u001b[0m')
        if name == '':
            name = f'python\\{current_time}.py'
        else:
            name = f'python\\{name}.py'
        
        print('\u001b[41;1mDecompiling...\u001b[0m', end='\r')
        try:
            with open(name, 'w') as f:
                for line in final:
                    if line == '\n' and line == final[final.index(line) + 1]:
                        final.remove(line)
                    elif line == '\t' and line == final[final.index(line) + 1]:
                        final.remove(line)
                    elif line == '   ' and line == final[final.index(line) + 1]:
                        final.remove(line)
                    f.write(line)
        except KeyboardInterrupt:
            print('\n\u001b[41;1mKeyboard Interrupt Detected\u001b[0m')
            print('\u001b[1m\u001b[31mDecompile Canclled\u001b[0m')
            os.remove(name)
            exit()
            
        time.sleep(3)     
        print('\u001b[42;1mDecompiling Complete\u001b[0m')
    
    files = os.listdir('src')
    files.sort()
    for file in files[:-10]:
        os.remove(f'src\\{file}')
    
    with open(f'src\\{current_time}.tmp', 'w') as f:
        for line in final:
            f.write(line)
    try:
        try: os.system(f'python "src\\{current_time}.tmp"')
        except FileNotFoundError: os.system(f'python3 "src\\{current_time}.tmp"')
        except KeyboardInterrupt: print(f'\u001b[41m\u001b[30mKeyboard Interrupt Detected\u001b[0m')
    except: print(f'\u001b[41m\u001b[30mError: {filename} Failed to run.\u001b[0m')
    finally: os.remove(f'src\\{current_time}.tmp')
