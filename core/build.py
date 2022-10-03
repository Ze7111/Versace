from build.make import main as m

try:
    import rich
    import playsound
    import os
    import sys
    import time
    
except ModuleNotFoundError as e:
    import subprocess
    for module in e.name.split(', '):
        subprocess.call(f'pip install {module}', shell=True)
    print('\u001b[41;1mRestart the compiler to continue\u001b[0m')

os.system('cls' if os.name == 'nt' else 'clear')

def build(filename, music_option, Version, music_path, decomplie=False):
    try:
        if Version != '2.4.5':
            print('\u001b[41;1mYou are using an unsupported version of the compiler, please fix it. The complier will still work but it may not be as stable as the official version.\u001b[0m')
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            
        if music_option:
                print('\u001b[32;1mDo you want to play music while compiling? (y/n): \u001b[0m', end='')
                
                if input().lower() == 'y':
                    os.system(f'start python -m playsound {music_path}')
                    
                    print('\u001b[41;1mPlaying music.\u001b[0m', end='\r')
                    time.sleep(0.5)
                    print('\u001b[41;1mPlaying music..\u001b[0m', end='\r')
                    time.sleep(0.5)
                    print('\u001b[41;1mPlaying music...\u001b[0m', end='\r')
                    time.sleep(0.5)
                    print('\u001b[42;1mMusic Started\u001b[0m    ', end='\n')
                    time.sleep(4)
                    for i in range(10):
                        print('\u001b[41;1mBuilding' + '.'*i, '\u001b[0m', end='\r')
                        time.sleep(0.5)
                    print('\u001b[42;1mBuild Complete\u001b[0m      ', end='\n')
                    pass
                
                else:
                    pass
                    
        
        m(filename, decomplie)
        
    except KeyboardInterrupt:
        print('\n\u001b[41;1mKeyboard Interrupt Detected\u001b[0m')
        print('\u001b[1m\u001b[31mStopping Build...\u001b[0m')
        time.sleep(2)
        print('\u001b[1m\u001b[31mBuild Stopped\u001b[0m')
        exit()
