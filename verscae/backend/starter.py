from build.build import build as b # don't change this unless you know what you are doing

def main(filename, music_option, Version, music_path, argv): # don't change this unless you know what you are doing
    try:
        import requests, time

        response = requests.get("https://api.github.com/repos/Ze7111/Verscae-Programing-language/releases/latest")
        if response.status_code == 200:
            print('\u001b[42;1mChecking for updates...\u001b[0m', end='\r')
        print('\u001b[42;1mCompleted\u001b[0m                  ', end='\r')
            
        if response.json()['tag_name'] != Version:
            print('\u001b[41;1mA newer version of Verscae is available\u001b[0m')
            print('\u001b[31;1m  Please update to the latest version\u001b[0m')
            print('\u001b[31;1m  You can Ctrl+click to open the link in a web browser \u001b[0m')
            print('\u001b[34;1m  https://github.com/Ze7111/Verscae-Programing-language/releases/latest \u001b[0m')
            time.sleep(5)
                
        try: # don't change this either
            if argv[1] != None or argv[1] != '': # don't change this unless you know what you are doing
                b(argv[1], music_option, Version, music_path, argv[2]) # don't change this unless you know what you are doing
                exit() # don't change this unless you know what you are doing
        except IndexError: # don't change this unless you know what you are doing
            b(filename, music_option, Version, music_path) # don't change this unless you know what you are doing
    except KeyboardInterrupt:
        print('\u001b[41;1mKeyboard Interrupt Detected\u001b[0m')
    