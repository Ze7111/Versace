from core.build import build as b

def main(filename, music_option, Version, music_path, argv):
    try: # don't change this either
        if argv[1] != None or argv[1] != '': # don't change this unless you know what you are doing
            b(argv[1], music_option, Version, music_path, argv[2]) # don't change this unless you know what you are doing
            exit() # don't change this unless you know what you are doing
    except IndexError: # don't change this unless you know what you are doing
        b(filename, music_option, Version, music_path) # don't change this unless you know what you are doing
    