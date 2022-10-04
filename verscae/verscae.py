from core.backend import main as m
import sys, os
os.system('cls' if os.name == 'nt' else 'clear')


music_option = False # change to False if you don't want want to play music while compling
music_path = 'music.mp3' # change to the path of your music file


try:
    if sys.argv[1] == '':
        print('\u001b[31;1mThe filename you put was either invalid or mismathced, enter file to run : \u001b[32;1m', end='')
        filename = input()
        print('\u001b[0m')
    else:
        filename = sys.argv[1]
except IndexError:
    print('\u001b[31;1mYou did not put a filename, enter file to run : \u001b[32;1m', end='')
    filename = input()
    print('\u001b[0m')



Version = '3.0.1' # don't change this unless you know what you are doing

if __name__ == '__main__': 
    m(filename, music_option, Version, music_path, sys.argv) # don't change this unless you know what you are doing

else: 
    print('\u001b[41;1mYou are not allowed to import this file\u001b[0m') # don't change this unless you know what you are doing