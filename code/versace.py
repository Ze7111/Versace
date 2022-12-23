# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
#!/usr/bin/env python3

# Github copilot should always use type annotations in this file
# how to use type annotations: https://www.python.org/dev/peps/pep-0484/

"""
This is the Soruce code for the Versace programming language.
This code does kinda not follow PEP8, but it is still readable and understandable.
A lot of code is not commented, but it is still understandable. Most functions and classes have docstrings.

For more information about Versace, please visit the Versace documentation at https://dhruvan.gitbook.io/vs/
RSTAB: TYPE-ANNOTATIONS USED
"""

__VERSION__ = '4.0.0rw'

import sys, os
from os import system as console
from time import perf_counter
from sys import exit
from time import sleep as wait
from subprocess import run as execute
from time import strftime
from tempfile import gettempdir
from subprocess import check_output
from textwrap import wrap
from types import MappingProxyType

_MAP_: MappingProxyType = MappingProxyType
__PASS_LIST__ = sys.argv.copy()
__DEBUG_DATA__: list[str] = []

class __GLOBAL_VARIABLES__():
    __SYNTAX__: tuple[str, ...] = (
    'func',
    'class',
    'include',
    'from',
    'const',
    'else if', # REMOVE THIS
    'async',
    'public',
    'private',
    'out',
    'in',
    'stop',
    'throw',

    'int',
    'float',
    'double',
    'str',
    'usize',
    'bool',
    'list',
    'dict',
    'tuple',
    'set',
    'byte',
    'char',

    'null',
    'true',
    'false',
    )
    __KEYWORDS_NEED_INDENTATION__: tuple[str, ...] = (
    'if',
    'else if',
    'else',
    'for',
    'while',
    'func',
    'public',
    'async',
    'try',
    'catch',
    'finally',
    'class',

    # python keywords that need indentation
    'except',
    'with',
    '{',
    '}',
    '(',
    ')',
    '[',
    ']',
    ',',
    '/*',
    '*/',
    )
    __NON_NORMAL_CHARS__: tuple[str, ...] = (
    ' ' ,
    '@' ,
    '#' ,
    '$' ,
    '%' ,
    '^' ,
    '&' ,
    '*' ,
    '!' ,
    '(' ,
    ')' ,
    '-' ,
    '+' ,
    '=' ,
    '[' ,
    ']' ,
    '{' ,
    '}' ,
    ';' ,
    ':' ,
    ',' ,
    '.' ,
    '<' ,
    '>' ,
    '/' ,
    '?' ,
    '`' ,
    '~' ,
    '|' ,
    '\\',
    )
    __DATA_TYPES__: tuple[str, ...] = (
    'array',
    'arr ',
    'int',
    'float',
    'complex',
    'double',
    'str',
    'usize',
    'bool',
    'list',
    'dict',
    'tuple',
    'set',
    'bytes',
    'char',
    'memoryview',
    'bytearray',
    'frozenset',
    'range',
    'nullType',
    )
    _END_TYPES_: MappingProxyType[str, str] = _MAP_(
        {
        'newl' : r'\n\n',
        'tab' : r'\t',
        'rw' : r'\r',
        'space' : r' ',
        'endl' : r'',
        'erase' : r'\x1b[2K',
        }
    )
    _JUSTIFY_TYPES_: tuple[str, ...] = (
    'left',
    'right',
    'center',
    'justify',
    )
    _COLOR_TYPES_: tuple[str, ...] = (
    # primitive colors
    'red',
    'green',
    'yellow',
    'blue',
    'magenta',
    'cyan',
    'white',
    'black',
    'bold red',
    'bold green',
    'bold yellow',
    'bold blue',
    'bold magenta',
    'bold cyan',
    'bold white',
    'bold black',
    'bright_red',
    'bright_green',
    'bright_yellow',
    'bright_blue',
    'bright_magenta',
    'bright_cyan',
    'bright_white',
    'bright_black',
    )
    _STYLE_TYPES_: tuple[str, ...] = (
    'bold',
    'dim',
    'italic',
    'underline',
    'blink',
    'reverse',
    'hidden',
    'strike',
    )
    __RESERVED_WORDS__: tuple[str, ...] = (
    'if',
    'else if',
    'else',
    'for',
    'while',
    'func',
    'public',
    'async',
    'try',
    'catch',
    'finally',
    'class',
    'include',
    'from',
    'const',
    'out',
    'in',
    'stop',
    'throw',
    'null',
    'True',
    'static',
    'struct',
    'enum',
    'False',
    'set',
    'frozenset',
    'dict',
    'list',
    'tuple',
    'pack',
    'unpack',
    'range',
    'bytearray',
    'memoryview',
    'bytes',
    'char',
    'str',
    'double',
    'complex',
    'float',
    'int',
    'bool',
    'usize',
    'array',
    'arr',
    'nullType',
    'print',
    'input',
    'pyc',
    'exec',
    'alloc',
    'dealloc',
    'exit',
    )
    __OPTIANAL_ARGS_ALLOWED__: tuple[str, str, str, str, str, str, str, str, str] = (
    r'-*- no types -*-',
    r'-*- no color -*-',
    r'-*- no indent -*-',
    r'-*- no main -*-',
    r'-*- no newline -*-',
    r'-*- use py -*-',
    r'-*- use cache -*-',
    r'-*- use exec -*-',
    r'-*- all errors -*-',
    )
    __CHANGE_WORDS__: MappingProxyType[str, str] = _MAP_(
        {
        'null'     : 'None',
        'true'     : 'True',
        'false'    : 'False',
        'nullType' : 'NoneType',
        'catch'    : 'except',
        'throw'    : 'raise',
        'NULL'     : 'None',
        'NULLTYPE' : 'NoneType',
        'NONE'     : 'None',
        'NONETYPE' : 'NoneType',
        }
    )
__OS__: str
__BINARY__: int
__WINDOWS__: bool
__FILE_PATH__: str
__USE_CACHE__: bool
__PYTHON_PATH__: str
__INDENTATION__: str
__NO_INCLUDES__: bool
__VERSACE_PATH__: str
__ALLOW_UPDATE__: bool
__NO_ARGS_START__: bool
__ALLOW_TRACKING__: bool
__KEEP_PERF_DATA__: bool
__BINARY_FILE_EXT__: str
__LINES__: list[str] = []
__NO_VERSION_CHECK__: bool
__TRANSPILE_FILE_EXT__: str
__FINAL_LIST__: list[str] = []
__INDENTATION_LEVEL__: int = 0
__INDENTATION_COUNT__: int = 0
__SPLIT_LIST__: list[list] = []
__CLASSES__: dict[str, dict] = {}
__ALWAYS_MONITOR_PERF_DATA__: bool
__PUBLIC_MAIN_FOUND__: bool = False
__VARIABLES__: dict[str, dict] = {}
__FUNCTIONS__: dict[str, dict] = {}
__PRE_SPLIT_LIST__: list[list] = []
__OVERLOAD_FUNCTION_REG__: dict = {}
__LINES_FROM_FILE_RAW__: list[str] = []
__OPTIANAL_ARGS_IN_FILE__: list[str] = []
__TERMINAL_WIDTH__: int = int(check_output(['tput', 'cols']))
__COLORS__: MappingProxyType[str, str] = _MAP_(
    {
        'red' : '\033[31m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'green' : '\033[32m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'yellow' : '\033[33m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'blue' : '\033[34m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'magenta' : '\033[35m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'cyan' : '\033[36m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'white' : '\033[37m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',

        'bold red' : '\033[1;31m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'bold green' : '\033[1;32m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'bold yellow' : '\033[1;33m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'bold blue' : '\033[1;34m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'bold magenta' : '\033[1;35m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'bold cyan' : '\033[1;36m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'bold white' : '\033[1;37m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',

        'bright_red' : '\033[91m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'bright_green' : '\033[92m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'bright_yellow' : '\033[93m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'bright_blue' : '\033[94m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'bright_magenta' : '\033[95m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'bright_cyan' : '\033[96m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'bright_white' : '\033[97m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',

        'underline' : '\033[4m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'italic' : '\033[3m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'blink' : '\033[5m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'reverse' : '\033[7m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'reset' : '\033[0m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
    }
)

class VersaceCodeBaseError(Exception):
    def __init__(self, message):
        print("\033[1;31mVersaceError: " + message + "\033[0m")
        exit()

def overload(func) -> object:
    """Overload decorator"""
    def overloader(*args, **kwargs):
        # TODO : Implement a proper overload decorator.
        return func(*args, **kwargs)
    return overloader
@overload
def overload_atter(func) -> object:
    """Overload decorator for gets"""
    def overloader(*args, **kwargs):
        # TODO : Implement a proper overload decorator.
        return func(*args, **kwargs)
    return overloader
@overload
def property(func) -> object:
    """Overload decorator for properties"""
    def overloader(*args, **kwargs):
        # TODO : Implement a proper overload decorator.
        return func(*args, **kwargs)
    return overloader

class __DISPATCH__(object):
    def __init__(self, NAME):
        self.NAME = NAME
        self.__TYPE_MAP__ = {}
    def __call__(self, *ARGUMENTS):
        __TYPES__ = tuple(argument.__class__ for argument in ARGUMENTS) # a generator expression!
        FUNCTION = self.__TYPE_MAP__.get(__TYPES__)
        if FUNCTION is None:
            VersaceCodeBaseError(f"No registered function for types \"{__TYPES__}\"")
        return FUNCTION(*ARGUMENTS)
    def __register__(self, __TYPES__, FUNCTION):
        if __TYPES__ in self.__TYPE_MAP__:
            VersaceCodeBaseError(f"Duplicate registration for function \"{FUNCTION.__name__}\"")
        self.__TYPE_MAP__[__TYPES__] = FUNCTION
@overload
def OVERLOAD(*__TYPES__):
    def __register__(FUNCTION):
        NAME = FUNCTION.__name__
        __D_INST__ = __OVERLOAD_FUNCTION_REG__.get(NAME)
        if __D_INST__ is None:
            __D_INST__ = __OVERLOAD_FUNCTION_REG__[NAME] = __DISPATCH__(NAME)
        __D_INST__.__register__(__TYPES__, FUNCTION)
        return __D_INST__
    return __register__

@overload_atter
def __GET_OS__() -> str and bool:
    """Get the operating system"""
    global __WINDOWS__, __OS__
    try:
        import msvcrt
        __WINDOWS__ = True
        __OS__ = 'Windows'
    except ImportError:
        __WINDOWS__ = False
        __OS__ = 'Linux' if sys.platform.startswith('linux') else 'MacOS' 
    return __OS__, __WINDOWS__   
@overload_atter
def __LINE_0__() -> str:
    """Returns the starting line that should go in every compiled file"""
    global __INDENTATION__
    DATA = f"""# -*- coding: utf-8 -*-
# THIS FILE WAS GENERATED BY VERSACE {__VERSION__}
# Versace can be found here: "https://github.com/Ze7111/Verscae-Programing-language/"
# Versace Documentation can be found here: "https://dhruvan.gitbook.io/vs/"
\"\"\"
--------------------------------------------------------------------------------
    DO NOT EDIT THIS CODE THIS SECTION OF CODE OR THE LINES ABOVE THIS,
                       AUTO GENERATED BY VERSACE.
--------------------------------------------------------------------------------
\"\"\"
from rich import console; print = console.Console().print
from sys import exit, getsizeof
import sys
from threading import Thread
from time import sleep as wait
from dataclasses import dataclass
from typing import Final
from psutil import virtual_memory
__ALLOCATED_MEMORY_ARRAY__ = []
__FREE_MEMORY__ = (virtual_memory().free / (1024 * 1024)) - 1024
_FROZENSET_ = frozenset
def _async(func):
{__INDENTATION__*1}\"\"\" This is a decorator for async functions \"\"\"
{__INDENTATION__*1}def wrapper(*args, **kwargs):
{__INDENTATION__*2}\"\"\" This is the wrapper function that will be returned \"\"\"
{__INDENTATION__*2}thread = Thread(target=func, args=args, kwargs=kwargs)
{__INDENTATION__*2}thread.start()
{__INDENTATION__*2}return thread
{__INDENTATION__*1}return wrapper
with open(__file__, 'r') as f:
{__INDENTATION__*1}__THIS_FILE_DATA__ = f.readlines()
if 'Versace' not in __THIS_FILE_DATA__[2]:
{__INDENTATION__*1}exit()
if 'https' not in __THIS_FILE_DATA__[2]:
{__INDENTATION__*1}exit()
if 'Ze7111' not in __THIS_FILE_DATA__[2]:
{__INDENTATION__*1}exit()
if 'GENERATED' not in __THIS_FILE_DATA__[1]:
{__INDENTATION__*1}exit()
if 'coding' not in __THIS_FILE_DATA__[0]:
{__INDENTATION__*1}raise UnicodeError('This file is corrupted, please do not modify the section of code that specifies that it is auto generated by Versace')
def pack(*args, **kwargs) -> tuple:
{__INDENTATION__*1}\"\"\" Packs any given data into a tuple \"\"\"
{__INDENTATION__*1}if not args and not kwargs:
{__INDENTATION__*2}return (None)
{__INDENTATION__*1}if not args:
{__INDENTATION__*2}return kwargs
{__INDENTATION__*1}if not kwargs:
{__INDENTATION__*2}return args
{__INDENTATION__*1}return args, kwargs
def unpack(args, **kwargs) -> ...:
{__INDENTATION__*1}\"\"\" Unpacks any packed data, so they can be assigned to variables \"\"\"
{__INDENTATION__*1}if not args and not kwargs:
{__INDENTATION__*2}return (None)
{__INDENTATION__*1}if not args:
{__INDENTATION__*2}return kwargs
{__INDENTATION__*1}if not kwargs:
{__INDENTATION__*2}return args
{__INDENTATION__*1}return args, kwargs
def frozenset(*args, **kwargs) -> _FROZENSET_:
{__INDENTATION__*1}\"\"\" Converts any given data to a frozenset \"\"\"
{__INDENTATION__*1}return __builtins__.frozenset(args)
def exec(*args, **kwargs) -> None:
{__INDENTATION__*1}\"\"\" Executes any given code \"\"\"
{__INDENTATION__*1}if not args and not kwargs:
{__INDENTATION__*2}return (None)
{__INDENTATION__*1}for i in args:
{__INDENTATION__*2}exec(i, globals())
def alloc(size=None, output=None, sep=None) -> int | str:
{__INDENTATION__*1}__ALLOCATE__ = size
{__INDENTATION__*1}if __ALLOCATE__ is None: raise ValueError('No ammout of memory provided to allocate')
{__INDENTATION__*1}if sep is None: sep = ','
{__INDENTATION__*1}global __ALLOCATED_MEMORY_ARRAY__, __FREE_MEMORY__
{__INDENTATION__*1}if __ALLOCATE__ > __FREE_MEMORY__: raise MemoryError(f'Not enough memory to allocate {{__ALLOCATE__:,}} MB, only {{int(__FREE_MEMORY__):,}} MB available')
{__INDENTATION__*1}if type(__ALLOCATE__) is not int: raise TypeError('Ammout of memory to allocate must be an integer')
{__INDENTATION__*1}if type(__ALLOCATED_MEMORY_ARRAY__) is not list: __ALLOCATED_MEMORY_ARRAY__ = []
{__INDENTATION__*1}__ALLOCATE__ = __ALLOCATE__ * 7710 * 17
{__INDENTATION__*1}__ALLOCATED_MEMORY_ARRAY__  = [0] * __ALLOCATE__
{__INDENTATION__*1}if output is None: return getsizeof(__ALLOCATED_MEMORY_ARRAY__)
{__INDENTATION__*1}elif output == str: 
{__INDENTATION__*2}__ALLOCATE__ = getsizeof(__ALLOCATED_MEMORY_ARRAY__)
{__INDENTATION__*2}if __ALLOCATE__ > 1024 * 1024 * 1024 * 1024:
{__INDENTATION__*3}__ALLOCATE__ = __ALLOCATE__ / (1024 * 1024 * 1024 * 1024)
{__INDENTATION__*3}__ALLOCATE__ = round(__ALLOCATE__, 2)
{__INDENTATION__*3}return f'{{__ALLOCATE__:{{sep}}}} TB'
{__INDENTATION__*2}elif __ALLOCATE__ > 1024 * 1024 * 1024:
{__INDENTATION__*3}__ALLOCATE__ = __ALLOCATE__ / (1024 * 1024 * 1024)
{__INDENTATION__*3}__ALLOCATE__ = round(__ALLOCATE__, 2)
{__INDENTATION__*3}return f'{{__ALLOCATE__:{{sep}}}} GB'
{__INDENTATION__*2}elif __ALLOCATE__ > 1024 * 1024:
{__INDENTATION__*3}__ALLOCATE__ = __ALLOCATE__ / (1024 * 1024)
{__INDENTATION__*3}__ALLOCATE__ = round(__ALLOCATE__, 2)
{__INDENTATION__*3}return f'{{__ALLOCATE__:{{sep}}}} MB'
{__INDENTATION__*2}elif __ALLOCATE__ > 1024:
{__INDENTATION__*3}__ALLOCATE__ = __ALLOCATE__ / 1024
{__INDENTATION__*3}__ALLOCATE__ = round(__ALLOCATE__, 2)
{__INDENTATION__*3}return f'{{__ALLOCATE__:{{sep}}}} KB'
{__INDENTATION__*2}else:
{__INDENTATION__*3}__ALLOCATE__ = round(__ALLOCATE__, 2)
{__INDENTATION__*3}return f'{{__ALLOCATE__:{{sep}}}} Bytes'
{__INDENTATION__*1}elif output == list:
{__INDENTATION__*2}# raise a exception informing the use THAT THEY ARE NOT SUPPOSED TO USE THIS FUNCTION
{__INDENTATION__*2}raise NotImplementedError('Using this WILL cause memory leaks, DO NOT USE')
{__INDENTATION__*1}elif output == int:
{__INDENTATION__*2}return getsizeof(__ALLOCATED_MEMORY_ARRAY__)
{__INDENTATION__*1}else:
{__INDENTATION__*2}raise TypeError('Invalid output type')
def dealloc(size=None, output=None, sep=None) -> int | str:
{__INDENTATION__*1}__DEALLOCATE__ = size
{__INDENTATION__*1}global __ALLOCATED_MEMORY_ARRAY__, __FREE_MEMORY__
{__INDENTATION__*1}if sep is None: sep = ','
{__INDENTATION__*1}__DEALLOCATE__ = (__DEALLOCATE__ * 7710 * 17) if __DEALLOCATE__ is not None else None
{__INDENTATION__*1}if __DEALLOCATE__ is None: __DEALLOCATE__ = len(__ALLOCATED_MEMORY_ARRAY__)
{__INDENTATION__*1}if __DEALLOCATE__ / 7710 / 17 > __FREE_MEMORY__: raise MemoryError(f'Not enough memory to deallocate {{__DEALLOCATE__:,}} MB, only {{int(__FREE_MEMORY__):,}} MB available')
{__INDENTATION__*1}if type(__ALLOCATED_MEMORY_ARRAY__) is not list: raise ValueError('Memory is not allocated')
{__INDENTATION__*1}if __DEALLOCATE__ > len(__ALLOCATED_MEMORY_ARRAY__): raise MemoryError(f'Not enough memory allocated to deallocate, only {{len(__ALLOCATED_MEMORY_ARRAY__):,}} MB allocated')
{__INDENTATION__*1}__ALLOCATED_MEMORY_ARRAY__ = __ALLOCATED_MEMORY_ARRAY__[:__DEALLOCATE__]
{__INDENTATION__*1}ammout_of_memory_allocated = getsizeof(__ALLOCATED_MEMORY_ARRAY__)
{__INDENTATION__*1}if ammout_of_memory_allocated == 56: ammout_of_memory_allocated = 0
{__INDENTATION__*1}if output is None: 
{__INDENTATION__*2}return ammout_of_memory_allocated
{__INDENTATION__*1}elif output == str: 
{__INDENTATION__*2}__DEALLOCATE__ = ammout_of_memory_allocated
{__INDENTATION__*2}if __DEALLOCATE__ > 1024 * 1024 * 1024 * 1024:
{__INDENTATION__*3}__DEALLOCATE__ = __DEALLOCATE__ / (1024 * 1024 * 1024 * 1024)
{__INDENTATION__*3}__DEALLOCATE__ = round(__DEALLOCATE__, 2)
{__INDENTATION__*3}return f'{{__DEALLOCATE__:{{sep}}}} TB'
{__INDENTATION__*2}elif __DEALLOCATE__ > 1024 * 1024 * 1024:
{__INDENTATION__*3}__DEALLOCATE__ = __DEALLOCATE__ / (1024 * 1024 * 1024)
{__INDENTATION__*3}__DEALLOCATE__ = round(__DEALLOCATE__, 2)
{__INDENTATION__*3}return f'{{__DEALLOCATE__:{{sep}}}} GB'
{__INDENTATION__*2}elif __DEALLOCATE__ > 1024 * 1024:
{__INDENTATION__*3}__DEALLOCATE__ = __DEALLOCATE__ = __DEALLOCATE__ / (1024 * 1024)
{__INDENTATION__*3}__DEALLOCATE__ = round(__DEALLOCATE__, 2)
{__INDENTATION__*3}return f'{{__DEALLOCATE__:{{sep}}}} MB'
{__INDENTATION__*2}elif __DEALLOCATE__ > 1024:
{__INDENTATION__*3}__DEALLOCATE__ = __DEALLOCATE__ / 1024
{__INDENTATION__*3}__DEALLOCATE__ = round(__DEALLOCATE__, 2)
{__INDENTATION__*3}return f'{{__DEALLOCATE__:{{sep}}}} KB'
{__INDENTATION__*2}else:
{__INDENTATION__*3}__DEALLOCATE__ = round(__DEALLOCATE__, 2)
{__INDENTATION__*3}return f'{{__DEALLOCATE__:{{sep}}}} Bytes'
{__INDENTATION__*1}elif output == list:
{__INDENTATION__*2}# raise a exception informing the use THAT THEY ARE NOT SUPPOSED TO USE THIS FUNCTION
{__INDENTATION__*2}raise NotImplementedError('Using this WILL cause memory leaks, DO NOT USE')
{__INDENTATION__*1}elif output == int:
{__INDENTATION__*2}return ammout_of_memory_allocated
{__INDENTATION__*1}else:
{__INDENTATION__*2}raise TypeError('Invalid output type')
class VariableError(Exception):
{__INDENTATION__*1}def __init__(self, *args, **kwargs):
{__INDENTATION__*2}if args:
{__INDENTATION__*3}print(f"VariableError: {{args}}")
{__INDENTATION__*2}elif kwargs:
{__INDENTATION__*3}print(f"VariableError: {{kwargs}}")
{__INDENTATION__*2}exit()
class SyntaxError(Exception):
{__INDENTATION__*1}def __init__(self, *args, **kwargs):
{__INDENTATION__*2}if args:
{__INDENTATION__*3}print(f"SyntaxError: {{args}}")
{__INDENTATION__*2}elif kwargs:
{__INDENTATION__*3}print(f"SyntaxError: {{kwargs}}")
{__INDENTATION__*2}exit()
class CloseError(Exception):
{__INDENTATION__*1}def __init__(self, *args, **kwargs):
{__INDENTATION__*2}if args:
{__INDENTATION__*3}print(f"CloseError: {{args}}")
{__INDENTATION__*2}elif kwargs:
{__INDENTATION__*3}print(f"CloseError: {{kwargs}}")
{__INDENTATION__*2}exit()
class TypeError(Exception):
{__INDENTATION__*1}def __init__(self, *args, **kwargs):
{__INDENTATION__*2}if args:
{__INDENTATION__*3}print(f"TypeError: {{args}}")
{__INDENTATION__*2}elif kwargs:
{__INDENTATION__*3}print(f"TypeError: {{kwargs}}")
{__INDENTATION__*2}exit()
class DataError(Exception):
{__INDENTATION__*1}def __init__(self, *args, **kwargs):
{__INDENTATION__*2}if args:
{__INDENTATION__*3}print(f"DataError: {{args}}")
{__INDENTATION__*2}elif kwargs:
{__INDENTATION__*3}print(f"DataError: {{kwargs}}")
{__INDENTATION__*2}exit()
class FileNotFoundError(Exception):
{__INDENTATION__*1}def __init__(self, *args, **kwargs):
{__INDENTATION__*2}if args:
{__INDENTATION__*3}print(f"FileNotFoundError: {{args}}")
{__INDENTATION__*2}elif kwargs:
{__INDENTATION__*3}print(f"FileNotFoundError: {{kwargs}}")
{__INDENTATION__*2}exit()
class RefrenceError(Exception):
{__INDENTATION__*1}def __init__(self, *args, **kwargs):
{__INDENTATION__*2}if args:
{__INDENTATION__*3}print(f"RefrenceError: {{args}}")
{__INDENTATION__*2}elif kwargs:
{__INDENTATION__*3}print(f"RefrenceError: {{kwargs}}")
{__INDENTATION__*2}exit()
class NoMainError(Exception):
{__INDENTATION__*1}def __init__(self, *args, **kwargs):
{__INDENTATION__*2}if args:
{__INDENTATION__*3}print(f"NoMainError: {{args}}")
{__INDENTATION__*2}elif kwargs:
{__INDENTATION__*3}print(f"NoMainError: {{kwargs}}")
{__INDENTATION__*2}exit()
class Error(Exception):
{__INDENTATION__*1}def __init__(self, *args, **kwargs):
{__INDENTATION__*2}if args:
{__INDENTATION__*3}print(f"Error: {{args}}")
{__INDENTATION__*2}elif kwargs:
{__INDENTATION__*3}print(f"Error: {{kwargs}}")
{__INDENTATION__*2}exit()
\"\"\"
--------------------------------------------------------------------------------
YOU CAN MODIFY THE CODE BELOW THIS LINE - DO NOT MODIFY THE CODE ABOVE THIS LINE
--------------------------------------------------------------------------------
\"\"\""""
    if "-*- no color -*-" in __OPTIANAL_ARGS_IN_FILE__: DATA = DATA.replace("from rich import console; print = console.Console().print", '')
    return DATA
@overload
def __CREATE_CONFIG_FILE__() -> str:
    """
    Inputs: None
    Outputs: Default config data (string)
    Returns the default config data.
    The returned data is automatically formatted and indented.
    """
    import time
    __CURRENT_TIME__ = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime())
    __CONFIG_DATA__ = f"""# {'-' * len(f"This is the config file for versace it was auto generated at {__CURRENT_TIME__}")} #
# This is the config file for versace it was auto generated at {__CURRENT_TIME__} #
# {'-' * len(f"This is the config file for versace it was auto generated at {__CURRENT_TIME__}")} #

["BASIC-INFORMATION"]
version = "{__VERSION__}"{' ' * (64 - len(f'version = "{__VERSION__}"'))}# the version of versace
indentation = "    "                                            # 4 spaces is the default
allow_tracking = True                                           # This is to allow tracking of versace
allow_update = False                                            # This is to allow updates of versace

["PATHS"]
python_path = "{sys.executable}"{' ' * (62 - len(f'python_path = "{sys.executable}"'))}# This is the path to the python interpreter
versace_path = "{os.path.expanduser('~') + os.sep + 'versace'}"{' ' * (61 - len(f"versace_path = '{os.path.expanduser('~') + os.sep + 'versace'}'"))}# This is the path to the versace folder

["COMPILER"]
no_includes = False                                             # This determines if the versace compiler should include the modules specified by the user in thier versace code
no_args_start = False                                           # This determines if the versace compiler should start the versace code with the args passed to the versace compiler
no_version_check = False                                        # This determines if the versace compiler should check for updates

["EXECUTABLE"]
binary_file_ext = ".exe"                                        # The type of binary to compile to when compiling to binary
binary = 0                                                      # Optimization level when compiling 0 = low_optimization(onfile), 1 = medium_optimization(ondir), 2 = max_optimization(nested_dirs)

["EXTRA"]
keep_perf_data = False                                          # This determines if the versace compiler should keep the performance data
always_monitor_perf_data = False                                # This determines if the versace compiler should always show the performance data
transpile_file_ext = ".py"                                      # The type of file to transpile to when compiling to python
use_cache = False                                                # This determines if the versace compiler should use the cache"""
    if '\\' in __CONFIG_DATA__:
        __CONFIG_DATA__ = __CONFIG_DATA__.replace('\\', '\\\\')
    return __CONFIG_DATA__
@overload
def __INITIALIZE__():
    """
    \n Inputs: None
    \n Outputs: None
    \n This is the first stage of the versace compiler.
    \n This stage is used to get the config data and the versace code.
    \n It also checks if the required modules are installed. and saves that information to a .pkg file.
    """
    if os.path.exists(os.path.expanduser('~') + os.sep + 'versace' + os.sep + 'base' + os.sep + 'packages.pkg') is False:
        import pkg_resources, subprocess
        console("")
        __REQUIRED_MODULES__ = {'psutil', 'rich', 'requests' , 'pyinstaller'}
        __INSTALLED_MODULES__ = {pkg.key for pkg in pkg_resources.working_set}
        __MISSING_MODULES__ = __REQUIRED_MODULES__ - __INSTALLED_MODULES__

        if __MISSING_MODULES__:
            __PYTHON_PATH__ = sys.executable
            subprocess.check_call([__PYTHON_PATH__, '-m', 'pip', 'install', *__MISSING_MODULES__], stdout=subprocess.DEVNULL)
            print(f"{__COLORS__['bold green']}Installed __MISSING_MODULES__ modules successfully{__COLORS__['reset']}")

        __REQUIRED_MODULES__ = {'cx_Freeze'}
        __INSTALLED_MODULES__ = {pkg.key for pkg in pkg_resources.working_set}
        __MISSING_MODULES__ = __REQUIRED_MODULES__ - __INSTALLED_MODULES__

        if __MISSING_MODULES__:
            __PYTHON_PATH__ = sys.executable
            subprocess.check_call([__PYTHON_PATH__, '-m', 'pip', 'install', '--pre', '--extra-index-url', 'https://marcelotduarte.github.io/packages/', 'cx_Freeze', 'cx_Logging'], stdout=subprocess.DEVNULL)
            print(f"{__COLORS__['bold green']}Installed __MISSING_MODULES__ modules successfully{__COLORS__['reset']}")

    # create a folder at os.path.expanduser('~') called versace
    if os.path.exists(os.path.expanduser('~') + os.sep + 'versace' + os.sep + 'base') is False:
        os.makedirs(os.path.expanduser('~') + os.sep + 'versace', exist_ok=True)
        os.makedirs(os.path.expanduser('~') + os.sep + 'versace' + os.sep + 'base', exist_ok=True)

    if os.path.exists(os.path.expanduser('~') + os.sep + 'versace' + os.sep + 'base' + os.sep + 'packages.pkg') is False:
        with open(f"{os.path.expanduser('~')}{os.sep}versace{os.sep}base{os.sep}packages.pkg", "w") as f:
            f.write('1 : psutil\n2 : rich\n3 : requests\n4 : pyinstaller\n5 : cx_Freeze')
            f.close()
@overload
def __READ_SYS_ARGS__() -> None:
    if '-cfg' in __PASS_LIST__:
        if os.path.exists(os.getcwd() + os.sep + 'versace.cfg') is False:
            with open(f"{os.getcwd()}{os.sep}versace.cfg", "w") as f:
                f.write(__CREATE_CONFIG_FILE__())
                f.close()
            console("")
            print(f"{__COLORS__['bold red']}Created config file at {__COLORS__['bold cyan']}{os.getcwd()}{os.sep}versace.cfg{__COLORS__['reset']}")
            exit()
        else:
            # execute the config file
            with open(f"{os.getcwd()}{os.sep}versace.cfg", "r") as f:
                __CONFIG_DATA__ = f.read()
                f.close()
            __READ_CONFIG__(__CONFIG_DATA__, FILE_PATH=f"{os.getcwd()}{os.sep}versace.cfg")

            if '-d' in __PASS_LIST__:
                print(f"{__INDENTATION__}, {__ALLOW_TRACKING__}, {__ALLOW_UPDATE__}, {__PYTHON_PATH__}, {__VERSACE_PATH__}, {__NO_INCLUDES__}, {__NO_ARGS_START__}, {__NO_VERSION_CHECK__}, {__BINARY_FILE_EXT__}, {__BINARY__}, {__KEEP_PERF_DATA__}, {__ALWAYS_MONITOR_PERF_DATA__}, {__TRANSPILE_FILE_EXT__}")
    else:
        if os.path.exists(os.getcwd() + os.sep + 'versace.cfg'):
            with open(f"{os.getcwd()}{os.sep}versace.cfg", "r") as f:
                __CONFIG_DATA__ = f.read()
                f.close()
            __READ_CONFIG__(__CONFIG_DATA__, FILE_PATH=f"{os.getcwd()}{os.sep}versace.cfg")

            if '-d' in __PASS_LIST__:
                print(f"{__INDENTATION__}, {__ALLOW_TRACKING__}, {__ALLOW_UPDATE__}, {__PYTHON_PATH__}, {__VERSACE_PATH__}, {__NO_INCLUDES__}, {__NO_ARGS_START__}, {__NO_VERSION_CHECK__}, {__BINARY_FILE_EXT__}, {__BINARY__}, {__KEEP_PERF_DATA__}, {__ALWAYS_MONITOR_PERF_DATA__}, {__TRANSPILE_FILE_EXT__}")

        else:
            if os.path.exists(os.path.expanduser('~') + os.sep + 'versace' + os.sep + 'base' + os.sep + 'defualt-versace.cfg') is False:
                with open(f"{os.path.expanduser('~')}{os.sep}versace{os.sep}base{os.sep}defualt-versace.cfg", "w") as f:
                    f.write(__CREATE_CONFIG_FILE__())
                    f.close()

            with open(f"{os.path.expanduser('~')}{os.sep}versace{os.sep}base{os.sep}defualt-versace.cfg", "r") as f:
                __CONFIG_DATA__ = f.read()
                f.close()
            __READ_CONFIG__(__CONFIG_DATA__, FILE_PATH=f"{os.path.expanduser('~')}{os.sep}versace{os.sep}base{os.sep}defualt-versace.cfg")

            if '-d' in __PASS_LIST__:
                print(f"{__INDENTATION__}, {__ALLOW_TRACKING__}, {__ALLOW_UPDATE__}, {__PYTHON_PATH__}, {__VERSACE_PATH__}, {__NO_INCLUDES__}, {__NO_ARGS_START__}, {__NO_VERSION_CHECK__}, {__BINARY_FILE_EXT__}, {__BINARY__}, {__KEEP_PERF_DATA__}, {__ALWAYS_MONITOR_PERF_DATA__}, {__TRANSPILE_FILE_EXT__}")
    return 0
@overload_atter
def __READ_CONFIG__(__CONFIG_DATA__, FILE_PATH=None) -> None:
    """
    \nInputs: __CONFIG_DATA__
    \nOutputs: None
    \nThis is used to read the config data and save it to their respective variables.
    """
    global __INDENTATION__, __ALLOW_TRACKING__, __ALLOW_UPDATE__, __PYTHON_PATH__, __VERSACE_PATH__, __NO_INCLUDES__, __NO_ARGS_START__, __NO_VERSION_CHECK__, __BINARY_FILE_EXT__, __BINARY__, __KEEP_PERF_DATA__, __ALWAYS_MONITOR_PERF_DATA__, __TRANSPILE_FILE_EXT__, __USE_CACHE__
    
    def _expectError(check, type) -> None:
        linetockek: str = check
        for index, i in enumerate(__CONFIG_DATA__.split('\n')):
            if i.startswith(linetockek):
                # check if the eval is valid 
                try:
                    __BINARY__ = type(eval(__CONFIG_DATA__.split (linetockek)[1].split('\n')[0].split('#')[0].strip()))
                except Exception as e:
                    __ERROR_REPORTING__(__CONFIG_DATA__.split('\n')[index], "BadConfigData", e, LINE_NO=index+1, FILE_NAME=FILE_PATH)
                    exit()
        exit()
    
    try:
        try:
            __BINARY__                   = int (eval(__CONFIG_DATA__.split(         'binary = '         )[1].split('\n')[0].split('#')[0].strip()))
        except:
            _expectError('binary = ', int)
        try:
            __USE_CACHE__                = bool(eval(__CONFIG_DATA__.split(       'use_cache = '        )[1].split('\n')[0].split('#')[0].strip()))
        except:
            _expectError('use_cache = ', bool)
        try:
            __INDENTATION__              = str (eval(__CONFIG_DATA__.split(      'indentation = '       )[1].split('\n')[0].split('#')[0].strip()))
        except:
            _expectError('indentation = ', str)
        try:
            __NO_INCLUDES__              = bool(eval(__CONFIG_DATA__.split(      'no_includes = '       )[1].split('\n')[0].split('#')[0].strip()))
        except:
            _expectError('no_includes = ', bool)
        try:
            __PYTHON_PATH__              = str (eval(__CONFIG_DATA__.split(      'python_path = '       )[1].split('\n')[0].split('#')[0].strip()))
        except:
            _expectError('python_path = ', str)
        try:
            __ALLOW_UPDATE__             = bool(eval(__CONFIG_DATA__.split(      'allow_update = '      )[1].split('\n')[0].split('#')[0].strip()))
        except:
            _expectError('allow_update = ', bool)
        try:
            __VERSACE_PATH__             = str (eval(__CONFIG_DATA__.split(      'versace_path = '      )[1].split('\n')[0].split('#')[0].strip()))
        except:
            _expectError('versace_path = ', str)
        try:
            __NO_ARGS_START__            = bool(eval(__CONFIG_DATA__.split(     'no_args_start = '      )[1].split('\n')[0].split('#')[0].strip()))
        except:
            _expectError('no_args_start = ', bool)
        try:
            __KEEP_PERF_DATA__           = bool(eval(__CONFIG_DATA__.split(     'keep_perf_data = '     )[1].split('\n')[0].split('#')[0].strip()))
        except:
            _expectError('keep_perf_data = ', bool)
        try:
            __ALLOW_TRACKING__           = bool(eval(__CONFIG_DATA__.split(     'allow_tracking = '     )[1].split('\n')[0].split('#')[0].strip()))
        except:
            _expectError('allow_tracking = ', bool)
        try:
            __BINARY_FILE_EXT__          = str (eval(__CONFIG_DATA__.split(    'binary_file_ext = '     )[1].split('\n')[0].split('#')[0].strip()))
        except:
            _expectError('binary_file_ext = ', str)
        try:
            __NO_VERSION_CHECK__         = bool(eval(__CONFIG_DATA__.split(    'no_version_check = '    )[1].split('\n')[0].split('#')[0].strip()))
        except:
            _expectError('no_version_check = ', bool)
        try:
            __TRANSPILE_FILE_EXT__       = str (eval(__CONFIG_DATA__.split(   'transpile_file_ext = '   )[1].split('\n')[0].split('#')[0].strip()))
        except: 
            _expectError('transpile_file_ext = ', str)
        try:
            __ALWAYS_MONITOR_PERF_DATA__ = bool(eval(__CONFIG_DATA__.split('always_monitor_perf_data = ')[1].split('\n')[0].split('#')[0].strip()))
        except:
            _expectError('always_monitor_perf_data = ', bool)
        return 0
    except Exception: exit()
            
@overload
def __INITIALIZE_CHECKS__() -> None:
    """
    \n Inputs: None
    \n Outputs: None
    \n This is the second stage of initial checks.
    \n It will check the sys.argv flags and cd to the correct directory.
    \n It will also check if the file exists.
    """
    # check which one of the sys.argv elements is the file path
    __FILE_PATH__: str = ''
    for _I_ in __PASS_LIST__:
        if '"' in _I_ or "'" in _I_:
            __PASS_LIST__[__PASS_LIST__.index(_I_)] = str(eval(_I_)).__str__()

        if _I_.endswith('.py') or _I_.endswith('.exe'):
            continue

        if '.' in _I_ or '/' in _I_ or '\\' in _I_:
            __FILE_PATH__ = _I_
            break

    if __FILE_PATH__ == '':
        console('')
        print(f"{__COLORS__['red']}No file path found{__COLORS__['reset']}")
        print(f"{__COLORS__['red']}If you need help type {__COLORS__['green']}versace -h{__COLORS__['red']}{__COLORS__['reset']}")
        print(f"{__COLORS__['red']}Please enter the file path : {__COLORS__['reset']}", end='')
        __FILE_PATH__ = input()
        

    if '\\\\' in __FILE_PATH__:
        __FILE_PATH__ = __FILE_PATH__.replace('\\', os.sep)
    elif '/' in __FILE_PATH__:
        __FILE_PATH__ = __FILE_PATH__.replace('/', os.sep)
    elif '\\' in __FILE_PATH__:
        __FILE_PATH__ = __FILE_PATH__.replace('\\', os.sep)

    if os.getcwd().lower() not in __FILE_PATH__.lower():
        __FILE_PATH__ = os.getcwd() + os.sep + __FILE_PATH__
        __PASS_LIST__[__PASS_LIST__.index(_I_)] = __FILE_PATH__

    os.chdir(os.path.dirname(__FILE_PATH__))

    __FILE_PATH__ = os.path.abspath(__FILE_PATH__)

    if os.path.exists(__FILE_PATH__) is False:
        console("")
        print(f"{__COLORS__['bold red']}File path {__COLORS__['bold cyan']}{__FILE_PATH__}{__COLORS__['bold red']} does not exist{__COLORS__['reset']}")
        wait(2)
        exit()

    return __FILE_PATH__
@overload
def __CHECK_ARGS__(__FILE_PATH__) -> None:
    """
    \n Inputs: __FILE_PATH__
    \n Outputs: None
    \n This is the third stage of initial checks.
    \n It will check the sys.argv flags and if they are not valid, it will print the help message.
    \n It also creates a config file if '-cfg' in passed.
    """
    __ALLOWED_ARGS__ = ('-p', '-d', '-v', '-h', '-f', '-all', '-cfg', '-ctemp', '-clear', '-upgrade', '-t', '-c', '-1', '-2', '-3', '-exec', '-py')

    for i in __PASS_LIST__:
        if '-' in i and '.' not in i:
            if i not in __ALLOWED_ARGS__:
                console("")
                print(f'{__COLORS__["bold red"]}Invalid argument provided{__COLORS__["reset"]}')
                print(f'{__COLORS__["bold green"]}Working arguments:{__COLORS__["reset"]}')
                print(f'{__COLORS__["bold green"]}-p            | Shows the performance statistics of the program{__COLORS__["reset"]}')
                print(f'{__COLORS__["bold green"]}-d            | Runs the debug mode{__COLORS__["reset"]}')
                print(f'{__COLORS__["bold green"]}-v            | Shows the version of the program{__COLORS__["reset"]}')
                print(f'{__COLORS__["bold green"]}-h            | Shows the help menu{__COLORS__["reset"]}')
                print(f'{__COLORS__["bold green"]}-f            | Forces the program to freeze before exiting{__COLORS__["reset"]}')
                print(f'{__COLORS__["bold green"]}-all          | Meant to be used in conjunction with -d or -ctemp, it shows more debug data, if used with "-ctemp" it will clear the entire temp folder{__COLORS__["reset"]}')
                print(f'{__COLORS__["bold green"]}-cfg          | Auto creates a versace.cfg file in your current directory and opens it in your text editor{__COLORS__["reset"]}')
                print(f'{__COLORS__["bold green"]}-ctemp        | Clears the data associated with inputed file (does not remove the file itself){__COLORS__["reset"]}')
                print(f'{__COLORS__["bold green"]}-clear        | Clears the terminal screen before execution{__COLORS__["reset"]}')
                print(f'{__COLORS__["bold green"]}-upgrade      | Upgrades Versace to the latest version{__COLORS__["reset"]}')
                print(f'{__COLORS__["bold green"]}-t <filename> | Transpiles the versace code to a python file{__COLORS__["reset"]}')
                print(f'{__COLORS__["bold green"]}-c <filename> | Compiles the versace code to a binary exe file{__COLORS__["reset"]}')
                print(f'{__COLORS__["bold green"]}  -1**        | Must be used in conjunction with -c, it compiles the file to a single unoptimized executable file{__COLORS__["reset"]}')
                print(f'{__COLORS__["bold green"]}  -2**        | Must be used in conjunction with -c, it compiles the file to a faster single directory with a executable file{__COLORS__["reset"]}')
                print(f'{__COLORS__["bold green"]}  -3**        | Must be used in conjunction with -c, it compiles the file to a the fastest most-optimized executable file, but nested with a lot of directories{__COLORS__["reset"]}')
                print(f'{__COLORS__["bold green"]}  -exec**     | Must be used in conjunction with a file to be run. Runs the file without using python (quickest){__COLORS__["reset"]}')
                print(f'{__COLORS__["bold green"]}  -py**       | Must be used in conjunction with a file to be run. Runs the file with python {__COLORS__["bold magenta"]}(Default){__COLORS__["reset"]}')
                print(f'{__COLORS__["yellow"]}If no arguments are provided, the program will run the file you put in the first argument using python (not that slow but still slow){__COLORS__["reset"]}')
                print(f'{__COLORS__["red"]}*<filename> is an OPTIONAL argument{__COLORS__["reset"]}')
                print(f'{__COLORS__["red"]}**Means that it must be used in conjunction with some argument{__COLORS__["reset"]}')
                print(f'{__COLORS__["bold red"]}You used {i}{__COLORS__["reset"]}')
                exit()  # Exit the program

    if '-all' in __PASS_LIST__ and '-d' not in __PASS_LIST__:
        if '-ctemp' in __PASS_LIST__: pass
        else:
            console("")
            print(f'{__COLORS__["bold red"]}-all must be used in conjunction with -d{__COLORS__["reset"]}')
            exit()
    if '-1' in __PASS_LIST__ or '-2' in __PASS_LIST__ or '-3' in __PASS_LIST__:
        if '-c' not in __PASS_LIST__:
            console("")
            print(f'{__COLORS__["bold red"]}-1, -2, and -3 must be used in conjunction with -c{__COLORS__["reset"]}')
            exit()
    if '-clear' in __PASS_LIST__:
        console("cls" if os.name == 'nt' else "clear")
    return __FILE_PATH__
@overload_atter
def __OPEN_FILE__(__FILE_PATH__, mode = None) -> list:
    """
    \n Input: The file path to the versace file
    \n Output: None
    \n Opens the versace file and passes it to the __SPLIT_ALL_LINES__ function.
    """
    global __LINES__, __LINES_FROM_FILE_RAW__, __COLORS__, __USE_CACHE__, __OPTIANAL_ARGS_IN_FILE__
    __OPTIONAL_ARGUMENT__: str = ""
    with open(__FILE_PATH__, "r") as f:
        __LINES__ = f.readlines()
        f.close()
    __LINES_FROM_FILE_RAW__ = __LINES__.copy()
    for _INDEX_, _LINE_ in enumerate(__LINES__):
        if '//' in _LINE_:
            _LINE_ = _LINE_.split('//')[0]
        if _LINE_.strip().startswith('[') and _LINE_.strip().endswith(']'):
            __OPTIONAL_ARGUMENT__ = _LINE_.strip()[1:-1]
            console("")
            if mode != 'include':
                if __OPTIONAL_ARGUMENT__ in __GLOBAL_VARIABLES__.__OPTIANAL_ARGS_ALLOWED__:
                    __OPTIANAL_ARGS_IN_FILE__.append(__OPTIONAL_ARGUMENT__)
                else:
                    # exmaple line: [arg1, arg2, arg3]
                    # output 1 : BAD OPTION CALL in line 1: [arg1, arg2, arg3]
                    # output 2 : ╰────────────────────────> ^                ^
                    # output 3 : You can only use "[" and "]" to make OPTIONAL arguments, if you do not understand this, please read the documentation. here https://dhruvan.gitbook.io/vs
                    print(f'{__COLORS__["bold red"]}Bad optional argument in line {_INDEX_ + 1}:{__COLORS__["bold yellow"]} {_LINE_.strip()}{__COLORS__["reset"]}')
                    print(f'{__COLORS__["bold red"]}╰{"─" * (len(f"Bad optional argument in line {_INDEX_ + 1}:") - 2)}> {"^" * (len(_LINE_.strip()) - 1)}^{__COLORS__["reset"]}')
                    if ',' in _LINE_.strip():
                        print(f'{__COLORS__["bold red"]}If you meant to make a list, you can use the "list" opperator, example: {__COLORS__["bold yellow"]}list(1, 2, 3){__COLORS__["reset"]}')
                        exit()
                    print(f'{__COLORS__["bold red"]}You can only use "[" and "]" to make OPTIONAL arguments, if you do not understand this, please read the documentation. here {__COLORS__["bold blue"]}https://dhruvan.gitbook.io/vs/versace/optional-arguments{__COLORS__["reset"]}')
                    exit()
            else:
                print(f'{__COLORS__["bold red"]}No optional arguments allowed, used in line {_INDEX_ + 1}:{__COLORS__["bold yellow"]} {_LINE_.strip()}{__COLORS__["reset"]}')
                print(f'{__COLORS__["bold red"]}╰{"─" * (len(f"Miss-used optional argument in line {_INDEX_ + 1}:") - 2)}> {"^" * (len(_LINE_.strip()) - 1)}^{__COLORS__["reset"]}')
                if ',' in _LINE_.strip():
                    print(f'{__COLORS__["bold red"]}If you meant to make a list, you can use the "list" opperator, example: {__COLORS__["bold yellow"]}list(1, 2, 3){__COLORS__["reset"]}')
                    exit()
                print(f'{__COLORS__["bold red"]}You an not use optional arguments in a included file, if you do not understand this, please read the documentation. here {__COLORS__["bold blue"]}https://dhruvan.gitbook.io/vs/versace/optional-arguments{__COLORS__["reset"]}')
                exit()
            __LINES__[_INDEX_] = ''
    if '-*- cache -*-' in __OPTIANAL_ARGS_IN_FILE__:
        __USE_CACHE__ = True
        
    __COLORS__ = _MAP_(
        {
            'red' : '\033[31m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'green' : '\033[32m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'yellow' : '\033[33m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'blue' : '\033[34m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'magenta' : '\033[35m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'cyan' : '\033[36m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'white' : '\033[37m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',

            'bold red' : '\033[1;31m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'bold green' : '\033[1;32m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'bold yellow' : '\033[1;33m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'bold blue' : '\033[1;34m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'bold magenta' : '\033[1;35m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'bold cyan' : '\033[1;36m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'bold white' : '\033[1;37m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',

            'bright_red' : '\033[91m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'bright_green' : '\033[92m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'bright_yellow' : '\033[93m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'bright_blue' : '\033[94m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'bright_magenta' : '\033[95m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'bright_cyan' : '\033[96m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'bright_white' : '\033[97m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',

            'underline' : '\033[4m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'italic' : '\033[3m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'blink' : '\033[5m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'reverse' : '\033[7m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'reset' : '\033[0m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        }
    )
    return __LINES_FROM_FILE_RAW__

@property
def __SPLIT_ALL_LINES_INCLUDE__(__LINES__: list[str] | str) -> list[list]:
    __CLOSING_PAIRS__ = {
        '(': ')',
        '[': ']',
        '{': '}',
        '"': '"',
    }

    __LINES__ = [x.strip() for x in __LINES__]
    __LINES__ = [x for x in __LINES__ if x != '']

    __WORD__ = ''
    __PRE_SPLIT_LIST__ = []
    __IN_STRING__ = False
    __IN_COMMENT__ = False
    __IN_MULTI_LINE_COMMENT__ = False
    __INDEX__ = 0
    __LINES_COPY__ = __LINES__.copy()
    __TEMP_LINE__ = ''
    __TEMP_SPLIT_LIST__: list[list] = []

    for __INDEX__, _I_ in enumerate(__LINES__):
        if _I_.startswith('/*') and __IN_MULTI_LINE_COMMENT__ is False:
            __IN_MULTI_LINE_COMMENT__ = True

        if _I_.endswith('*/') and __IN_MULTI_LINE_COMMENT__:
            __LINES__[__INDEX__] = ''
            __IN_MULTI_LINE_COMMENT__ = False

        if __IN_MULTI_LINE_COMMENT__:
            __LINES__[__INDEX__] = ''

        if _I_.startswith('//'):
            __LINES__[__INDEX__] = ''

        if _I_.startswith('#'):
            __ERROR_REPORTING__(__LINES__[__INDEX__], "usedHashtag")
    if __IN_MULTI_LINE_COMMENT__:
        __ERROR_REPORTING__(__LINES__[__INDEX__], "unclosedComment")
        exit()
    __LINES__ = [x for x in __LINES__ if x != '']
    _NEW_LINE_: str = ''

    for _INDEX_, _I_ in enumerate(__LINES__):
        if _I_.startswith('[') and _I_.endswith(']'):
            __TEMP_SPLIT_LIST__.append([_I_])
            __LINES__.remove(_I_)
            continue
        for i in _I_:
            _NEW_LINE_ += i
            if i == '"' and __IN_STRING__ is False:
                __IN_STRING__ = True
                continue
            if i == '"' and __IN_STRING__:
                __IN_STRING__ = False
                continue
            if __IN_STRING__ is False:
                if i == '}':
                    _NEW_LINE_ += ';'

        __LINES__[_INDEX_] = _NEW_LINE_
        _NEW_LINE_ = ''

    for _I_ in __LINES__:
        __IN_COMMENT__ = False
        for _INDEX_CHAR_, _II_ in enumerate(_I_):
            if _II_ == '"' and _I_[_INDEX_CHAR_ - 1] != '\\':
                if __IN_STRING__ is False:
                    __IN_STRING__ = True
                else:
                    __IN_STRING__ = False
            if _II_ == '/' and __IN_STRING__ is False:
                if _INDEX_CHAR_ + 1 < len(_I_):
                    if _I_[_INDEX_CHAR_ + 1] == '/':
                        break

            if _II_ in __GLOBAL_VARIABLES__.__NON_NORMAL_CHARS__ and __IN_STRING__ is False and __IN_COMMENT__ is False and __IN_MULTI_LINE_COMMENT__ is False:
                if __WORD__ != '':
                    __PRE_SPLIT_LIST__.append(__WORD__)
                    __WORD__ = ''
                if _II_ == ';':
                    __PRE_SPLIT_LIST__.append(_II_ + '<newline>')
                else:
                    __PRE_SPLIT_LIST__.append(_II_)
            else:
                __WORD__ += _II_

        if __WORD__ != '':
            __PRE_SPLIT_LIST__.append(__WORD__)
            __WORD__ = ''

    __PRE_SPLIT_LIST__ = [x.strip() for x in __PRE_SPLIT_LIST__]
    __PRE_SPLIT_LIST__ = [x for x in __PRE_SPLIT_LIST__ if x != '']

    for _INDEX_CHAR_, i in enumerate(__PRE_SPLIT_LIST__):
        if i in __CLOSING_PAIRS__.keys():
            if __PRE_SPLIT_LIST__[_INDEX_CHAR_ + 1] == __CLOSING_PAIRS__[i]:
                __PRE_SPLIT_LIST__[_INDEX_CHAR_] = i + __CLOSING_PAIRS__[i]
                __PRE_SPLIT_LIST__.pop(_INDEX_CHAR_ + 1)
        if _INDEX_CHAR_ + 1 < len(__PRE_SPLIT_LIST__):
            if __PRE_SPLIT_LIST__[_INDEX_CHAR_ + 1] == i:
                __PRE_SPLIT_LIST__[_INDEX_CHAR_] = i + i
                __PRE_SPLIT_LIST__.pop(_INDEX_CHAR_ + 1)

    for i in __PRE_SPLIT_LIST__:
        if i.endswith('<newline>'):
            # remove the newline from the end of the line
            __TEMP_SPLIT_LIST__.append(__PRE_SPLIT_LIST__[:__PRE_SPLIT_LIST__.index(i) + 1][:-1])
            __PRE_SPLIT_LIST__ = __PRE_SPLIT_LIST__[__PRE_SPLIT_LIST__.index(i) + 1:]
            __PRE_SPLIT_LIST__ = [x.strip() for x in __PRE_SPLIT_LIST__]
            __PRE_SPLIT_LIST__ = [x for x in __PRE_SPLIT_LIST__ if x != '']

    __PRE_SPLIT_LIST__ = [x.strip() for x in __PRE_SPLIT_LIST__]
    __PRE_SPLIT_LIST__ = [x for x in __PRE_SPLIT_LIST__ if x != '']
    
    del __WORD__, __PRE_SPLIT_LIST__, __IN_STRING__, __IN_COMMENT__, __IN_MULTI_LINE_COMMENT__, __INDEX__, __LINES_COPY__, __TEMP_LINE__
    
    return __TEMP_SPLIT_LIST__
@property
def __SPLIT_ALL_LINES__(mode=None, __DATA__=None) -> list[list] | None:
    """
    \n Inputs: mode, and data
    \n Outputs: List if mode is 'include', None for all other modes
    \n Splits the list of lines into a list of lists, where each list is a line.
    \n It configures the list of lists to be used in the rest of the program.
    """
    global __SPLIT_LIST__, __LINES__, __PRE_SPLIT_LIST__
    
    if mode == 'include':
        return __SPLIT_ALL_LINES_INCLUDE__(__DATA__)
    
    __CLOSING_PAIRS__ = {
        '(': ')',
        '[': ']',
        '{': '}',
        '"': '"',
    }

    __LINES__ = [x.strip() for x in __LINES__]
    __LINES__ = [x for x in __LINES__ if x != '']

    __WORD__ = ''
    __PRE_SPLIT_LIST__ = []
    __IN_STRING__ = False
    __IN_COMMENT__ = False
    __IN_MULTI_LINE_COMMENT__ = False
    __INDEX__ = 0
    __LINES_COPY__ = __LINES__.copy()
    __TEMP_LINE__ = ''

    for __INDEX__, _I_ in enumerate(__LINES__):
        if _I_.startswith('/*') and __IN_MULTI_LINE_COMMENT__ is False:
            __IN_MULTI_LINE_COMMENT__ = True

        if _I_.endswith('*/') and __IN_MULTI_LINE_COMMENT__:
            __LINES__[__INDEX__] = ''
            __IN_MULTI_LINE_COMMENT__ = False

        if __IN_MULTI_LINE_COMMENT__:
            __LINES__[__INDEX__] = ''

        if _I_.startswith('//'):
            __LINES__[__INDEX__] = ''

        if _I_.startswith('#'):
            __ERROR_REPORTING__(__LINES__[__INDEX__], "usedHashtag")

    __LINES__ = [x for x in __LINES__ if x != '']
    _NEW_LINE_: str = ''

    for _INDEX_, _I_ in enumerate(__LINES__):
        if _I_.startswith('[') and _I_.endswith(']'):
            __SPLIT_LIST__.append([_I_])
            __LINES__.remove(_I_)
            continue
        for i in _I_:
            _NEW_LINE_ += i
            if i == '"' and __IN_STRING__ is False:
                __IN_STRING__ = True
                continue
            if i == '"' and __IN_STRING__:
                __IN_STRING__ = False
                continue
            if __IN_STRING__ is False:
                if i == '}':
                    _NEW_LINE_ += ';'

        __LINES__[_INDEX_] = _NEW_LINE_
        _NEW_LINE_ = ''

    for _I_ in __LINES__:
        __IN_COMMENT__ = False
        for _INDEX_CHAR_, _II_ in enumerate(_I_):
            if _II_ == '"' and _I_[_INDEX_CHAR_ - 1] != '\\':
                if __IN_STRING__ is False:
                    __IN_STRING__ = True
                else:
                    __IN_STRING__ = False
            if _II_ == '/' and __IN_STRING__ is False:
                if _INDEX_CHAR_ + 1 < len(_I_):
                    if _I_[_INDEX_CHAR_ + 1] == '/':
                        break

            if _II_ in __GLOBAL_VARIABLES__.__NON_NORMAL_CHARS__ and __IN_STRING__ is False and __IN_COMMENT__ is False and __IN_MULTI_LINE_COMMENT__ is False:
                if __WORD__ != '':
                    __PRE_SPLIT_LIST__.append(__WORD__)
                    __WORD__ = ''
                if _II_ == ';':
                    __PRE_SPLIT_LIST__.append(_II_ + '<newline>')
                else:
                    __PRE_SPLIT_LIST__.append(_II_)
            else:
                __WORD__ += _II_

        if __WORD__ != '':
            __PRE_SPLIT_LIST__.append(__WORD__)
            __WORD__ = ''
        
    __PRE_SPLIT_LIST__ = [x.strip() for x in __PRE_SPLIT_LIST__]
    __PRE_SPLIT_LIST__ = [x for x in __PRE_SPLIT_LIST__ if x != '']

    for _INDEX_CHAR_, i in enumerate(__PRE_SPLIT_LIST__):
        if i in __CLOSING_PAIRS__.keys():
            if __PRE_SPLIT_LIST__[_INDEX_CHAR_ + 1] == __CLOSING_PAIRS__[i]:
                __PRE_SPLIT_LIST__[_INDEX_CHAR_] = i + __CLOSING_PAIRS__[i]
                __PRE_SPLIT_LIST__.pop(_INDEX_CHAR_ + 1)
        if _INDEX_CHAR_ + 1 < len(__PRE_SPLIT_LIST__):
            if __PRE_SPLIT_LIST__[_INDEX_CHAR_ + 1] == i:
                __PRE_SPLIT_LIST__[_INDEX_CHAR_] = i + i
                __PRE_SPLIT_LIST__.pop(_INDEX_CHAR_ + 1)

    for i in __PRE_SPLIT_LIST__:
        if i.endswith('<newline>'):
            # remove the newline from the end of the line
            __SPLIT_LIST__.append(__PRE_SPLIT_LIST__[:__PRE_SPLIT_LIST__.index(i) + 1][:-1])
            __PRE_SPLIT_LIST__ = __PRE_SPLIT_LIST__[__PRE_SPLIT_LIST__.index(i) + 1:]
            __PRE_SPLIT_LIST__ = [x.strip() for x in __PRE_SPLIT_LIST__]
            __PRE_SPLIT_LIST__ = [x for x in __PRE_SPLIT_LIST__ if x != '']
    
    __PRE_SPLIT_LIST__ = [x.strip() for x in __PRE_SPLIT_LIST__]
    __PRE_SPLIT_LIST__ = [x for x in __PRE_SPLIT_LIST__ if x != '']
    del __WORD__, __PRE_SPLIT_LIST__, __IN_STRING__, __IN_COMMENT__, __IN_MULTI_LINE_COMMENT__, __INDEX__, __LINES_COPY__, __TEMP_LINE__
    if mode == 'include':
        return __SPLIT_LIST__
    return None    
@property
def __SPLIT_LINE__(_I_) -> list:
    """
    \n Inputs: the line to split into tokens
    \n Outputs: the split line
    \n This function splits the line into a list of words and opperators
    """
    __CLOSING_PAIRS__ = {
        '(': ')',
        '[': ']',
        '{': '}',
        '"': '"',
    }
    __PRE_SPLIT_LIST__ = []
    __WORD__ = ''
    __IN_STRING__ = False
    __IN_COMMENT__ = False
    __WORD__ = ''
    __PRE_SPLIT_LIST__ = []
    __IN_STRING__ = False
    __IN_COMMENT__ = False
    __IN_MULTI_LINE_COMMENT__ = False
    __INDEX__ = 0
    __LINES_COPY__ = __LINES__.copy()
    __TEMP_LINE__ = ''
    __SPACES__ = -1
    for _INDEX_CHAR_, _II_ in enumerate(_I_):
        if _II_ == ' ':
            __SPACES__ += 1
        else:
            break
    if __SPACES__ == -1: __SPACES__ = 0
    for _INDEX_CHAR_, _II_ in enumerate(_I_):  # For each character in the line
        if _II_ == '"' and _I_[_INDEX_CHAR_ - 1] != '\\':
            if __IN_STRING__ is False:
                __IN_STRING__ = True
            else:
                __IN_STRING__ = False
        if _II_ == '/' and __IN_STRING__ is False:
            if _INDEX_CHAR_ + 1 < len(_I_):
                if _I_[_INDEX_CHAR_ + 1] == '/':
                    break

        if _II_ in __GLOBAL_VARIABLES__.__NON_NORMAL_CHARS__ and __IN_STRING__ is False and __IN_COMMENT__ is False and __IN_MULTI_LINE_COMMENT__ is False:
            if __WORD__ != '':
                __PRE_SPLIT_LIST__.append(__WORD__)
                __WORD__ = ''
            if _II_ == ';':
                __PRE_SPLIT_LIST__.append(_II_ + '<newline>')
            else:
                __PRE_SPLIT_LIST__.append(_II_)
        else:
            __WORD__ += _II_

    if __WORD__ != '':
        __PRE_SPLIT_LIST__.append(__WORD__)
        __WORD__ = ''

    __PRE_SPLIT_LIST__ = [x.strip() for x in __PRE_SPLIT_LIST__]
    __PRE_SPLIT_LIST__ = [x for x in __PRE_SPLIT_LIST__ if x != '']

    for _INDEX_CHAR_, i in enumerate(__PRE_SPLIT_LIST__):
        # check if the next item is a closing pair and if it is then merge them
        if i in __CLOSING_PAIRS__.keys():
            if __PRE_SPLIT_LIST__[_INDEX_CHAR_ + 1] == __CLOSING_PAIRS__[i]:
                __PRE_SPLIT_LIST__[_INDEX_CHAR_] = i + __CLOSING_PAIRS__[i]
                __PRE_SPLIT_LIST__.pop(_INDEX_CHAR_ + 1)
        # if the next iteem is the same as the current item then merge them, but do this without raising an index error
        if _INDEX_CHAR_ + 1 < len(__PRE_SPLIT_LIST__):
            if __PRE_SPLIT_LIST__[_INDEX_CHAR_ + 1] == i:
                __PRE_SPLIT_LIST__[_INDEX_CHAR_] = i + i
                __PRE_SPLIT_LIST__.pop(_INDEX_CHAR_ + 1)

    __PRE_SPLIT_LIST__ = [x.strip() for x in __PRE_SPLIT_LIST__]
    __PRE_SPLIT_LIST__ = [x for x in __PRE_SPLIT_LIST__ if x != '']
    __PRE_SPLIT_LIST__.insert(0, ' ' * (__SPACES__))

    return __PRE_SPLIT_LIST__

@overload_atter
def __ASSIGN_VARIABLE__(__VARIABLE_NAME__, __VARIABLE_TYPE__, __VARIABLE_VALUE__) -> None:
    """
    \n Inputs: the variable name and the variable value
    \n Outputs: None
    \n This function assigns the variable name to the variable value and saves it to the variable dictionary
    """
    global __VARIABLES__
    __VARIABLES__[__VARIABLE_NAME__] = {
        'type': __VARIABLE_TYPE__,
        'value': __VARIABLE_VALUE__
    }
    return
@overload_atter
def __ASSIGN_FUNCTION__(__FUNCTION_NAME__, __FUNCTION_TYPE__, __FUNCTION_VALUE__) -> None:
    """
    \n Inputs: the function name and the function value
    \n Outputs: None
    \n This function assigns the function name to the function value and saves it to the function dictionary
    """
    global __FUNCTIONS__
    __FUNCTIONS__[__FUNCTION_NAME__] = {
        'type': __FUNCTION_TYPE__,
        'value': __FUNCTION_VALUE__
    }
    return
@overload_atter
def __ASSIGN_CLASS__(__CLASS_NAME__, __CLASS_TYPE__) -> None:
    """
    \n Inputs: the class name and the class value
    \n Outputs: None
    \n This function assigns the class name to the class value and saves it to the class dictionary
    """
    global __CLASSES__
    __CLASSES__[__CLASS_NAME__] = __CLASS_TYPE__
    return

@overload_atter
def __GET_VARIABLE__(__VARIABLE_NAME__, __TYPE__: int) -> str:
    """
    \n Inputs: the variable name and type (0 = value, 1 = type, 3 = both)
    \n Outputs: the variable value
    \n This function gets the variable value from the variable dictionary
    """
    global __VARIABLES__
    if __TYPE__ == 0:
        return __VARIABLES__[__VARIABLE_NAME__]['value']
    elif __TYPE__ == 1:
        return __VARIABLES__[__VARIABLE_NAME__]['type']
    else:
        return __VARIABLES__[__VARIABLE_NAME__]
@overload_atter
def __GET_CLASS__(__CLASS_NAME__) -> str:
    """
    \n Inputs: the class name
    \n Outputs: the class value
    \n This function gets the class value from the class dictionary
    """
    global __CLASSES__
    return __CLASSES__[__CLASS_NAME__]
@overload_atter
def __GET_FUNCTION__(__FUNCTION_NAME__, __TYPE__: int) -> str:
    """
    \n Inputs: the function name and type (0 = value, 1 = type, 2 = full line, other = all)
    \n Outputs: the function value
    \n This function gets the function value from the function dictionary
    """
    global __FUNCTIONS__
    if __TYPE__ == 0:
        return __FUNCTIONS__[__FUNCTION_NAME__]['value']
    elif __TYPE__ == 1:
        return __FUNCTIONS__[__FUNCTION_NAME__]['type']
    elif __TYPE__ == 2:
        for i in __FUNCTIONS__:
            if __FUNCTION_NAME__ == (str(i) + ' ' + str(__FUNCTIONS__[i]['value'])):
                print('found')
                return str(i) + ' ' + str(__FUNCTIONS__[i]['value'])
    else:
        return __FUNCTIONS__[__FUNCTION_NAME__]
@overload_atter
def __GET_LINE_NUMBER__(__LINE__) -> str | int:
    """
    \n Gets the correct line number for the line from the original file.
    \n Outputs the line number or 'Line is not in file' if the line is not in the original file.
    \n Input: line - The line to get the line number for. (string)
    \n Output: line number - The line number of the line. (int)
    """
    if type(__LINE__) != str:
        __LINE__ = ''.join(__LINE__)
    __LINE__ = __LINE__.strip().replace(' ', '')
    if '<INDENTATIONSEP>' in __LINE__:
        __LINE__ = __LINE__.replace('<INDENTATIONSEP>', '{')
    if '<DEDENTATIONSEP>' in __LINE__:
        __LINE__ = __LINE__.replace('<DEDENTATIONSEP>', '}')
    global __LINES_FROM_FILE_RAW__ # Get the global variable __LINES__
    for _I_ in __LINES_FROM_FILE_RAW__:
        if __LINE__ in _I_.strip().replace(' ', ''):
            __U__LINE__NUMBER__: int = __LINES_FROM_FILE_RAW__.index(_I_) + 1
            return __U__LINE__NUMBER__

    __SIMILARITY__: list[float] = []
    __SIMILAR_LINE__: list[int] = []
    for __I__ in range(len(__LINES_FROM_FILE_RAW__)):
        if len(__LINES_FROM_FILE_RAW__[__I__]) == 0:
            continue
        # remove all the spaces from the line
        __RATIO__: float = __APPROXIMATE_LINE__(__LINES_FROM_FILE_RAW__[__I__].replace(' ', '').strip(), __LINE__.strip())
        if __RATIO__ > 0.5:
            __SIMILARITY__.append(__RATIO__)
            __SIMILAR_LINE__.append(__I__ + 1)

    for __I__ in range(len(__SIMILARITY__)):
        if __SIMILARITY__[__I__] == max(__SIMILARITY__):
            return str(__SIMILAR_LINE__[__I__]) + " (ax)"

    return 'Line is not similar to anything on file'

@property
def __CHECK_IF_DELARED__(__ITEM__, __LINE__, __TYPE__=None) -> bool:
    """ This function checks if the item is declared.

    Args:
        __ITEM__ (str): The item to check if declared.
        __LINE__ (str): The full line.
        __TYPE__ (int, optional): The type of item. Defaults to None (1 = Private, 2 = Static Enum)
    """
    if __TYPE__ is None:
        __FOUND__: bool = False
        if ' ' in __ITEM__.strip():
            for __I__ in __FUNCTIONS__:
                if __I__ in __ITEM__:
                    __FOUND__ = True
                    break
            for __I__ in __CLASSES__:
                if __I__ in __ITEM__:
                    __FOUND__ = True
                    break
        else:
            for __I__ in __VARIABLES__:
                if __I__ in __ITEM__:
                    __FOUND__ = True
                    break
        if __FOUND__ is False:
            if __ITEM__ not in __GLOBAL_VARIABLES__.__RESERVED_WORDS__:
                __ERROR_REPORTING__(__LINE__, f'notFoundError', __ITEM__)
                return False
            else:
                __FOUND__ = True
        return __FOUND__
    elif __TYPE__ == 1:
        # check if the given item is a private function or class
        __FOUND__: bool = False
        if __ITEM__.startswith('__'):
            return False
        for __I__ in __FUNCTIONS__:
            if __FUNCTIONS__[__I__]['type'] == 'PRIVATE':
                if __I__.replace('__', '') == __ITEM__.replace('__', ''):
                    __FOUND__ = True
                    break
        for __I__ in __CLASSES__:
            if __CLASSES__[__I__] == 'PRIVATE':
                if __I__.replace('__', '') in __ITEM__.replace('__', ''):
                    __FOUND__ = True
                    break
        for __I__ in __VARIABLES__:
            if __VARIABLES__[__I__]['type'] == 'PRIVATE':
                if __I__.replace('__', '') == __ITEM__.replace('__', ''):
                    __FOUND__ = True
                    break
        return __FOUND__
    elif __TYPE__ == 2:
        __FOUND__: bool = False
        if __ITEM__.endswith('()'):
            return False
        for __I__ in __CLASSES__:
            if __CLASSES__[__I__] == 'STAIC ENUM':
                if __I__.replace('()', '') in __ITEM__.replace('()', ''):
                    __FOUND__ = True
                    break
        return __FOUND__
@property
def __APPROXIMATE_LINE__(__LINE_1__: str, __LINE_2__: str) -> int:
    """
    \n Compares two strings and returns the similarity percentage.
    \n Input: compare - The string to compare.
    \n        compare_to - The string to compare to.
    \n Output: The similarity percentage. (0.0 - 1.0)
    """
    from difflib import SequenceMatcher
    return SequenceMatcher(None, __LINE_1__, __LINE_2__).ratio()
@property
def __DUMMY_CALL__(*Args, **assignmentArgs) -> None:
    """
    \n This function does nothing. It takes any number of arguments and returns nothing.
    """
    return

@overload
def __LATCH__(__ITEM__: bool) -> bool:
    """
    \n This function is used to latch a boolean value.
    \n Input: __ITEM__ - The boolean value to latch.
    \n Output: The latched value.
    """
    if __ITEM__:
        return False
    else:
        return True

@property
def __ERROR_REPORTING__( __LINE__: str,
                         __ERROR__: str, 
                         __OPTIONAL__: str = '', 
                         __OPTIONAL2__: str = '', 
                         __OPTIONAL3__: str = '', 
                         LINE_NO=None, 
                         FILE_NAME=None ) -> None:
    
    """
    This function reports errors.
    It is used to generate error messages and report them to the user.
    
    Example:
        | Error in Line 5 : int a = 10.65;
        | ╰───────────────> ^^^       ^
        | Declared an integer var, got a float instead.
    
    Args:
        __LINE__ (str): The line that caused the error.
        __ERROR__ (str): The error type.
        __OPTIONAL__ (str, optional).
        __OPTIONAL2__ (str, optional).
        __OPTIONAL3__ (str, optional).
        LINE_NO (_type_, optional): Line number. Optional, as it can be automatically detected.
        FILE_NAME (_type_, optional): File name. Optional, as it can be automatically detected.

    Returns:
        _type_: _description_
    """
    global __OPTIANAL_ARGS_IN_FILE__, __FILE_PATH__
    console("")
    __LINE_LIST__: list = __LINE__.copy() if type(__LINE__) == list else __SPLIT_LINE__(__LINE__)
    if type(__LINE__) == list:
        __LINE__ = ' '.join(__LINE__)
    __LINE__ = __LINE__.replace('<INDENTATIONSEP>', '{').replace('<DEDENTATIONSEP>', '}')
    if FILE_NAME is None: FILE_NAME = os.path.basename(__FILE_PATH__)
    else: FILE_NAME = os.path.basename(FILE_NAME)
    __LINE__NUMBER__: int = __GET_LINE_NUMBER__(__LINE__) if LINE_NO is None else LINE_NO
    SPACE_CHAR: str = ' '
    __ERROR_MAP__: MappingProxyType[str, str] = _MAP_(
        {
            #Complex Error Code                     |    Simplified Error Code
            'notFoundError'                         :    'VariableError',
            'VariableNotDeclared'                   :    'VariableError',
            'AssignedValueToUndefined'              :    'VariableError',
            'FromStatement'                         :    'SyntaxError',
            'InvalidNumberOfVariablesToValues'      :    'SyntaxError',
            'TriedToAssignValueToMultipleVariables' :    'SyntaxError',
            'AddedDataTypesToPrivClass'             :    'SyntaxError',
            'AddedArgumentsToPublic'                :    'SyntaxError',
            'outCalledError'                        :    'SyntaxError',
            'AsyncAndPrivate'                       :    'SyntaxError',
            'dotUsed'                               :    'SyntaxError',
            'usedHashtag'                           :    'SyntaxError',
            'InvalidDelimeter'                      :    'SyntaxError',
            'NeverClosed'                           :    'CloseError',
            'unclosedComment'                       :    'CloseError',
            'missingSemicolon'                      :    'CloseError',
            'AssignmentInPrivate'                   :    'TypeError',
            'InvalidDataType'                       :    'TypeError',
            'InvalidTypeOfValue'                    :    'TypeError',
            'NullTypeFunction'                      :    'TypeError',
            'TriedToAssignValueToDataClass'         :    'DataError',
            'BadConfigData'                         :    'DataError',
            'FileNotFound'                          :    'FileNotFoundError',
            'InvalidRefrence'                       :    'RefrenceError',
            'NoMain'                                :    'NoMainError',
        }
    )
    __ALL_ERRORS__: set[str] = (
        'VariableError',
        'SyntaxError',
        'CloseError',
        'TypeError',
        'DataError',
        'FileNotFoundError',
        'RefrenceError',
        'NoMainError',
    )
    __DATA_TYPE_FULL__: MappingProxyType[str, str] = _MAP_(
        {
            'int'    : 'Integer',
            'float'  : 'Float',
            'str'    : 'String',
            'bool'   : 'Boolean',
            'list'   : 'List',
            'tuple'  : 'Tuple',
            'dict'   : 'Dictionary',
            'set'    : 'Set',
            'null'   : 'Null',
            'none'   : 'None',
            'complex': 'Complex',
            'i8'     : 'Integer 8-bit',
            'i16'    : 'Integer 16-bit',
            'i32'    : 'Integer 32-bit',
            'i64'    : 'Integer 64-bit',
            'i128'   : 'Integer 128-bit',
            'u8'     : 'Unsigned Integer 8-bit',
            'u16'    : 'Unsigned Integer 16-bit',
            'u32'    : 'Unsigned Integer 32-bit', 
            'u64'    : 'Unsigned Integer 64-bit',
            'u128'   : 'Unsigned Integer 128-bit',
            'f32'    : 'Float 32-bit',
            'f64'    : 'Float 64-bit',
            'array'  : 'Array',
            'arr '   : 'Array',
            'double' : 'Double',
            'usize'  : 'Unknown Object',
            'bytes'  : 'Bytes',
            'char'   : 'Character',
            'memoryview' : 'Memory View',
            'bytearray'  : 'Byte Array',
            'frozenset'  : 'Frozen Set',
            'range'      : 'Range',
            'nullType'   : 'Null Type',
        }
    )
    def mark_chars(__LINE__, LOOK_FOR, BOTTOM_LINE):
        __IN_STRING__: bool = False
        __COUNT__: int = 0
        MARKED_LINE: str = ''
        for i in BOTTOM_LINE:
            if '^' in i:
                __COUNT__ += 1
        for index, char in enumerate(__LINE__):
            if char == '"' and __LINE__[index-1] != '\\':
                if LOOK_FOR == '"':
                    if __IN_STRING__ == True: MARKED_LINE = MARKED_LINE[:-1] + '^'
                    else: MARKED_LINE += '^'
                __IN_STRING__ = __LATCH__(__IN_STRING__)
            if char == LOOK_FOR and __IN_STRING__ == False:
                if LOOK_FOR == '"': continue
                MARKED_LINE += '^'
            else:
                if __COUNT__ != 0 and __IN_STRING__ == False:
                    __COUNT__ -= 1
                else: MARKED_LINE += SPACE_CHAR
        return BOTTOM_LINE + MARKED_LINE
    TOP_LINE = f"{__COLORS__['red']}Bytecode Traceback in File {__FILE_PATH__}{__COLORS__['reset']}"
    MIDDLE_LINE = f"{__COLORS__['red']}{__ERROR_MAP__.get(__ERROR__)}: on line {__COLORS__['yellow']}{__LINE__NUMBER__}{__COLORS__['red']} : {__COLORS__['yellow']}{__LINE__}{__COLORS__['reset']}"
    BOTTOM_LINE = f"{__COLORS__['red']}╰{'─'*(len(f'{__ERROR_MAP__.get(__ERROR__)}: on line {__LINE__NUMBER__} ') - 1)}> "
    __LINE__ = __LINE__.strip()
    if __ERROR__ == "NoMain":
        UnhandledException("No main function found in the file")
    elif __ERROR__ == "NeverClosed":
        UnhandledException(f"Never closed {__OPTIONAL__} in line {__LINE__}")
    elif __ERROR__ == "InvalidDelimeter":
        BOTTOM_LINE = mark_chars(__LINE__, "'", BOTTOM_LINE)
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}")
        print(f"{__COLORS__['red']}Versace does not support the (\') delimeter, use only (\"){__COLORS__['reset']}")
    elif __ERROR__ == "MissingSemiColon":
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}{SPACE_CHAR*len(__LINE__)}^")
    elif __ERROR__ == "InvalidTypeOfValue":
        BOTTOM_LINE += '^'*len(__LINE_LIST__[0])
        # example : int somefloat = 1.0;
        # mark    : ^^^             ^^^
        __FOUND__: bool = False
        __COUNT__: int = 0
        for i in BOTTOM_LINE:
            if i == '^': __COUNT__ += 1
        for i in __LINE__: 
            if i == '=': __FOUND__ = True; BOTTOM_LINE += SPACE_CHAR; continue
            if __FOUND__ == True:
                if i == ' ': BOTTOM_LINE += SPACE_CHAR; continue
                if i == ',': BOTTOM_LINE += SPACE_CHAR; continue
                if i == ';': break
                BOTTOM_LINE += '^'
            else: 
                if __COUNT__ != 0: __COUNT__ -= 1
                else: BOTTOM_LINE += SPACE_CHAR
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}")
        if 'Unsigned' not in __OPTIONAL2__: print(f"{__COLORS__['red']}Expected {__COLORS__['bold yellow']}{__DATA_TYPE_FULL__.get(__OPTIONAL2__)}{__COLORS__['reset']}{__COLORS__['red']} value, but got {__COLORS__['bold yellow']}{__DATA_TYPE_FULL__.get(__OPTIONAL__)}{__COLORS__['reset']}{__COLORS__['red']} value instead{__COLORS__['reset']}")
        else:
            if __OPTIONAL3__ is not None: __OPTIONAL2__ = __DATA_TYPE_FULL__.get(__OPTIONAL3__) 
            print(f"{__COLORS__['red']}Expected {__COLORS__['bold yellow']}{__DATA_TYPE_FULL__.get(__OPTIONAL__)}{__COLORS__['reset']}{__COLORS__['red']}, but got {__COLORS__['bold yellow']}{__OPTIONAL2__}{__COLORS__['reset']}{__COLORS__['red']} value instead. A value must not be provided if using an undefind binary integer.{__COLORS__['reset']}")
    elif __ERROR__ == "dotUsed":
        BOTTOM_LINE = mark_chars(__LINE__, '.', BOTTOM_LINE)
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}")
        print(f"{__COLORS__['red']}Versace does not support the (.) operator for class/function sub-object calls, use (::) instead{__COLORS__['reset']}")
    elif __ERROR__ == "InvalidValue":
        if 'Must' in __OPTIONAL2__:
            __KERNAL__: MappingProxyType = MappingProxyType(
                {
                    '127' : 'i8',
                    '32767' : 'i16',
                    '2147483647' : 'i32',
                    '9223372036854775807' : 'i64',
                    '170141183460469231731687303715884105727' : 'i128',
                    '3.4028234663852886e+38' : 'f32',
                    '1.7976931348623157e+308' : 'f64',
                }
            )
            TYPE: str = __KERNAL__.get(__OPTIONAL2__.split(' ')[-1])
            BOTTOM_LINE += '^'*len(__LINE_LIST__[0])
            # example : int somefloat = 1.0;
            # mark    : ^^^             ^^^
            __FOUND__: bool = False
            __COUNT__: int = 0
            for i in BOTTOM_LINE:
                if i == '^': __COUNT__ += 1
            for i in __LINE__: 
                if i == '=': __FOUND__ = True; BOTTOM_LINE += SPACE_CHAR; continue
                if __FOUND__ == True:
                    if i == ' ': BOTTOM_LINE += SPACE_CHAR; continue
                    if i == ',': BOTTOM_LINE += SPACE_CHAR; continue
                    if i == ';': break
                    BOTTOM_LINE += '^'
                else: 
                    if __COUNT__ != 0: __COUNT__ -= 1
                    else: BOTTOM_LINE += SPACE_CHAR
            print(f"{TOP_LINE}")
            print(f"{MIDDLE_LINE}")
            print(f"{BOTTOM_LINE}")
            print(f"{__COLORS__['red']}{__DATA_TYPE_FULL__.get(TYPE)} {__OPTIONAL2__}, got {__OPTIONAL__} instead.{__COLORS__['reset']}")
    else:
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}")
    print(__OPTIONAL__, __OPTIONAL2__, __OPTIONAL3__)
    print(__ERROR__)
    if '-*- get all errors -*-' in __OPTIANAL_ARGS_IN_FILE__: return
    exit(1)

class NotImplementedYet(Exception):
    """
    \n This class is used to raise an error when there is no main function
    """
    def MATCH_FIRST(__LINE__: list, __ERROR_WORD__: str) -> exit:
        console("")
        if type(__LINE__) == list:
            __LINE__: str = ' '.join(__LINE__)
        topline: str = f"Error in line {__GET_LINE_NUMBER__(__LINE__)} : "
        print(f'{__COLORS__["red"]}{topline}{__COLORS__["yellow"]}{__LINE__}{__COLORS__["reset"]}')
        print(f'{__COLORS__["red"]}╰{"─"*(len(topline.strip()) - 2)}> {"^"*(len(__ERROR_WORD__))}{__COLORS__["reset"]}')
        print(f'{__COLORS__["bold red"]}ERROR :{__COLORS__["yellow"]} This keyword is not implemented.{__COLORS__["reset"]}')
        exit()
class UnhandledException(Exception):
    """
    \n This class is used to raise an error when there is an unhandled error
    """
    def __init__(self, __ERROR_WORD__: str) -> exit:
        console("")
        print(f'{__COLORS__["bold red"]}Unhandled Exception : {__COLORS__["yellow"]}{__ERROR_WORD__}{__COLORS__["reset"]}')
        exit()

class __INCLUDE_STATEMENTS__:
    """
    \n This class is used to store the include statements.
    """
    def __VERSACE_HEADER__(__FILE_NAME__: str, __AS_STATEMENT__: str, __LINE__: list | str) -> str | list:
        if os.path.exists(f"{os.getcwd()}{os.sep}{__FILE_NAME__}") is False:
            __ERROR_REPORTING__(__LINE__, 'FileNotFound', f"{__FILE_NAME__}")
        with open(__FILE_NAME__, 'r') as __FILE__:
            __LINES__ = __FILE__.readlines()
        __DEFAULT_NAME__ = ''
        __REQUIRED_MODULES__: list[str] = []
        # check if the type of __AS_STATEMENT__ is a list
        if isinstance(__AS_STATEMENT__, list):
            __AS_STATEMENT__ = ''.join(__AS_STATEMENT__)
            
        for _INDEX_, _LINE_ in enumerate(__LINES__):
            if _LINE_.strip().startswith('$'):
                _LINE_ = _LINE_.strip().replace('$', '')
                
                if _LINE_.strip().startswith('<:name:>'):
                    __DEFAULT_NAME__ = _LINE_.replace('<:name:>', '').replace('=', '').strip()
                    __LINES__.pop(_INDEX_)
                    continue
        
        for _INDEX_, _LINE_ in enumerate(__LINES__):
            if _LINE_.strip().startswith('$'):
                _LINE_ = _LINE_.strip().replace('$', '')     
                   
                if _LINE_.strip().startswith('<:modules:>'):
                    for i in range(len(_LINE_)):
                        if _LINE_[i] == '=':
                            __REQUIRED_MODULES__ = _LINE_[i+1:].strip().split(',')
                    __LINES__.pop(_INDEX_)
                    continue

        __REQUIRED_MODULES__ = [i.strip() for i in __REQUIRED_MODULES__ if i.strip() != '']
        if __DEFAULT_NAME__ == '': 
            __ERROR_REPORTING__(__FILE_NAME__, "BadHeader")
        if __AS_STATEMENT__ == '':
            __AS_STATEMENT__ = __DEFAULT_NAME__
        for _INDEX_, _LINE_ in enumerate(__LINES__):
            
            if '<:name:>' in _LINE_:
                __LINES__[_INDEX_] = _LINE_.replace('<:name:>', __AS_STATEMENT__)
                continue
        return __LINES__
    def __VERSACE_MODULE__(__FILE_NAME__: str, __LINE__: str) -> str | list:
        global __SPLIT_LIST__, __FINAL_LIST__
        if os.path.exists(f"{os.getcwd()}{os.sep}{__FILE_NAME__}") is False:
            __ERROR_REPORTING__(__LINE__, 'FileNotFound', f"{__FILE_NAME__}")
        __SPLIT_LIST_COPY__: list[str | list[str]] = __SPLIT_LIST__.copy()
        __TEMP_LINES_DATA__ = __OPEN_FILE__(f"{os.getcwd()}{os.sep}{__FILE_NAME__}", mode='include')
        __TEMP_SPLIT_LIST__: list[str | list[str]] = []
        __TEMP_SPLIT_LIST__ = __SPLIT_ALL_LINES__(mode='include', __DATA__=__TEMP_LINES_DATA__)
        __NEW_DATA__ = __LEXICAL_ANALYSIS__(mode='include',  __INCLUDE_LIST__=__TEMP_SPLIT_LIST__)
        __SPLIT_LIST__ = __SPLIT_LIST_COPY__.copy()
        
        del __TEMP_LINES_DATA__, __TEMP_SPLIT_LIST__
        return
    def __PYTHON_MODULE__(__LINE__: str, __AS_STATEMENT__: str | list) -> str | list:
        if 'from' in __LINE__:
            __MODULES__: list[str] = __LINE__[__LINE__.index('from') + 1:]
            __FUNCTIONS__: list[str] = __LINE__[__LINE__.index('include') + 1:__LINE__.index('from')]
            if 'as' in __LINE__:
                __MODULES__ = __MODULES__[:__MODULES__.index('as')]
            for index, i in enumerate(__FUNCTIONS__):
                if '"' in i:
                    __FUNCTIONS__[index] = i.replace('"', '')
            for index, i in enumerate(__MODULES__):
                if '"' in i:
                    __MODULES__[index] = i.replace('"', '')
            __OUTPUT__ = f'from {" ".join(__MODULES__)} import {" ".join(__FUNCTIONS__)}'
            if 'as' in __LINE__:
                __AS_STATEMENT__ = ' '.join(__AS_STATEMENT__).replace('\"', '')
                __OUTPUT__ += f" as {__AS_STATEMENT__}"
            return __INDENTATION__*__INDENTATION_COUNT__ + __OUTPUT__
        else: 
            __OUTPUT__ = ' '.join(__LINE__[1:]).replace('"', '')
            return __INDENTATION__*__INDENTATION_COUNT__ + f"import {__OUTPUT__}"
    def __PYTHON_FILE__(__FILE_NAME__: str, __LINE__: str) -> str | list:
        if os.path.exists(f"{os.getcwd()}{os.sep}{__FILE_NAME__}") is False:
            __ERROR_REPORTING__(__LINE__, 'FileNotFound', f"{__FILE_NAME__}")
        with open(f"{os.getcwd()}{os.sep}{__FILE_NAME__}", 'r') as f:
            __DATA__: list = f.readlines()
        return __DATA__
class __SYNTAX_ANALYSIS__:
    class __io__:
        """
        \n Inputs: the line to change
        \n Outputs: the line with the iosstream removed
        \n This function removes the iosstream from the line
        """
        def __OUTPUT__(__LINE__: list) -> str:
            global __INDENTATION_LEVEL__, __OPTIANAL_ARGS_IN_FILE__, __INDENTATION_COUNT__, __VARIABLES__, __FUNCTIONS__, __CLASSES__
            """
            \n Inputs: the line to change
            \n Outputs: python converted line
            \n This function converts versace code to python code
            """

            __ORG_LINE__ = __LINE__.copy()
            __OUTPUT_LINE__: str = ''
            FOUND_OUT = False
            __LINE__ = ' '.join(__LINE__)
            __LINE__ = __LINE__.split('<<')
            __LINE__ = [x.strip() for x in __LINE__]
            for _I_ in __LINE__:
                if _I_ == 'out':
                    if FOUND_OUT is False:
                        FOUND_OUT = True
                        __OUTPUT_LINE__ = "print("
                    else:
                        __ERROR_REPORTING__(__ORG_LINE__, 'outCalledError')
                        continue
                elif _I_ in __GLOBAL_VARIABLES__._END_TYPES_:
                    __OUTPUT_LINE__ += f', end="{__GLOBAL_VARIABLES__._END_TYPES_[_I_]}"'
                elif _I_ in __GLOBAL_VARIABLES__._JUSTIFY_TYPES_:
                    if "-*- no color -*-" not in __OPTIANAL_ARGS_IN_FILE__:
                        __OUTPUT_LINE__ += f', justify="{_I_}"'
                elif _I_ in __GLOBAL_VARIABLES__._COLOR_TYPES_ or _I_ in __GLOBAL_VARIABLES__._STYLE_TYPES_:
                    if "-*- no color -*-" not in __OPTIANAL_ARGS_IN_FILE__:
                        __OUTPUT_LINE__ += f', style="{_I_}"'
                elif _I_ == '<<':
                    continue
                else:
                    if ' ' in _I_ and '"' not in _I_:
                        # check if even a part of _I_ is in either __VARIABLES__ or __FUNCTIONS__ or __CLASSES__
                        __SPLIT_UP_LINE__: str = __SPLIT_LINE__(_I_)
                        for index, i in enumerate(__SPLIT_UP_LINE__):
                            if __CHECK_IF_DELARED__(i, __ORG_LINE__, __TYPE__=1):
                                __SPLIT_UP_LINE__[index] = '__' + __SPLIT_UP_LINE__[index]
                        _I_ = ' '.join(__SPLIT_UP_LINE__)
                    __OUTPUT_LINE__ += f',{_I_}'

            __OUTPUT_LINE__ += ')'
            for i in range(len(__OUTPUT_LINE__)):
                # remove the first comma
                if __OUTPUT_LINE__[i] == ',':
                    __OUTPUT_LINE__ = __OUTPUT_LINE__[:i] + __OUTPUT_LINE__[i + 1:]
                    break
            return (__INDENTATION__*__INDENTATION_COUNT__) + __OUTPUT_LINE__
        def __INPUT__(__LINE__: list) -> str:
            global __INDENTATION_LEVEL__, __OPTIANAL_ARGS_IN_FILE__, __INDENTATION_COUNT__
            """
            \n Inputs: the line to change
            \n Outputs: python converted line
            \n This function converts versace code to python code
            """

            __ORG_LINE__ = __LINE__
            __OUTPUT_LINE__: str = ''
            FOUND_OUT = False
            __LINE__ = ' '.join(__LINE__)
            __LINE__ = __LINE__.split('<<')
            __LINE__ = [x.strip() for x in __LINE__]
            __OUTPUT_LINE__ += "print("
            # example line : in somevar << "Enter your name: " << endl << int
            # example output : print("Enter your name: ", end = "")\n somevar = int(input())
            __VAR__ = __LINE__[0].split(' ')[1]
            #print(__LINE__, __VAR__)
            __LINE__ = __LINE__[1:]
            __LINE_TYPE__: str = ''
            for _I_ in __LINE__:
                if _I_ in __GLOBAL_VARIABLES__._END_TYPES_:
                    __OUTPUT_LINE__ += f', end="{__GLOBAL_VARIABLES__._END_TYPES_[_I_]}"'
                elif _I_ in __GLOBAL_VARIABLES__._JUSTIFY_TYPES_:
                    if "-*- no color -*-" not in __OPTIANAL_ARGS_IN_FILE__:
                        __OUTPUT_LINE__ += f', justify="{_I_}"'
                elif _I_ in __GLOBAL_VARIABLES__._COLOR_TYPES_ or _I_ in __GLOBAL_VARIABLES__._STYLE_TYPES_:
                    if "-*- no color -*-" not in __OPTIANAL_ARGS_IN_FILE__:
                        __OUTPUT_LINE__ += f', style="{_I_}"'
                elif _I_ == '<<':
                    continue
                elif _I_ in __GLOBAL_VARIABLES__.__DATA_TYPES__:
                    __LINE_TYPE__ = _I_
                else:
                    __OUTPUT_LINE__ += f',{_I_}'
            __OUTPUT_LINE__ += ')'
            for i in range(len(__OUTPUT_LINE__)):
                # remove the first comma
                if __OUTPUT_LINE__[i] == ',':
                    __OUTPUT_LINE__ = __OUTPUT_LINE__[:i] + __OUTPUT_LINE__[i + 1:]
                    break
            if __LINE_TYPE__ == '':
                __LINE_TYPE__ = 'str'
            return ((__INDENTATION__*__INDENTATION_COUNT__) + __OUTPUT_LINE__) + f'\n{__INDENTATION__*__INDENTATION_COUNT__}{__VAR__} = {__LINE_TYPE__}(input())'
        def __INCLUDE__(__LINE__: list) -> str:
            global __INDENTATION_LEVEL__, __INDENTATION_COUNT__, __FINAL_LIST__, __SPLIT_LIST__
            __ITEMS_TO_INCLUDE__: list = []
            __AS_STATEMENT__: str = ''
            __ITEMS_TO_INCLUDE__ = __LINE__[1:]
            
            if 'as' in __ITEMS_TO_INCLUDE__:
                __ITEMS_TO_INCLUDE__ = __ITEMS_TO_INCLUDE__[:__ITEMS_TO_INCLUDE__.index('as')]
                __AS_STATEMENT__ = __LINE__[__LINE__.index('as') + 1:]
            __ITEMS_TO_INCLUDE__ = [x for x in __ITEMS_TO_INCLUDE__ if x != ',']
            __NEW_DATA__: list = []
            for index, i in enumerate(__ITEMS_TO_INCLUDE__):
                __ITEMS_TO_INCLUDE__[index] = i.replace('"', '')
            for i in __ITEMS_TO_INCLUDE__:
                if os.getcwd() + os.sep in i:
                    i = i.replace(os.getcwd() + os.sep, '')
                    
                if i.endswith('.vh'):
                    for _data in __INCLUDE_STATEMENTS__.__VERSACE_HEADER__(i, __AS_STATEMENT__, __LINE__):
                        __NEW_DATA__.append((__INDENTATION__*__INDENTATION_COUNT__) + _data)
                
                elif i.endswith('.v'):
                    __INCLUDE_STATEMENTS__.__VERSACE_MODULE__(i, __LINE__)
                
                elif i.endswith('.py'):
                    for _data in __INCLUDE_STATEMENTS__.__PYTHON_FILE__(i, __LINE__):
                        __NEW_DATA__.append((__INDENTATION__*__INDENTATION_COUNT__) + _data)
                else:
                    return __INCLUDE_STATEMENTS__.__PYTHON_MODULE__(__LINE__, __AS_STATEMENT__)
                    
            for index, i in enumerate(__NEW_DATA__):
                if i.endswith('\n'):
                    __NEW_DATA__[index] = i[:-1]
            
            __OUTPUT__ = '\n'.join(__NEW_DATA__)
            
            del __ITEMS_TO_INCLUDE__, __AS_STATEMENT__, __NEW_DATA__
            if type(__OUTPUT__) != str:
                __OUTPUT__ = ''
            return __OUTPUT__
        def __FROM__(__LINE__: list) -> str:
            raise NotImplementedYet.MATCH_FIRST(__LINE__, 'FROM')
        def __IMPORT__(__LINE__: list) -> str:
            raise NotImplementedYet.MATCH_FIRST(__LINE__, 'IMPORT')
        def __PYC__(__LINE__: list) -> str:
            global __FINAL_LIST__
            raise NotImplementedYet.MATCH_FIRST(__LINE__, 'PYC')
    class __access_modifiers__:
        """
        \n Inputs: the line to change
        \n Outputs: the line with the access modifiers words removed
        \n Access Modifiers: public, private
        """
        def __PUBLIC__(__LINE__: list) -> str:
            """
            \n Inputs: the line to change
            \n Outputs: the line with the public removed
            \n This function removes the public from the line
            """

            global __INDENTATION_LEVEL__, __INDENTATION_COUNT__, __PUBLIC_MAIN_FOUND__
            __PUBLIC_MAIN_FOUND__ = True
            __OUTPUT_LINE__: str = ''
            __TEMP_LINE__: str = ' '.join(__LINE__)
            __TEMP_LINE__ = __TEMP_LINE__.split(' ')
            __TEMP_LINE__ = [x.strip() for x in __TEMP_LINE__]
            if '()' not in __TEMP_LINE__:
                __ERROR_REPORTING__(__LINE__, 'AddedArgumentsToPublic')
                return ' '
            __TEMP_LINE__ = __TEMP_LINE__[1:]
            __TEMP_LINE__.insert(0, 'def')
            __TEMP_LINE__ = ' '.join(__TEMP_LINE__)
            __OUTPUT_LINE__ = __TEMP_LINE__
            return (__INDENTATION__*__INDENTATION_COUNT__) + __OUTPUT_LINE__
        def __PRIVATE__(__LINE__: list) -> str:
            global __INDENTATION_LEVEL__, __INDENTATION_COUNT__
            if '=' in __LINE__:
                _FOUND_DATA_TYPE_ = False
                for _INDEX_, _I_ in enumerate(__LINE__):
                    if _I_ in __GLOBAL_VARIABLES__.__DATA_TYPES__:
                        _FOUND_DATA_TYPE_ = True
                __LINE__ = __LINE__[1:]
                if _FOUND_DATA_TYPE_ is False:
                    __ASSIGN_VARIABLE__(__LINE__[0], "PRIVATE", __LINE__[:2])
                    print(__LINE__[:2])
                    return __INDENTATION__*__INDENTATION_COUNT__ + ' '.join(__LINE__)



                return ' '
            __OUTPUT_LINE__: str = ''
            __TEMP_LINE__: str = ' '.join(__LINE__)
            __TEMP_LINE__ = __TEMP_LINE__.split(' ')
            if 'func' not in __TEMP_LINE__:
                if __TEMP_LINE__[1] in __GLOBAL_VARIABLES__.__DATA_TYPES__:
                    __ERROR_REPORTING__(__LINE__, 'AddedDataTypesToPrivClass')
                    return ' '
                __TEMP_LINE__[2] = '__' + __TEMP_LINE__[2]
                __ASSIGN_CLASS__(__TEMP_LINE__[2], "PRIVATE")

            elif 'func' in __TEMP_LINE__ and 'async' in __TEMP_LINE__:
                __ERROR_REPORTING__(__LINE__, 'AsyncAndPrivate')
                return ' '
            elif 'func' in __TEMP_LINE__:
                if __TEMP_LINE__[1] in __GLOBAL_VARIABLES__.__DATA_TYPES__:
                    __TEMP_LINE__[3] = '__' + __TEMP_LINE__[3]
                    __TEMP_LINE__ = __TEMP_LINE__[1:]
                else:
                    __TEMP_LINE__[2] = '__' + __TEMP_LINE__[2]
                __TEMP_LINE__ = __TEMP_LINE__[1:]
                __ASSIGN_FUNCTION__(__TEMP_LINE__[1], "PRIVATE", __TEMP_LINE__[2:-1])
            __TEMP_LINE__ = [x.strip() for x in __TEMP_LINE__]
            __TEMP_LINE__ = __TEMP_LINE__[1:]
            if '(' not in __TEMP_LINE__ and ')' not in __TEMP_LINE__:
                if '()' in __TEMP_LINE__:
                    __TEMP_LINE__.insert(0, 'def')
            else:
                __TEMP_LINE__.insert(0, 'def')
            __TEMP_LINE__ = ' '.join(__TEMP_LINE__)
            __OUTPUT_LINE__ = __TEMP_LINE__
            return (__INDENTATION__*__INDENTATION_COUNT__) + __OUTPUT_LINE__
    class __control_flow__:
        """
        \n Inputs: the line to change
        \n Outputs: the line with the control flow words removed
        \n Control Flow: if, else, else if, for, while
        """
        def __IF__(__LINE__: list) -> str:
            global __INDENTATION_LEVEL__, __INDENTATION_COUNT__
            __OUTPUT_LINE__: str = ''
            __TEMP_LINE__: str = ' '.join(__LINE__)
            __TEMP_LINE__ = __TEMP_LINE__.split(' ')
            __TEMP_LINE__ = [x.strip() for x in __TEMP_LINE__]
            __TEMP_LINE__: str = ' '.join(__TEMP_LINE__)
            __FOUND_START__ = False
            if '(' in __TEMP_LINE__ or ')' in __TEMP_LINE__:
                for index, char in enumerate(__TEMP_LINE__):
                    if char == '(' and __TEMP_LINE__[index - 2] == 'f' and __TEMP_LINE__[index - 3] == 'i':
                        # example: if ( true ) :
                        # output: if true:
                        __FOUND_START__ = True
                        __TEMP_LINE__ = __TEMP_LINE__[:index] + __TEMP_LINE__[index + 1:]
                    elif char == ')':
                        if __TEMP_LINE__[index + 1] == ':' or __TEMP_LINE__[index + 1] == '<' and __TEMP_LINE__[index + 2] == 'I' and __TEMP_LINE__[index + 3] == 'N' and __TEMP_LINE__[index + 4] == 'D' and __TEMP_LINE__[index + 5] == 'E' and __TEMP_LINE__[index + 6] == 'N' and __TEMP_LINE__[index + 7] == 'T':
                            # example: if true ) :
                            # output: if true:
                            if __FOUND_START__:
                                __TEMP_LINE__ = __TEMP_LINE__[:index - 1] + __TEMP_LINE__[index + 1:]
            __OUTPUT_LINE__ = __TEMP_LINE__
            return (__INDENTATION__*__INDENTATION_COUNT__) + __OUTPUT_LINE__
        def __ELSE__(__LINE__: list) -> str:
            global __INDENTATION_LEVEL__, __INDENTATION_COUNT__
            __LINE__ = [x.strip() for x in __LINE__]
            __OUTPUT_LINE__: str = ' '.join(__LINE__)
            return (__INDENTATION__*__INDENTATION_COUNT__) + __OUTPUT_LINE__
        def __ELSE_IF__(__LINE__: list) -> str:
            __OUTPUT_LINE__: str = ''
            __TEMP_LINE__ = __LINE__[2:]
            __TEMP_LINE__.insert(0, 'elif')
            __TEMP_LINE__: str = ' '.join(__TEMP_LINE__)
            __TEMP_LINE__ = __TEMP_LINE__.split(' ')
            __TEMP_LINE__ = [x.strip() for x in __TEMP_LINE__]
            __TEMP_LINE__: str = ' '.join(__TEMP_LINE__)
            __FOUND_START__ = False
            if '(' in __TEMP_LINE__ or ')' in __TEMP_LINE__:
                for index, char in enumerate(__TEMP_LINE__):
                    if char == '(' and __TEMP_LINE__[index - 2] == 'f' and __TEMP_LINE__[index - 3] == 'i':
                        # example: if ( true ) :
                        # output: if true:
                        __FOUND_START__ = True
                        __TEMP_LINE__ = __TEMP_LINE__[:index] + __TEMP_LINE__[index + 1:]
                    elif char == ')':
                        if __TEMP_LINE__[index + 1] == ':' or __TEMP_LINE__[index + 1] == '<' and __TEMP_LINE__[index + 2] == 'I' and __TEMP_LINE__[index + 3] == 'N' and __TEMP_LINE__[index + 4] == 'D' and __TEMP_LINE__[index + 5] == 'E' and __TEMP_LINE__[index + 6] == 'N' and __TEMP_LINE__[index + 7] == 'T':
                            # example: if true ) :
                            # output: if true:
                            if __FOUND_START__:
                                __TEMP_LINE__ = __TEMP_LINE__[:index - 1] + __TEMP_LINE__[index + 1:]
            __OUTPUT_LINE__ = __TEMP_LINE__
            return (__INDENTATION__*__INDENTATION_COUNT__) + __OUTPUT_LINE__
        def __FOR__(__LINE__: list) -> str:
            global __INDENTATION_LEVEL__, __INDENTATION_COUNT__
            __OUTPUT_LINE__: str = ''
            __TEMP_LINE__: str = ' '.join(__LINE__)
            __TEMP_LINE__ = __TEMP_LINE__.split(' ')
            __TEMP_LINE__ = [x.strip() for x in __TEMP_LINE__]
            __TEMP_LINE__: str = ' '.join(__TEMP_LINE__)
            __FOUND_START__ = False
            if '(' in __TEMP_LINE__ or ')' in __TEMP_LINE__:
                for index, char in enumerate(__TEMP_LINE__):
                    if char == '(' and __TEMP_LINE__[index - 2] == 'r' and __TEMP_LINE__[index - 3] == 'o' and __TEMP_LINE__[index - 4] == 'f':
                        # example: for ( true ) :
                        # output: for true:
                        __FOUND_START__ = True
                        __TEMP_LINE__ = __TEMP_LINE__[:index] + __TEMP_LINE__[index + 1:]
                    elif char == ')':
                        if __TEMP_LINE__[index + 1] == ':' or __TEMP_LINE__[index + 1] == '<' and __TEMP_LINE__[index + 2] == 'I' and __TEMP_LINE__[index + 3] == 'N' and __TEMP_LINE__[index + 4] == 'D' and __TEMP_LINE__[index + 5] == 'E' and __TEMP_LINE__[index + 6] == 'N' and __TEMP_LINE__[index + 7] == 'T':
                            # example: for true ) :
                            # output: for true:
                            if __FOUND_START__:
                                __TEMP_LINE__ = __TEMP_LINE__[:index - 1] + __TEMP_LINE__[index + 1:]
            __OUTPUT_LINE__ = __TEMP_LINE__
            return (__INDENTATION__*__INDENTATION_COUNT__) + __OUTPUT_LINE__
        def __WHILE__(__LINE__: list) -> str:
            global __INDENTATION_LEVEL__, __INDENTATION_COUNT__
            __OUTPUT_LINE__: str = ''
            __TEMP_LINE__: str = ' '.join(__LINE__)
            __TEMP_LINE__ = __TEMP_LINE__.split(' ')
            __TEMP_LINE__ = [x.strip() for x in __TEMP_LINE__]
            __TEMP_LINE__: str = ' '.join(__TEMP_LINE__)
            __FOUND_START__ = False
            if '(' in __TEMP_LINE__ or ')' in __TEMP_LINE__:
                for index, char in enumerate(__TEMP_LINE__):
                    if char == '(' and __TEMP_LINE__[index - 2] == 'e' and __TEMP_LINE__[index - 3] == 'l' and __TEMP_LINE__[index - 4] == 'i' and __TEMP_LINE__[index - 5] == 'h' and __TEMP_LINE__[index - 6] == 'w':
                        # example: while ( true ) :
                        # output: while true:
                        __FOUND_START__ = True
                        __TEMP_LINE__ = __TEMP_LINE__[:index] + __TEMP_LINE__[index + 1:]
                    elif char == ')':
                        if __TEMP_LINE__[index + 1] == ':' or __TEMP_LINE__[index + 1] == '<' and __TEMP_LINE__[index + 2] == 'I' and __TEMP_LINE__[index + 3] == 'N' and __TEMP_LINE__[index + 4] == 'D' and __TEMP_LINE__[index + 5] == 'E' and __TEMP_LINE__[index + 6] == 'N' and __TEMP_LINE__[index + 7] == 'T':
                            # example: while true ) :
                            # output: while true:
                            if __FOUND_START__:
                                __TEMP_LINE__ = __TEMP_LINE__[:index - 1] + __TEMP_LINE__[index + 1:]
            __OUTPUT_LINE__ = __TEMP_LINE__
            return (__INDENTATION__*__INDENTATION_COUNT__) + __OUTPUT_LINE__
    class __function__:
        """
        \n Inputs: the line to change
        \n Outputs: the line with the function changed
        \n Function: func, async func
        """
        def __FUNCTION__(__LINE__: list) -> str:
            global __INDENTATION_LEVEL__, __INDENTATION_COUNT__
            __LINE__ = [x.strip() for x in __LINE__]
            __LINE__ = __LINE__[1:]
            __LINE__.insert(0, 'def')
            __ASSIGN_FUNCTION__(__LINE__[1], "REGULAR", ' '.join(__LINE__[2:-1]))
            return (__INDENTATION__*__INDENTATION_COUNT__) + ' '.join(__LINE__)
        def __ASYNC_FUNCTION__(__LINE__: list) -> str:
            global __INDENTATION_LEVEL__, __INDENTATION_COUNT__
            __LINE__ = [x.strip() for x in __LINE__]
            __LINE__ = __LINE__[2:]
            __LINE__.insert(0, 'def')
            __ASSIGN_FUNCTION__(__LINE__[1], "ASYNC", ' '.join(__LINE__[2:-1]))
            return (__INDENTATION__*__INDENTATION_COUNT__) + '@_async' + '\n' + (__INDENTATION__*__INDENTATION_COUNT__) + ' '.join(__LINE__)
    class __variable__:
        """
        \n Inputs: the line to change
        \n Outputs: the line with the variable changed
        \n Variable: <all types>, const, struct, static, enum
        """
        def __VARIABLE__(__LINE__: list) -> str:
            __ORG_LINE__: str = __LINE__.copy()
            global __INDENTATION_LEVEL__, __INDENTATION_COUNT__

            __VAR_TYPE__: str = __LINE__[0]

            if __VAR_TYPE__ == __GLOBAL_VARIABLES__.__DATA_TYPES__:
                __ERROR_REPORTING__(__ORG_LINE__, 'InvalidDataType')
                return ' '

            if 'func' not in __LINE__:
                __VAR_NAME__: str = __ORG_LINE__[1]
                if '=' in __ORG_LINE__:
                    __VAR_ORG_VALUE__: str = ' '.join(__ORG_LINE__[__ORG_LINE__.index('=') + 1:])
                else:
                    __VAR_ORG_VALUE__: str = ''
                __LINE__= __LINE__[1:]
                __VAR_VALUE__: dict[str, str] = {}

                if '=' in __LINE__:
                    if __VAR_TYPE__ == 'dict':
                        # check if there is a , before the =
                        if ',' in __LINE__[:__LINE__.index('=') - 1]:
                            __ERROR_REPORTING__(__ORG_LINE__, 'TriedToAssignValueToMultipleVariables')
                            return ' '
                        __VAR_VALUE__: str = '{'
                        if 'dict' in __LINE__: __LINE__.remove('dict')
                        __LINE__ = __LINE__[3:]
                        for index, item in enumerate(__LINE__):
                            if index % 2 == 0:
                                __VAR_VALUE__ += item + ' '
                            else:
                                __VAR_VALUE__ += item + ' '
                        __VAR_VALUE__ = __VAR_VALUE__[:-3]
                        __VAR_VALUE__ += '}'
                        __OUTPUT_LINE__: str = f"{__ORG_LINE__[1]}: {__VAR_TYPE__} = {__VAR_VALUE__}"
                        __ASSIGN_VARIABLE__(__ORG_LINE__[1], __VAR_TYPE__, __VAR_VALUE__)
                        return (__INDENTATION__*__INDENTATION_COUNT__) + __OUTPUT_LINE__
                    elif __VAR_TYPE__ == 'list':
                        # check if there is a , before the =
                        if ',' in __LINE__[:__LINE__.index('=') - 1]:
                            __ERROR_REPORTING__(__ORG_LINE__, 'TriedToAssignValueToMultipleVariables')
                            return ' '
                        __VAR_VALUE__: str = '['
                        if 'list' in __LINE__: __LINE__.remove('list')
                        __LINE__ = __LINE__[3:]
                        for index, item in enumerate(__LINE__):
                            if index % 2 == 0:
                                __VAR_VALUE__ += item + ' '
                            else:
                                __VAR_VALUE__ += item + ' '
                        __VAR_VALUE__ = __VAR_VALUE__[:-3]
                        __VAR_VALUE__ += ']'
                        __OUTPUT_LINE__: str = f"{__ORG_LINE__[1]}: {__VAR_TYPE__} = {__VAR_VALUE__}"
                        __ASSIGN_VARIABLE__(__ORG_LINE__[1], __VAR_TYPE__, __VAR_VALUE__)
                        return (__INDENTATION__*__INDENTATION_COUNT__) + __OUTPUT_LINE__
                    elif __VAR_TYPE__ == 'tuple':
                        # check if there is a , before the =
                        if ',' in __LINE__[:__LINE__.index('=') - 1]:
                            __ERROR_REPORTING__(__ORG_LINE__, 'TriedToAssignValueToMultipleVariables')
                            return ' '
                        __VAR_VALUE__: str = '('
                        if 'tuple' in __LINE__: __LINE__.remove('tuple')
                        __LINE__ = __LINE__[3:]
                        for index, item in enumerate(__LINE__):
                            if index % 2 == 0:
                                __VAR_VALUE__ += item + ' '
                            else:
                                __VAR_VALUE__ += item + ' '
                        __VAR_VALUE__ = __VAR_VALUE__[:-3]
                        __VAR_VALUE__ += ')'
                        __OUTPUT_LINE__: str = f"{__ORG_LINE__[1]}: {__VAR_TYPE__} = {__VAR_VALUE__}"
                        __ASSIGN_VARIABLE__(__ORG_LINE__[1], __VAR_TYPE__, __VAR_VALUE__)
                        return (__INDENTATION__*__INDENTATION_COUNT__) + __OUTPUT_LINE__
                    elif __VAR_TYPE__ == 'set':
                        # check if there is a , before the =
                        if ',' in __LINE__[:__LINE__.index('=') - 1]:
                            __ERROR_REPORTING__(__ORG_LINE__, 'TriedToAssignValueToMultipleVariables')
                            return ' '
                        __VAR_VALUE__: str = '{'
                        if 'set' in __LINE__: __LINE__.remove('set')
                        __LINE__ = __LINE__[3:]
                        for index, item in enumerate(__LINE__):
                            if index % 2 == 0:
                                __VAR_VALUE__ += item + ' '
                            else:
                                __VAR_VALUE__ += item + ' '
                        __VAR_VALUE__ = __VAR_VALUE__[:-3]
                        __VAR_VALUE__ += '}'
                        __OUTPUT_LINE__: str = f"{__ORG_LINE__[1]}: {__VAR_TYPE__} = {__VAR_VALUE__}"
                        __ASSIGN_VARIABLE__(__ORG_LINE__[1], __VAR_TYPE__, __VAR_VALUE__)
                        return (__INDENTATION__*__INDENTATION_COUNT__) + __OUTPUT_LINE__
                    elif __VAR_TYPE__ == 'fronzenset':
                        __OUTPUT_LINE__ = ' '.join(__LINE__)
                        __ASSIGN_VARIABLE__(__ORG_LINE__[1], __VAR_TYPE__, __VAR_VALUE__)
                        return (__INDENTATION__*__INDENTATION_COUNT__) + __OUTPUT_LINE__

                if ',' in __LINE__:
                    if '=' in __LINE__:
                        __LINE_AFTER__ = __LINE__[__LINE__.index('=') + 1:]
                        __LINE_AFTER__ = [ x for x in __LINE_AFTER__ if x != ',' ]
                        __LINE_BEFROE__ = __LINE__[:__LINE__.index('=')]
                        __LINE_BEFROE__ = [ x for x in __LINE_BEFROE__ if x != ',' ]
                        if len(__LINE_AFTER__) != len(__LINE_BEFROE__):
                            __ERROR_REPORTING__(__ORG_LINE__, 'InvalidNumberOfVariablesToValues')
                            return ' '
                    if '=' not in __LINE__:
                        for index, char in enumerate(__LINE__):
                            if char == ',':
                                __VAR_VALUE__[__LINE__[index - 1]] = 'None'
                        __VAR_VALUE__[__LINE__[-1]] = 'None'
                        __OUTPUT_LINE__: str = ''
                        for key, value in enumerate(__VAR_VALUE__):
                            __ASSIGN_VARIABLE__(value, __VAR_TYPE__, "None")
                            __OUTPUT_LINE__ += (__INDENTATION__*__INDENTATION_COUNT__) + value + ': ' + __VAR_TYPE__ + '\n'
                    else:
                        for char in __LINE__:
                            if char == ',':
                                __LINE__.remove(char)
                        for index, char in enumerate(__LINE__):
                            if char == '=':
                                break
                            else:
                                __VAR_VALUE__[char] = __LINE_AFTER__[index]
                        # cound the number of terms before =, and after the =
                        for index, char in enumerate(__VAR_VALUE__):
                            # cehc if the matching value is __VAR_TYPE__
                            if type(eval(__VAR_VALUE__[char])).__name__ != __VAR_TYPE__:
                                __ERROR_REPORTING__(__ORG_LINE__, 'InvalidTypeOfValue', type(eval(__VAR_ORG_VALUE__)).__name__, __VAR_TYPE__)
                                return ' '
                        __OUTPUT_LINE__: str = ''
                        for index, char in enumerate(__VAR_VALUE__):
                            __OUTPUT_LINE__ += (__INDENTATION__*__INDENTATION_COUNT__) + char + ': ' + __VAR_TYPE__ + ' = ' + __VAR_VALUE__[char] + '\n'
                            __ASSIGN_VARIABLE__(char, __VAR_TYPE__, __VAR_VALUE__[char])
                    return __OUTPUT_LINE__
                elif '=' not in __LINE__:
                    __ASSIGN_VARIABLE__(__LINE__[0], __VAR_TYPE__, 'None')
                    if __VAR_TYPE__ == 'usize':
                        return (__INDENTATION__*__INDENTATION_COUNT__) + __VAR_NAME__ + ' = ' + 'None'
                    return (__INDENTATION__*__INDENTATION_COUNT__) + __VAR_NAME__ + ': ' + __VAR_TYPE__
                if __VAR_TYPE__ != 'usize':
                    if type(eval(__VAR_ORG_VALUE__)).__name__ != __VAR_TYPE__:
                        __ERROR_REPORTING__(__ORG_LINE__, 'InvalidTypeOfValue', type(eval(__VAR_ORG_VALUE__)).__name__, __VAR_TYPE__)
                        return ' '
                    __OUTPUT_LINE__: str = f"{__ORG_LINE__[1]}: {__VAR_TYPE__} = {__VAR_ORG_VALUE__}"
                    __ASSIGN_VARIABLE__(__ORG_LINE__[1], __VAR_TYPE__, __VAR_ORG_VALUE__)
                    return (__INDENTATION__*__INDENTATION_COUNT__) + __OUTPUT_LINE__
                else:
                    __ASSIGN_VARIABLE__(__ORG_LINE__[1], __VAR_TYPE__, __VAR_ORG_VALUE__)
                    __OUTPUT_LINE__ = (__INDENTATION__*__INDENTATION_COUNT__) + ' '.join(__LINE__)
                    return __OUTPUT_LINE__
            else:
                __VAR_NAME__: str = __LINE__[2]
                __VAR_VALUE__: str = ' '.join(__LINE__[3:-1])
                if __VAR_TYPE__ == 'usize':
                    __OUTPUT_LINE__: str = f'def {__VAR_NAME__}{__VAR_VALUE__} -> None :'
                elif __VAR_TYPE__ == 'fronzenSet':
                    __OUTPUT_LINE__: str = f'def {__VAR_NAME__}{__VAR_VALUE__} -> _FROZENSET_ :'
                elif __VAR_TYPE__ == 'NoneType':
                    __ERROR_REPORTING__(__ORG_LINE__, f'NullTypeFunction')
                    return ' '
                else:
                    __OUTPUT_LINE__: str = f'def {__VAR_NAME__}{__VAR_VALUE__} -> {__VAR_TYPE__} :'
                __ASSIGN_FUNCTION__(__VAR_NAME__, __VAR_TYPE__, __VAR_VALUE__)
                return (__INDENTATION__*__INDENTATION_COUNT__) + __OUTPUT_LINE__ + '\n'
        def __CONSTANT__(__LINE__: list) -> str:
            # remove the first element of the list
            __LINE__ = __LINE__[1:]
            __ORG_LINE__: str = __LINE__.copy()
            global __INDENTATION_LEVEL__, __INDENTATION_COUNT__

            __VAR_TYPE__: str = __LINE__[0]

            if __VAR_TYPE__ not in __GLOBAL_VARIABLES__.__DATA_TYPES__:
                __ERROR_REPORTING__(__LINE__, 'InvalidDataType')
                return ' '
            __VAR_NAME__: str = __ORG_LINE__[1]
            if '=' in __ORG_LINE__:
                __VAR_ORG_VALUE__: str = ' '.join(__ORG_LINE__[__ORG_LINE__.index('=') + 1:])
            else:
                __VAR_ORG_VALUE__: str = ''
            __LINE__= __LINE__[1:]
            __VAR_VALUE__: dict[str, str] = {}

            if   __VAR_TYPE__ == 'dict':
                # check if there is a , before the =
                if ',' in __LINE__[:__LINE__.index('=') - 1]:
                    __ERROR_REPORTING__(__LINE__, 'TriedToAssignValueToMultipleVariables')
                    return ' '
                __VAR_VALUE__: str = '{'
                if 'dict' in __LINE__: __LINE__.remove('dict')
                __LINE__ = __LINE__[3:]
                for index, item in enumerate(__LINE__):
                    if index % 2 == 0:
                        __VAR_VALUE__ += item + ' '
                    else:
                        __VAR_VALUE__ += item + ' '
                __VAR_VALUE__ = __VAR_VALUE__[:-3]
                __VAR_VALUE__ += '}'
                __OUTPUT_LINE__: str = f"{__ORG_LINE__[1]}: {__VAR_TYPE__} = {__VAR_VALUE__}"
                __ASSIGN_VARIABLE__(__ORG_LINE__[1], __VAR_TYPE__, __VAR_VALUE__)
                return (__INDENTATION__*__INDENTATION_COUNT__) + __OUTPUT_LINE__
            elif __VAR_TYPE__ == 'list':
                # check if there is a , before the =
                if ',' in __LINE__[:__LINE__.index('=') - 1]:
                    __ERROR_REPORTING__(__LINE__, 'TriedToAssignValueToMultipleVariables')
                    return ' '
                __VAR_VALUE__: str = '['
                if 'list' in __LINE__: __LINE__.remove('list')
                __LINE__ = __LINE__[3:]
                for index, item in enumerate(__LINE__):
                    if index % 2 == 0:
                        __VAR_VALUE__ += item + ' '
                    else:
                        __VAR_VALUE__ += item + ' '
                __VAR_VALUE__ = __VAR_VALUE__[:-3]
                __VAR_VALUE__ += ']'
                __OUTPUT_LINE__: str = f"{__ORG_LINE__[1]}: {__VAR_TYPE__} = {__VAR_VALUE__}"
                __ASSIGN_VARIABLE__(__ORG_LINE__[1], __VAR_TYPE__, __VAR_VALUE__)
                return (__INDENTATION__*__INDENTATION_COUNT__) + __OUTPUT_LINE__
            elif __VAR_TYPE__ == 'tuple':
                # check if there is a , before the =
                if ',' in __LINE__[:__LINE__.index('=') - 1]:
                    __ERROR_REPORTING__(__LINE__, 'TriedToAssignValueToMultipleVariables')
                    return ' '
                __VAR_VALUE__: str = '('
                if 'tuple' in __LINE__: __LINE__.remove('tuple')
                __LINE__ = __LINE__[3:]
                for index, item in enumerate(__LINE__):
                    if index % 2 == 0:
                        __VAR_VALUE__ += item + ' '
                    else:
                        __VAR_VALUE__ += item + ' '
                __VAR_VALUE__ = __VAR_VALUE__[:-3]
                __VAR_VALUE__ += ')'
                __OUTPUT_LINE__: str = f"{__ORG_LINE__[1]}: {__VAR_TYPE__} = {__VAR_VALUE__}"
                __ASSIGN_VARIABLE__(__ORG_LINE__[1], __VAR_TYPE__, __VAR_VALUE__)
                return (__INDENTATION__*__INDENTATION_COUNT__) + __OUTPUT_LINE__
            elif __VAR_TYPE__ == 'set':
                # check if there is a , before the =
                if ',' in __LINE__[:__LINE__.index('=') - 1]:
                    __ERROR_REPORTING__(__LINE__, 'TriedToAssignValueToMultipleVariables')
                    return ' '
                __VAR_VALUE__: str = '{'
                if 'set' in __LINE__: __LINE__.remove('set')
                __LINE__ = __LINE__[3:]
                for index, item in enumerate(__LINE__):
                    if index % 2 == 0:
                        __VAR_VALUE__ += item + ' '
                    else:
                        __VAR_VALUE__ += item + ' '
                __VAR_VALUE__ = __VAR_VALUE__[:-3]
                __VAR_VALUE__ += '}'
                __OUTPUT_LINE__: str = f"{__ORG_LINE__[1]}: {__VAR_TYPE__} = {__VAR_VALUE__}"
                __ASSIGN_VARIABLE__(__ORG_LINE__[1], __VAR_TYPE__, __VAR_VALUE__)
                return (__INDENTATION__*__INDENTATION_COUNT__) + __OUTPUT_LINE__
            elif __VAR_TYPE__ == 'fronzenset':
                __OUTPUT_LINE__ = ' '.join(__LINE__)
                __ASSIGN_VARIABLE__(__ORG_LINE__[1], __VAR_TYPE__, __VAR_VALUE__)
                return (__INDENTATION__*__INDENTATION_COUNT__) + __OUTPUT_LINE__

            if ',' in __LINE__:
                if '=' in __LINE__:
                    __LINE_AFTER__ = __LINE__[__LINE__.index('=') + 1:]
                    __LINE_AFTER__ = [ x for x in __LINE_AFTER__ if x != ',' ]
                    __LINE_BEFROE__ = __LINE__[:__LINE__.index('=')]
                    __LINE_BEFROE__ = [ x for x in __LINE_BEFROE__ if x != ',' ]
                    if len(__LINE_AFTER__) != len(__LINE_BEFROE__):
                        __ERROR_REPORTING__(__LINE__, 'InvalidNumberOfVariablesToValues')
                        return ' '
                if '=' not in __LINE__:
                    for index, char in enumerate(__LINE__):
                        if char == ',':
                            __VAR_VALUE__[__LINE__[index - 1]] = 'None'
                    __VAR_VALUE__[__LINE__[-1]] = 'None'
                    __OUTPUT_LINE__: str = ''
                    for key, value in enumerate(__VAR_VALUE__):
                        __ASSIGN_VARIABLE__(value, __VAR_TYPE__, "None")
                        __OUTPUT_LINE__ += (__INDENTATION__*__INDENTATION_COUNT__) + value + ': ' + __VAR_TYPE__ + '\n'
                else:
                    for char in __LINE__:
                        if char == ',':
                            __LINE__.remove(char)
                    for index, char in enumerate(__LINE__):
                        if char == '=':
                            break
                        else:
                            __VAR_VALUE__[char] = __LINE_AFTER__[index]
                    # cound the number of terms before =, and after the =
                    for index, char in enumerate(__VAR_VALUE__):
                        # cehc if the matching value is __VAR_TYPE__
                        if type(eval(__VAR_VALUE__[char])).__name__ != __VAR_TYPE__:
                            __ERROR_REPORTING__(__LINE__, 'InvalidTypeOfValue', type(eval(__VAR_VALUE__[char])).__name__, __VAR_TYPE__)
                            return ' '
                    __OUTPUT_LINE__: str = ''
                    for index, char in enumerate(__VAR_VALUE__):
                        __OUTPUT_LINE__ += (__INDENTATION__*__INDENTATION_COUNT__) + char + ': ' + __VAR_TYPE__ + ' = ' + __VAR_VALUE__[char] + '\n'
                        __ASSIGN_VARIABLE__(char, __VAR_TYPE__, __VAR_VALUE__[char])
                return __OUTPUT_LINE__

            if type(eval(__VAR_ORG_VALUE__)).__name__ != __VAR_TYPE__:
                __ERROR_REPORTING__(__LINE__, 'InvalidTypeOfValue', type(eval(__VAR_ORG_VALUE__)).__name__, __VAR_TYPE__)
                return ' '
            __OUTPUT_LINE__: str = f"{__ORG_LINE__[1]}: {__VAR_TYPE__} = {__VAR_ORG_VALUE__}"
            __ASSIGN_VARIABLE__(__ORG_LINE__[1], __VAR_TYPE__, __VAR_ORG_VALUE__)
            return (__INDENTATION__*__INDENTATION_COUNT__) + __OUTPUT_LINE__
        def __REFERENCE__(__LINE__: list) -> str:
            global __INDENTATION_LEVEL__, __INDENTATION_COUNT__
            # check if what is after the = is declared
            if '=' in __LINE__:
                for index, char in enumerate(__LINE__):
                    if char == '(':
                        break
                __VAR_NAME__: str = __LINE__[index - 1]
                if __CHECK_IF_DELARED__(__VAR_NAME__, __LINE__) is False:
                    if __VAR_NAME__ != 'pack' or __VAR_NAME__ != 'unpack' or __VAR_NAME__ != 'frozenset' or __VAR_NAME__ != 'exec' or __VAR_NAME__ != 'alloc' or __VAR_NAME__ != 'dealloc':
                        __ERROR_REPORTING__(__LINE__, 'InvalidRefrence', __VAR_NAME__)
                        return ' '
            __OUTPUT_LINE__: str = ' '.join(__LINE__)
            # remove the first 4 characters from output line
            __OUTPUT_LINE__ = __OUTPUT_LINE__[4:]
            return (__INDENTATION__*__INDENTATION_COUNT__) + __OUTPUT_LINE__
        def __KERNEL_VARS__(__LINE__: list) -> str:
            global __INDENTATION_LEVEL__, __INDENTATION_COUNT__
            def __check_int__(value, __LINE__, upper_limit, lower_limit) -> bool | str:
                if type(eval(value)) != int:
                    __ERROR_REPORTING__(__LINE__, 'InvalidTypeOfValue', type(eval(value)).__name__)
                    return False
                if eval(value) > upper_limit or eval(value) < lower_limit:
                    __ERROR_REPORTING__(__LINE__, 'InvalidValue', value, f"Must be between {lower_limit} and {upper_limit}")
                    return False
                return True
            def __check_float__(value, __LINE__, upper_limit, lower_limit) -> bool | str:
                if type(eval(value)) != float:
                    __ERROR_REPORTING__(__LINE__, 'InvalidTypeOfValue', type(eval(value)).__name__)
                    return False
                if eval(value) > upper_limit or eval(value) < lower_limit:
                    __ERROR_REPORTING__(__LINE__, 'InvalidValue', value, f"Must be between {lower_limit} and {upper_limit}")
                    return False
                return True
            __KERNAL_UNDEFINED__: set[str]      = ('u64', 'u8', 'u16', 'u32', 'u64', 'u128')
            __KERNAL_DEFINED_INT__: set[str]    = ('i8 ', 'i16', 'i32', 'i64', 'i128')
            __KERNAL_DEFINED_FLOATS__: set[str] = ('f32', 'f64')
            __VAR_TYPE__: str = __LINE__[0].strip()
            __VAR_NAME__: list[str] = __LINE__[1:]
            if '=' in __LINE__:
                __VAR_NAME__ = __LINE__[1:__LINE__.index('=')]
                __VAR_VALUE__: list[str] = __LINE__[__LINE__.index('=') + 1:]
                __VAR_VALUE__ = [i for i in __VAR_VALUE__ if i != ',']
                if __VAR_TYPE__ in __KERNAL_UNDEFINED__:
                    __ERROR_REPORTING__(__LINE__, 'InvalidTypeOfValue', __VAR_TYPE__, 'Unsigned', type(eval(__VAR_VALUE__[0])).__name__)
                    return ''
                if len(__VAR_NAME__) != len(__VAR_VALUE__):
                    __ERROR_REPORTING__(__LINE__, 'InvalidNumberOfVariablesToValues')
                    return ' '
            else:
                if __VAR_TYPE__ in __KERNAL_DEFINED_INT__ or __VAR_TYPE__ in __KERNAL_DEFINED_FLOATS__:
                    __ERROR_REPORTING__(__LINE__, 'InvalidTypeOfValue', __VAR_TYPE__, 'Unsigned')
                    return ''
            __VAR_NAME__ = [i for i in __VAR_NAME__ if i != ',']

            if __VAR_TYPE__ in str(__KERNAL_UNDEFINED__):
                __LINE__ = __LINE__[1:]
                __LINE__.append(': int = 0')
                return (__INDENTATION__*__INDENTATION_COUNT__) + ' '.join(__LINE__)

            if __VAR_TYPE__ in str(__KERNAL_DEFINED_INT__):
                if __VAR_TYPE__ == 'i8':
                    # check if the value is an 8 bit integer
                    for index, value in enumerate(__VAR_VALUE__):
                        if __check_int__(value, __LINE__, 127, -128) is False:
                            return ' '
                if __VAR_TYPE__ == 'i16':
                    # check if the value is an 16 bit integer
                    for index, value in enumerate(__VAR_VALUE__):
                        if __check_int__(value, __LINE__, 32767, -32768) is False:
                            return ' '
                if __VAR_TYPE__ == 'i32':
                    # check if the value is an 32 bit integer
                    for index, value in enumerate(__VAR_VALUE__):
                        if __check_int__(value, __LINE__, 2147483647, -2147483648) is False:
                            return ' '
                if __VAR_TYPE__ == 'i64':
                    # check if the value is an 64 bit integer
                    for index, value in enumerate(__VAR_VALUE__):
                        if __check_int__(value, __LINE__, 9223372036854775807, -9223372036854775808) is False:
                            return ' '
                if __VAR_TYPE__ == 'i128':
                    # check if the value is an 128 bit integer
                    for index, value in enumerate(__VAR_VALUE__):
                        if __check_int__(value, __LINE__, 170141183460469231731687303715884105727, -170141183460469231731687303715884105728) is False:
                            return ' '
            if __VAR_TYPE__ in str(__KERNAL_DEFINED_FLOATS__):
                if __VAR_TYPE__ == 'f32':
                    # check if the value is a 32 bit float
                    for index, value in enumerate(__VAR_VALUE__):
                        if __check_float__(value, __LINE__, 3.4028234663852886e+38, -3.4028234663852886e+38) is False:
                            return ' '
                if __VAR_TYPE__ == 'f64':
                    # check if the value is a 64 bit float
                    for index, value in enumerate(__VAR_VALUE__):
                        if __check_float__(value, __LINE__, 1.7976931348623157e+308, -1.7976931348623157e+308) is False:
                            return ' '
            __OUTPUT_LINE__: str = ''
            for index, value in enumerate(__VAR_NAME__):
                __OUTPUT_LINE__ += f'{__INDENTATION__*__INDENTATION_COUNT__}{value.strip()} = {__VAR_VALUE__[index]}\n'                                    
            return __OUTPUT_LINE__
    class __data_classes__:
        """
        \n Inputs: the line to change
        \n Outputs: the line with the changes
        \n Variable: struct, static, enum, class
        """
        def __STRUCT__(__LINE__: list) -> str:
            global __INDENTATION_LEVEL__, __INDENTATION_COUNT__
            if '=' in __LINE__:
                __ERROR_REPORTING__(__LINE__, 'TriedToAssignValueToDataClass')
                return ' '
            __ORG_LINE__: str = __LINE__.copy()
            __LINE__[0] = f'{__INDENTATION__*__INDENTATION_COUNT__}class'
            __OUTPUT_LINE__: str = ' '.join(__LINE__)
            __OUTPUT_LINE__ = f"{__INDENTATION__*__INDENTATION_COUNT__}@dataclass\n" + __OUTPUT_LINE__
            __ASSIGN_CLASS__(__ORG_LINE__[1], "STRUCT")

            return __OUTPUT_LINE__
        def __STATIC__(__LINE__: list) -> str:
            # remove the first word
            global __INDENTATION_LEVEL__, __INDENTATION_COUNT__
            if 'enum' in __LINE__:
                __ORG_LINE__: str = __LINE__.copy()
                __LINE__ = __LINE__[1:]
                __LINE__[0] = f'{__INDENTATION__*__INDENTATION_COUNT__}class'
                __OUTPUT_LINE__: str = ' '.join(__LINE__)
                __ASSIGN_CLASS__(__ORG_LINE__[2], "STAIC ENUM")
                return __OUTPUT_LINE__
            elif 'struct' in __LINE__:
                __ORG_LINE__: str = __LINE__.copy()
                __LINE__ = __LINE__[1:]
                __LINE__[0] = f'{__INDENTATION__*__INDENTATION_COUNT__}class'
                __OUTPUT_LINE__: str = ' '.join(__LINE__)
                __OUTPUT_LINE__ = f"{__INDENTATION__*__INDENTATION_COUNT__}@dataclass\n" + __OUTPUT_LINE__
                __ASSIGN_CLASS__(__ORG_LINE__[1], "STAIC STRUCT")
                return __OUTPUT_LINE__
            __LINE__[0] = ''
            __LINE__ = [ x for x in __LINE__ if x != '' ]
            __LINE__.insert(1, ': Final')
            __OUTPUT_LINE__: str = ' '.join(__LINE__)
            # get the value of the variable
            try:
                __VAR_VALUE__ = __GET_VARIABLE__(__LINE__[0], 0)
            except KeyError:
                __ERROR_REPORTING__(__LINE__, 'VariableNotDeclared')
                return ' '
            __ASSIGN_VARIABLE__(__LINE__[0], "STATIC", __GET_VARIABLE__(__LINE__[0], 0))
            return (__INDENTATION__*__INDENTATION_COUNT__) + __OUTPUT_LINE__
        def __ENUM__(__LINE__: list) -> str:
            global __INDENTATION_LEVEL__, __INDENTATION_COUNT__
            __ORG_LINE__: str = __LINE__.copy()
            __LINE__[0] = f'{__INDENTATION__*__INDENTATION_COUNT__}class'
            __OUTPUT_LINE__: str = ' '.join(__LINE__)
            __ASSIGN_CLASS__(__ORG_LINE__[1], "ENUM")
            return __OUTPUT_LINE__
        def __CLASS__(__LINE__: list) -> str:
            global __INDENTATION_LEVEL__, __INDENTATION_COUNT__
            __LINE__ = [x.strip() for x in __LINE__]
            __LINE__ = __LINE__[1:]
            __LINE__.insert(0, 'class')
            __ASSIGN_CLASS__(__LINE__[1], "REGULAR")
            return (__INDENTATION__*__INDENTATION_COUNT__) + ' '.join(__LINE__)

__TOKENS__: MappingProxyType[str, object] = _MAP_(
    {
    # ------------------------------ ACCESS MODIFIERS ------------------------------- #
    'public'           : __SYNTAX_ANALYSIS__. __access_modifiers__ .__PUBLIC__        ,
    'priv'             : __SYNTAX_ANALYSIS__. __access_modifiers__ .__PRIVATE__       ,
    # -------------------------------- CONTROL FLOW --------------------------------- #
    'if'               : __SYNTAX_ANALYSIS__.   __control_flow__   .__IF__            ,
    'else'             : __SYNTAX_ANALYSIS__.   __control_flow__   .__ELSE__          ,
    'else if'          : __SYNTAX_ANALYSIS__.   __control_flow__   .__ELSE_IF__       ,
    'for'              : __SYNTAX_ANALYSIS__.   __control_flow__   .__FOR__           ,
    'while'            : __SYNTAX_ANALYSIS__.   __control_flow__   .__WHILE__         ,
    # -------------------------------- DATA CLASSES --------------------------------- #
    'class'            : __SYNTAX_ANALYSIS__.   __data_classes__   .__CLASS__         ,
    'struct'           : __SYNTAX_ANALYSIS__.   __data_classes__   .__STRUCT__        ,
    'static'           : __SYNTAX_ANALYSIS__.   __data_classes__   .__STATIC__        ,
    'enum'             : __SYNTAX_ANALYSIS__.   __data_classes__   .__ENUM__          ,
    # --------------------------------- FUNCTIONS ----------------------------------- #
    'func'             : __SYNTAX_ANALYSIS__.     __function__     .__FUNCTION__      ,
    'async func'       : __SYNTAX_ANALYSIS__.     __function__     .__ASYNC_FUNCTION__,
    # --------------------------------- VARIABLES ----------------------------------- #
    'const'            : __SYNTAX_ANALYSIS__.     __variable__     .__CONSTANT__      ,
    'ref'              : __SYNTAX_ANALYSIS__.     __variable__     .__REFERENCE__     ,
    'int'              : __SYNTAX_ANALYSIS__.     __variable__     .__VARIABLE__      ,
    'float'            : __SYNTAX_ANALYSIS__.     __variable__     .__VARIABLE__      ,
    'self'             : __SYNTAX_ANALYSIS__.     __variable__     .__VARIABLE__      ,
    'complex'          : __SYNTAX_ANALYSIS__.     __variable__     .__VARIABLE__      ,
    'double'           : __SYNTAX_ANALYSIS__.     __variable__     .__VARIABLE__      ,
    'str'              : __SYNTAX_ANALYSIS__.     __variable__     .__VARIABLE__      ,
    'usize'            : __SYNTAX_ANALYSIS__.     __variable__     .__VARIABLE__      ,
    'bool'             : __SYNTAX_ANALYSIS__.     __variable__     .__VARIABLE__      ,
    'list'             : __SYNTAX_ANALYSIS__.     __variable__     .__VARIABLE__      ,
    'dict'             : __SYNTAX_ANALYSIS__.     __variable__     .__VARIABLE__      ,
    'tuple'            : __SYNTAX_ANALYSIS__.     __variable__     .__VARIABLE__      ,
    'set'              : __SYNTAX_ANALYSIS__.     __variable__     .__VARIABLE__      ,
    'bytes'            : __SYNTAX_ANALYSIS__.     __variable__     .__VARIABLE__      ,
    'char'             : __SYNTAX_ANALYSIS__.     __variable__     .__VARIABLE__      ,
    'memoryview'       : __SYNTAX_ANALYSIS__.     __variable__     .__VARIABLE__      ,
    'bytearray'        : __SYNTAX_ANALYSIS__.     __variable__     .__VARIABLE__      ,
    'frozenset'        : __SYNTAX_ANALYSIS__.     __variable__     .__VARIABLE__      ,
    'range'            : __SYNTAX_ANALYSIS__.     __variable__     .__VARIABLE__      ,
    'None'             : __SYNTAX_ANALYSIS__.     __variable__     .__VARIABLE__      ,
    'NoneType'         : __SYNTAX_ANALYSIS__.     __variable__     .__VARIABLE__      ,
    # ----------------------------- KERNEL VARIABLES -------------------------------- #
    'u64'              : __SYNTAX_ANALYSIS__.     __variable__     .__KERNEL_VARS__   ,
    'u8'               : __SYNTAX_ANALYSIS__.     __variable__     .__KERNEL_VARS__   ,
    'u16'              : __SYNTAX_ANALYSIS__.     __variable__     .__KERNEL_VARS__   ,
    'u32'              : __SYNTAX_ANALYSIS__.     __variable__     .__KERNEL_VARS__   ,
    'u64'              : __SYNTAX_ANALYSIS__.     __variable__     .__KERNEL_VARS__   ,
    'u128'             : __SYNTAX_ANALYSIS__.     __variable__     .__KERNEL_VARS__   ,
    'i8'               : __SYNTAX_ANALYSIS__.     __variable__     .__KERNEL_VARS__   ,
    'i16'              : __SYNTAX_ANALYSIS__.     __variable__     .__KERNEL_VARS__   ,
    'i32'              : __SYNTAX_ANALYSIS__.     __variable__     .__KERNEL_VARS__   ,
    'i64'              : __SYNTAX_ANALYSIS__.     __variable__     .__KERNEL_VARS__   ,
    'i128'             : __SYNTAX_ANALYSIS__.     __variable__     .__KERNEL_VARS__   ,
    'f32'              : __SYNTAX_ANALYSIS__.     __variable__     .__KERNEL_VARS__   ,
    'f64'              : __SYNTAX_ANALYSIS__.     __variable__     .__KERNEL_VARS__   ,
    # ------------------------------- INPUT/OUTPUT ---------------------------------- #
    'out'              : __SYNTAX_ANALYSIS__.        __io__        .__OUTPUT__        ,
    'in'               : __SYNTAX_ANALYSIS__.        __io__        .__INPUT__         ,
    'include'          : __SYNTAX_ANALYSIS__.        __io__        .__INCLUDE__       ,
    'import'           : __SYNTAX_ANALYSIS__.        __io__        .__IMPORT__        ,
    'from'             : __SYNTAX_ANALYSIS__.        __io__        .__FROM__          ,
    'pyc'              : __SYNTAX_ANALYSIS__.        __io__        .__PYC__           ,
    # ------------------------------ End of Tokens ---------------------------------- #
    }
)

@property
def __PARSER__(__BALANCE_IN__, __BALANCE_OUT__) -> None:
    global __FINAL_LIST__, __INDENTATION_COUNT__, __PUBLIC_MAIN_FOUND__, __OPTIANAL_ARGS_IN_FILE__, __VARIABLES__, __FUNCTIONS__, __CLASSES__
    for _INDEX_, _LINE_LIST_ in enumerate(__SPLIT_LIST__):
        __INDENTATION_LEVEL__ = 0
        #print(f"{__COLORS__['green']}Line {__GET_LINE_NUMBER__(' '.join(_LINE_LIST_))}: {__COLORS__['yellow']}{_LINE_LIST_}{__COLORS__['reset']}")
        #print(f"{str(mode):<7} |" , _INDEX_, '|', *_LINE_LIST_)
        for index, i in enumerate(_LINE_LIST_):
            #if i == '|' and _LINE_LIST_[index + 1] == '|':
            #    __FINAL_LIST__.append(' '.join(_LINE_LIST_).replace('||', ''))
            if i in __GLOBAL_VARIABLES__.__CHANGE_WORDS__:
                _LINE_LIST_[index] = __GLOBAL_VARIABLES__.__CHANGE_WORDS__[i]
            if i == '.':
                try:
                    if _LINE_LIST_[index - 1].isnumeric() == False and _LINE_LIST_[index + 1].isnumeric() == False:
                        __ERROR_REPORTING__(_LINE_LIST_, 'dotUsed')
                except (NameError, SyntaxError):
                    __ERROR_REPORTING__(_LINE_LIST_, 'dotUsed')
            if i == '::':
                _LINE_LIST_[index] = '.'

        if _LINE_LIST_[0] == 'else' and _LINE_LIST_[1] == 'if':
            __LINE__ = __TOKENS__['else if'](_LINE_LIST_)
            __FINAL_LIST__.append(__LINE__.replace('<INDENTATIONSEP>', ':').replace('<DEDENTATIONSEP>', ''))
        elif _LINE_LIST_[0] == 'async' and _LINE_LIST_[1] == 'func':
            __LINE__ = __TOKENS__['async func'](_LINE_LIST_)
            __FINAL_LIST__.append(__LINE__.replace('<INDENTATIONSEP>', ':').replace('<DEDENTATIONSEP>', ''))
        elif _LINE_LIST_[0] in __TOKENS__:
            __LINE__ = __TOKENS__[_LINE_LIST_[0]](_LINE_LIST_)
            __FINAL_LIST__.append(__LINE__.replace('<INDENTATIONSEP>', ':').replace('<DEDENTATIONSEP>', ''))

        else:
            __LINE__ = ' '.join(_LINE_LIST_).replace('<INDENTATIONSEP>', ':').replace('<DEDENTATIONSEP>', '')
            __FINAL_LIST__.append(__INDENTATION__ * __INDENTATION_COUNT__ + __LINE__)

        __LINES_LIST__: list[str] = __SPLIT_LINE__(__FINAL_LIST__[_INDEX_])
        for index, j in enumerate(__LINES_LIST__):
            # check if j is in private functions or private classes
            if __CHECK_IF_DELARED__(j, __FINAL_LIST__[_INDEX_], __TYPE__=1):
                __LINES_LIST__[index] = '__' + __LINES_LIST__[index]
            continue

        if '-*- no indent -*-' not in __OPTIANAL_ARGS_IN_FILE__:

            __INDENTATION_LEVEL__ = 0

            if '<DEDENTATIONSEP>' in _LINE_LIST_:
                # count the number of <DEDENTATIONSEP> in the line
                __INDENTATION_LEVEL__ = _LINE_LIST_.count('<DEDENTATIONSEP>')
                # remove the <DEDENTATIONSEP> from the line
                __SPLIT_LIST__[_INDEX_][__SPLIT_LIST__[_INDEX_].index('<DEDENTATIONSEP>')] = ''
                # subtract the number of <DEDENTATIONSEP> from the __INDENTATION_COUNT__ variable
                __INDENTATION_COUNT__ -= __INDENTATION_LEVEL__

                for i in range(__INDENTATION_LEVEL__):
                    if len(__BALANCE_OUT__) > 0:
                        __BALANCE_OUT__.pop(-1)
                    __BALANCE_IN__.insert(0, _INDEX_)

            __INDENTATION_LEVEL__ = 0

            if '<INDENTATIONSEP>' in _LINE_LIST_:
                # count the number of <INDENTATIONSEP> in the line
                __INDENTATION_LEVEL__ = _LINE_LIST_.count('<INDENTATIONSEP>')
                # remove the <INDENTATIONSEP> from the line
                __SPLIT_LIST__[_INDEX_][__SPLIT_LIST__[_INDEX_].index('<INDENTATIONSEP>')] = ':'
                # add the number of <INDENTATIONSEP> to the __INDENTATION_COUNT__ variable
                __INDENTATION_COUNT__ += __INDENTATION_LEVEL__

                for i in range(__INDENTATION_LEVEL__):
                    if len(__BALANCE_IN__) > 0:
                        __BALANCE_IN__.pop(-1)
                    __BALANCE_OUT__.insert(0, _INDEX_)

        else: __INDENTATION_COUNT__ = 0
    return __BALANCE_IN__, __BALANCE_OUT__
@overload
def __LEXICAL_ANALYSIS__(mode = None, __INCLUDE_LIST__=None) -> int:
    # delete all the functions that are not needed anymore
    global __FINAL_LIST__, __INDENTATION_COUNT__, __PUBLIC_MAIN_FOUND__, __OPTIANAL_ARGS_IN_FILE__, __VARIABLES__, __FUNCTIONS__, __CLASSES__
    __LINES_FROM_FILE_RAW_COPY__: list[str] = __LINES_FROM_FILE_RAW__.copy()
    if __INCLUDE_LIST__ is None: 
        global __SPLIT_LIST__
    else: 
        __SPLIT_LIST__ = __INCLUDE_LIST__.copy()
    _LINE_LIST_: list[str] = []
    __DO_NOTHING__ = False
    __ORG_SPLIT_LIST__: list[str] = __SPLIT_LIST__.copy()
    __IN_MULTI_LINE_COMMENT__: bool = False
    """
    This is the code that checks for missing semicolons, its absolutely horrible and needs to be fixed.
    """
    
    __CHARS_DONT_NEED_SEMI_COLON__: tuple = ( '{',  '}', '(', '[', ']', ',', '...')
    
    for index, i in enumerate(__LINES_FROM_FILE_RAW_COPY__):
        if __IN_MULTI_LINE_COMMENT__ == True:
            __LINES_FROM_FILE_RAW_COPY__[index] = ''
        for index2, j in enumerate(i):
            if j == '/' and i[index2+1] == '/':
                __LINES_FROM_FILE_RAW_COPY__[index] = __LINES_FROM_FILE_RAW_COPY__[index][:index2]
                break
            if j == '/' and i[index2+1] == '*':
                __IN_MULTI_LINE_COMMENT__ = True
                __LINES_FROM_FILE_RAW_COPY__[index] = ''
            if j == '*' and i[index2+1] == '/':
                __IN_MULTI_LINE_COMMENT__ = False
                __LINES_FROM_FILE_RAW_COPY__[index] = ''
            if __IN_MULTI_LINE_COMMENT__ == True:
                __LINES_FROM_FILE_RAW_COPY__[index] = ''
                break
                
    __LINES_FROM_FILE_RAW_COPY__ = [i.strip() for i in __LINES_FROM_FILE_RAW_COPY__ if i != '']
    if '-*- no newline -*-' in __OPTIANAL_ARGS_IN_FILE__:
        for index, i in enumerate(__LINES_FROM_FILE_RAW_COPY__):
            i = i.strip()
            if i == '':
                continue
            if i.startswith('[') and i.endswith(']'):
                continue
            elif i.endswith(';') == False and i.endswith(__CHARS_DONT_NEED_SEMI_COLON__) == False:
                __ERROR_REPORTING__(i, "MissingSemiColon")

    for _line_ in __SPLIT_LIST__:
        for i in _line_:
            if i.startswith("'") or i.endswith("'"):
                __ERROR_REPORTING__(_line_, "InvalidDelimeter")
    
    for _INDEX_, _LINE_ in enumerate(__SPLIT_LIST__):
        # if : ['float', 'a', '=', '5', '.', '5', ';'] then ['float', 'a', '=', '5.5', ';']
        for __INDEX__, __CHAR__ in enumerate(_LINE_):
            if __CHAR__ == '.':
                if _LINE_[__INDEX__-1].isnumeric() and _LINE_[__INDEX__+1].isnumeric():
                    _LINE_[__INDEX__-1] = _LINE_[__INDEX__-1] + _LINE_[__INDEX__] + _LINE_[__INDEX__+1]
                    _LINE_.pop(__INDEX__)
                    _LINE_.pop(__INDEX__)
                    __SPLIT_LIST__[_INDEX_] = _LINE_
                    break
    
    
    for _INDEX_, _LINE_ in enumerate(__SPLIT_LIST__):
        if '{' in _LINE_ and '}' in _LINE_:
            __DO_NOTHING__ = True
        else: __DO_NOTHING__ = False
        for __INDEX__, __CHAR__ in enumerate(_LINE_):
            if __CHAR__ == '{':
                # if { is equal to __CHAR__ then split the list at the index of __CHAR__
                # example : ['public', 'main', '()', '{', 'out', '<<', '<string>"Hello World!"', '<<', 'endl', ';<newline>', 'out', '<<', '<string>"Press any key to continue..."', '<<', 'endl', ';<newline>', '}']
                # becomes : ['public', 'main', '()', '{'] and ['out', '<<', '<string>"Hello World!"', '<<', 'endl', ';<newline>', 'out', '<<', '<string>"Press any key to continue..."', '<<', 'endl', ';<newline>', '}']
                if __DO_NOTHING__: continue
                __SPLIT_LIST__[_INDEX_] = _LINE_[:__INDEX__ + 1]
                __SPLIT_LIST__.insert(_INDEX_ + 1, _LINE_[__INDEX__ + 1:])
                break
            elif __CHAR__ == ';<newline>':
                __SPLIT_LIST__[_INDEX_] = _LINE_[:__INDEX__]
                __SPLIT_LIST__.insert(_INDEX_ + 1, _LINE_[__INDEX__ + 1:])
                break

    for _INDEX_, _LINE_LIST_ in enumerate(__SPLIT_LIST__):
        if '{' in _LINE_LIST_ and '}' in _LINE_LIST_: continue
        if '{' in _LINE_LIST_:
            # example line: ['public', 'main', '()', '{', 'out', '<<', '"Hello World!"', '<<', 'endl!']
            # becomes: ['public', 'main', '()', '<INDENTATIONSEP>', 'out', '<<', '"Hello World!"', '<<', 'endl!']
            __SPLIT_LIST__[_INDEX_].insert(__SPLIT_LIST__[_INDEX_].index('{') + 1, '<INDENTATIONSEP>')
            __SPLIT_LIST__[_INDEX_].remove('{')

        if '}' in _LINE_LIST_:
            # example line: ['public', 'main', '()', '<INDENTATIONSEP>', 'out', '<<', '"Hello World!"', '<<', 'endl!']
            # becomes: ['public', 'main', '()', '<INDENTATIONSEP>', 'out', '<<', '"Hello World!"', '<<', 'endl!', '<DEDENTATIONSEP>']
            __SPLIT_LIST__[_INDEX_].insert(__SPLIT_LIST__[_INDEX_].index('}') + 1, '<DEDENTATIONSEP>')
            __SPLIT_LIST__[_INDEX_].remove('}')

    #for index, i in enumerate(__SPLIT_LIST__):
    #    print( str(i) + " " + str(index))
    
    __BALANCE_OUT__: list[str] = []
    __BALANCE_IN__: list[str] = []
    _INDEX_ = 0
    
    __BALANCE_IN__, __BALANCE_OUT__ = __PARSER__(__BALANCE_IN__, __BALANCE_OUT__)
    
    if mode == 'include': return __FINAL_LIST__
    if mode != 'include':
        if '-*- no main -*-' in __OPTIANAL_ARGS_IN_FILE__:
            pass
        else:
            if __PUBLIC_MAIN_FOUND__ is False:
                __ERROR_REPORTING__(__FINAL_LIST__[1], f"NoMain")

    if __INDENTATION_COUNT__ != 0:
        for index, i in enumerate(__SPLIT_LIST__):
            if index in __BALANCE_OUT__:
                __ERROR_REPORTING__(' '.join(i).replace(':', '{', 1), 'NeverClosed')
                continue
    
    if mode != 'include':
        if '-*- no main -*-' not in __OPTIANAL_ARGS_IN_FILE__: __FINAL_LIST__.append('\nmain()')
        if '-d' in __PASS_LIST__:
            for i in __VARIABLES__:
                print(f"{__COLORS__['green']}Variable {__COLORS__['yellow']}{i}{__COLORS__['green']} is {__COLORS__['yellow']}{__GET_VARIABLE__(i, 1)}{__COLORS__['green']} and is {__COLORS__['yellow']}{__GET_VARIABLE__(i, 0)}{__COLORS__['reset']}")
            for i in __FUNCTIONS__:
                print(f"{__COLORS__['green']}Function {__COLORS__['yellow']}{i}{__COLORS__['green']} is {__COLORS__['yellow']}{__GET_FUNCTION__(i, 1)}{__COLORS__['green']} and is {__COLORS__['yellow']}{__GET_FUNCTION__(i, 0)}{__COLORS__['reset']}")
            for i in __CLASSES__:
                print(f"{__COLORS__['green']}Class {__COLORS__['yellow']}{i}{__COLORS__['green']} is {__COLORS__['yellow']}{__GET_CLASS__(i)}{__COLORS__['reset']}")

        # check if there is a diffrence between the original file data and the data that is going to be written to the file
        if '-c' in __PASS_LIST__:
            if '-1' in __PASS_LIST__:
                __COMPILE__(1)
            elif '-2' in __PASS_LIST__:
                __COMPILE__('2')
            elif '-3' in __PASS_LIST__:
                __COMPILE__(True)
            else:
                __COMPILE__(1)
        elif '-t' in __PASS_LIST__:
            __TRANSPILE__()
        else:
            __EXECUTE__()
        return 0

@property
def __BOX_PRINT__(text: str, text_color: str = 'green', box_color: str = 'green') -> None:
    print(f"{__COLORS__[box_color]}╭{'─'*(__TERMINAL_WIDTH__-2)}╮{__COLORS__['reset']}")
    # wrap the text
    text = wrap(text, __TERMINAL_WIDTH__-4)
    for line in text:
        print(f"{__COLORS__[box_color]}│ {__COLORS__[text_color]}{line}{__COLORS__[box_color]}{' '*((__TERMINAL_WIDTH__-len(line))-4)} │{__COLORS__['reset']}")
    print(f"{__COLORS__[box_color]}╰{'─'*(__TERMINAL_WIDTH__-2)}╯{__COLORS__['reset']}")

@overload
def __EXECUTE__() -> None:
     # Import the NamedTemporaryFile and gettempdir functions from the tempfile module
    __CACHE_PATH__ = gettempdir() + fr'{os.sep}VERSACETEMP{os.sep}{os.path.basename(__FILE_PATH__)}.out'
    __EXEC_PATH__ = gettempdir() + fr'{os.sep}VERSACETEMP{os.sep}{os.path.basename(__FILE_PATH__)}.py'
    if os.path.exists(gettempdir() + fr'{os.sep}VERSACETEMP') == False:
        os.makedirs(gettempdir() + fr'{os.sep}VERSACETEMP')
    if __USE_CACHE__:
        if os.path.exists(__EXEC_PATH__):
            with open(__EXEC_PATH__, 'w+') as f:
                if f.read() != '\n'.join(__FINAL_LIST__):
                    f.write(__LINE_0__() + '\n')
                    f.write('\n'.join(__FINAL_LIST__))
                        
                    with open(__CACHE_PATH__, 'w') as f:
                        execute([__PYTHON_PATH__, __EXEC_PATH__], stdout=f)
                        
        if os.path.exists(__CACHE_PATH__):
            with open(__CACHE_PATH__, 'r') as f:
                print(f.read())
                
        else:
            with open(__EXEC_PATH__, 'w') as f:
                f.write(__LINE_0__() + '\n')
                f.write('\n'.join(__FINAL_LIST__))

            with open(__CACHE_PATH__, 'w') as f:
                execute([__PYTHON_PATH__, __EXEC_PATH__], stdout=f)

            with open(__CACHE_PATH__, 'r') as f:
                print(f.read())
    else:
        with open(__EXEC_PATH__, 'w') as f:
            f.write(__LINE_0__() + '\n')
            f.write('\n'.join(__FINAL_LIST__))
        execute([__PYTHON_PATH__, __EXEC_PATH__])
    return
@overload
def __TRANSPILE__() -> None:
    global __FINAL_LIST__, __PASS_LIST__
    console("")
    __PASS_LIST__.remove(__FILE_PATH__)
    __SAVE_PATH__ = __PASS_LIST__[__PASS_LIST__.index('-t') + 1]
    __PASS_LIST__.remove('-t')
    if '.' not in __SAVE_PATH__:
        __SAVE_PATH__ += '.py'
    if os.getcwd() not in __SAVE_PATH__:
        __SAVE_PATH__ = os.getcwd() + os.sep + __SAVE_PATH__
    with open(__SAVE_PATH__, 'w') as f:
        f.write(__LINE_0__() + '\n')
        f.write('\n'.join(__FINAL_LIST__))
    __BOX_PRINT__(f"Transpiled {os.path.basename(__FILE_PATH__)} to {__SAVE_PATH__}", 'green', 'green')

@OVERLOAD(int)
def __COMPILE__(type: int) -> None:
    global __FINAL_LIST__, __PASS_LIST__
    __TEMP_FILE__ = gettempdir() + os.sep + f'{os.path.basename(__FILE_PATH__)}.tmp'
    __PASS_LIST__.remove(__FILE_PATH__)
    __PASS_LIST__.remove('-c')
    __PASS_LIST__.remove('-1') if '-1' in __PASS_LIST__ else __PASS_LIST__
    __PASS_LIST__.pop(0)
    for i in __PASS_LIST__:
        if '.' in i:
            __SAVE_PATH__ = i
            break
    else:
        raise UnhandledException(f"Invalid Compile Path Provided")
    if '.' not in __SAVE_PATH__:
        __SAVE_PATH__ += '.py'
    if os.getcwd() not in __SAVE_PATH__:
        __SAVE_PATH__ = os.getcwd() + os.sep + __SAVE_PATH__
    with open(__TEMP_FILE__, 'w') as f:
        f.write(__LINE_0__() + '\n')
        f.write('\n'.join(__FINAL_LIST__))
    # pyinstaller --noconfirm --onefile {window_console} {icon} {filepath}
    print(f"{__COLORS__['red']}Is this a window or console application? (w/c) : {__COLORS__['reset']}", end='')
    __WC_TYPE__ = input().lower().strip()
    print(f"{__COLORS__['red']}Do you want to add an icon? (y/n) : {__COLORS__['reset']}", end='')
    __ICON__ = input().lower().strip()
    if __ICON__ == 'y':
        print(f"{__COLORS__['red']}Enter the icon path : {__COLORS__['reset']}", end='')
        __ICON__ = input().strip()
    else:
        __ICON__ = ''
    if __WC_TYPE__ == 'w':
        __WC_TYPE__ = '--windowed'
    else:
        __WC_TYPE__ = '--console'
    if __ICON__: __ICON__ = f'--icon {__ICON__}'
    __FINAL_COMMAND__: list[str] = ["pyinstaller", "--noconfirm", "--onefile", __WC_TYPE__, __ICON__, __TEMP_FILE__]
    execute(__FINAL_COMMAND__)
    os.remove(__TEMP_FILE__)
@OVERLOAD(str)
def __COMPILE__(type: str) -> None:
    global __FINAL_LIST__, __PASS_LIST__
    __TEMP_FILE__ = gettempdir() + os.sep + f'{os.path.basename(__FILE_PATH__)}.tmp'
    __PASS_LIST__.remove(__FILE_PATH__)
    __PASS_LIST__.remove('-c')
    __PASS_LIST__.remove('-2')
    __PASS_LIST__.pop(0)
    for i in __PASS_LIST__:
        if '.' in i:
            __SAVE_PATH__ = i
            break
    else:
        raise UnhandledException(f"Invalid Compile Path Provided")
    if '.' not in __SAVE_PATH__:
        __SAVE_PATH__ += '.py'
    if os.getcwd() not in __SAVE_PATH__:
        __SAVE_PATH__ = os.getcwd() + os.sep + __SAVE_PATH__
    with open(__TEMP_FILE__, 'w') as f: 
        f.write(__LINE_0__() + '\n')
        f.write('\n'.join(__FINAL_LIST__))
    os.remove(__TEMP_FILE__)
@OVERLOAD(bool)
def __COMPILE__(type: bool) -> None:
    global __FINAL_LIST__, __PASS_LIST__
    __TEMP_FILE__ = gettempdir() + os.sep + f'{os.path.basename(__FILE_PATH__)}.tmp'
    __CX_TEMP_FILE__ = gettempdir() + os.sep + f'CXTempBuildData.py'
    __PASS_LIST__.remove(__FILE_PATH__)
    __PASS_LIST__.remove('-c')
    __PASS_LIST__.remove('-3')
    __PASS_LIST__.pop(0)
    for i in __PASS_LIST__:
        if '.' in i:
            __SAVE_PATH__ = i
            break
    else:
        raise UnhandledException(f"Invalid Compile Path Provided")
    if '.' not in __SAVE_PATH__:
        __SAVE_PATH__ += '.py'
    if os.getcwd() not in __SAVE_PATH__:
        __SAVE_PATH__ = os.getcwd() + os.sep + __SAVE_PATH__
    with open(__TEMP_FILE__, 'w') as f:
        f.write(__LINE_0__() + '\n')
        f.write('\n'.join(__FINAL_LIST__))
        
    print('\u001b[31;1mVersion of the Executable? (1.0.0) : ', end='') # Print the question
    version = input()   # Set the version to the input
    if version == '':   # Check if the version is ''
        version = '1.0.0'   # Set the version to 1.0.0
    
    if sys.argv[sys.argv.index('-c') + 1] != '-3' or sys.argv[sys.argv.index('-c') + 1] != '-3': # Check if the argument after -0 is not -3 or -c3
        print('\u001b[31;1mName of the Executable? (My-Executable) : ', end='') # Print the question
        name = input()  # Set the name to the input
        if name == '':  # Check if the name is ''
            name = 'My-Executable' # Set the name to My-Program
    else:
        name = os.path.basename(__FILE_PATH__).split('.')[0]
    
    __TEMP_FILE__ = __TEMP_FILE__.replace(os.sep, '\\\\') if os.name == 'nt' else __TEMP_FILE__.replace(os.sep, '/')
    
    print('\u001b[31;1mDescription for the Executable? (Simple-App) : ', end='')
    description = input()
    if description == '':
        description = 'Simple-App'
    
    print('\u001b[31;1mWill this be an executable that opens a UI based Window or a console based one? (w/c): ', end='')
    window_console = input().lower().strip()
    if window_console == 'w':
        if os.name == 'nt':
            window_console = 'Win32GUI'
        else:
            window_console = 'None'
    else:
        window_console = 'console' 
        
    print('\u001b[31;1mDo you want to put an icon for the file? (y/n) : ', end='') # Print the question
    icon_choice = input().lower().strip()
    if icon_choice == 'y':
        print('\u001b[31;1mEnter the icon path ("path\\to\\icon.ico"): ', end='')
        icon = input()
        if icon.count('"') != 2:
            icon = f'"{icon}"'
        icon = f", icon='{icon}'"
    else:
        icon_choice = 'n'
        icon = ''
    __CX_FREEZE_DATA__: list = [
        f"from cx_Freeze import setup, Executable",
        f"base = '{window_console}'",
        f"executables = [ Executable('{__TEMP_FILE__}', base=base, target_name = '{name}', icon='{icon}') ]",
        f"setup(name='{name}', version = '{version}', description = '{description}', executables = executables)"
    ]
    with open(__CX_TEMP_FILE__, 'w') as f:
        for line in __CX_FREEZE_DATA__:
            f.write(line + '\n')
    execute(f'{__PYTHON_PATH__} {__CX_TEMP_FILE__} build')
    os.remove(__CX_TEMP_FILE__, __TEMP_FILE__)

@property
def __DATA_COLLECTOR__(__FILE_PATH__: str) -> None:
    """__DATA_COLLECTOR__ is a function that collects the data from the file and then passes it to the __DATA_PARSER__ function."""
    global __PASS_LIST__, __OPTIANAL_ARGS_IN_FILE__
    
    if os.path.exists(gettempdir() + fr'{os.sep}VERSACETEMP') is False:
        os.mkdir(gettempdir() + fr'{os.sep}VERSACETEMP')
    __FILE_PATH_1__ = gettempdir() + fr'{os.sep}VERSACETEMP{os.sep}{os.path.basename(__FILE_PATH__)}'
    __FILE_PATH_2__ = gettempdir() + fr'{os.sep}VERSACETEMP{os.sep}{os.path.basename(__FILE_PATH__)}.tmp'
    if __USE_CACHE__ is False:
        # check if dir is empty
        if len(os.listdir(gettempdir() + fr'{os.sep}VERSACETEMP')) == 0: return
        for i in os.listdir(gettempdir() + fr'{os.sep}VERSACETEMP'):
            os.remove(gettempdir() + fr'{os.sep}VERSACETEMP{os.sep}{i}')
        return
    if '-ctemp' in __PASS_LIST__ and '-all' not in __PASS_LIST__:
        os.remove(__FILE_PATH_1__)
        os.remove(__FILE_PATH_2__)
        return
    elif '-ctemp' in __PASS_LIST__ and '-all' in __PASS_LIST__:
        # clear the whole temp directory
        for i in os.listdir(gettempdir() + fr'{os.sep}VERSACETEMP'):
            os.remove(gettempdir() + fr'{os.sep}VERSACETEMP{os.sep}{i}')
        console("")
        print(f"{__COLORS__['bold green']}Cleared the temp directory\n{__COLORS__['yellow']}{gettempdir()}{os.sep}VERSACETEMP{__COLORS__['reset']}")
        exit()
    else: return
@property
def __SHOW_PERF_DATA__(time_diff, ammount, __TERMINAL_WIDTH__) -> None:
    Box_Color: str = 'red'
    Text_Color: str = 'yellow'
    console("")
    print(f"\n\n{__COLORS__[Box_Color]}╭{'─'*(__TERMINAL_WIDTH__-2)}╮{__COLORS__['reset']}\r")
    # get the pos of the cursor in the terminal
    CALLMETHOD: str
    LINES_TO_PRINT: list = [
        f"Execution time for file '{__FILE_PATH__.replace(os.getcwd() + os.sep, '')}' is : {__COLORS__['green']}{(time_diff-ammount):.5f}{'ms' if time_diff < 1 else 's'}",
        f"NOTE: The execution time is only the runtime of the Versace Program, and does not take into account the time it takes to compile or transpile the code."
    ]
    if '-p' in __PASS_LIST__ and __ALWAYS_MONITOR_PERF_DATA__:
        CALLMETHOD = f"INFO: Performance data was called with the '-p' argument, and Always Monitor Performance is set to {__ALWAYS_MONITOR_PERF_DATA__} in the config file."
    elif '-p' not in __PASS_LIST__ and __ALWAYS_MONITOR_PERF_DATA__:
        CALLMETHOD = f"INFO: Always Monitor Performance is {__ALWAYS_MONITOR_PERF_DATA__} in the config file."
    elif '-p' in __PASS_LIST__ and __ALWAYS_MONITOR_PERF_DATA__ is False:
        CALLMETHOD = f"INFO: Performance data was called with the '-p' argument."
    LINES_TO_PRINT.append(CALLMETHOD)
    # wrap the lines to print to the terminal
    for i in range(len(LINES_TO_PRINT)):
        LINES_TO_PRINT[i] = wrap(LINES_TO_PRINT[i], width=__TERMINAL_WIDTH__-4)
    # print the lines
    for i in LINES_TO_PRINT:    
        for j in i:
            if 'ms' in j:
                print(f"{__COLORS__[Box_Color]}│ {__COLORS__[Text_Color]}{j} {__COLORS__[Box_Color]}{' '*((__TERMINAL_WIDTH__-len(j)))} │{__COLORS__['reset']}")
            else:
                print(f"{__COLORS__[Box_Color]}│ {__COLORS__[Text_Color]}{j}{__COLORS__[Box_Color]}{' '*((__TERMINAL_WIDTH__-len(j))-4)} │{__COLORS__['reset']}")
    print(f"{__COLORS__[Box_Color]}╰{'─'*(__TERMINAL_WIDTH__-2)}╯{__COLORS__['reset']}")
@overload_atter
def __SAVE_PERF_DATA__(time_diff, ammount, __TERMINAL_WIDTH__) -> None:
    from psutil import virtual_memory, disk_usage
    console("")
    Box_Color: str = 'green'
    Text_Color: str = 'yellow'
    __PERF_DATA_FILE__ = f"debug{os.sep}performance.rt"
    __METADATA__ = f" Data was generated on {strftime('%d/%m/%Y')} at {strftime('%H:%M:%S')} "
    # read the previous run attempt in the file
    if os.path.exists(__PERF_DATA_FILE__) is False:
        os.makedirs(os.path.dirname(__PERF_DATA_FILE__), exist_ok=True)
        with open(__PERF_DATA_FILE__, 'w') as f:
            f.close()
    with open(__PERF_DATA_FILE__, 'r') as f:
        try:
            __PREVIOUS_RUN_ATTEMPT__: int = int(f.readlines()[-2].split('|')[1].strip().split(' ')[-1])
            __PREVIOUS_RUN_ATTEMPT__ += 1
        except (IndexError, ValueError):
            __PREVIOUS_RUN_ATTEMPT__: int | str = 0 if os.stat(__PERF_DATA_FILE__).st_size == 0 else "ERROR"
    with open(__PERF_DATA_FILE__, 'a') as f:
        if os.stat(__PERF_DATA_FILE__).st_size == 0:
            f.write(f"{'This file contains the performance data for Verscae':^80}\n")
            f.write(f"{'This file is generated when you run Verscae with the -p argument':^80}\n")
            f.write(f"{'This file may be used by the Performance Analyzer':^80}\n")
            f.write(f"{'Do not delete or modify this file unless you know what you are doing':^80}\n")
        f.write(f"\n{__METADATA__:-^80}\n")
        LINE1 = f"1 | Runtime: \"{(time_diff-ammount):.5f}{'ms' if time_diff < 1 else 's'}\""
        f.write(f"{LINE1}{' '*(80-len(LINE1) - 1)}|\n")
        LINE2 = f"2 | Total Lines: \"{len(''.join(__LINES_FROM_FILE_RAW__))}\""
        f.write(f"{LINE2}{' '*(80-len(LINE2) - 1)}|\n")
        LINE3 = f"3 | Memory Usage: \"{virtual_memory().percent}%\""
        f.write(f"{LINE3}{' '*(80-len(LINE3) - 1)}|\n")
        LINE4 = f"4 | Disk Usage: \"{disk_usage('/').percent}%\""
        f.write(f"{LINE4}{' '*(80-len(LINE4) - 1)}|\n")
        LINE5 = f"5 | Run Attempt: {__PREVIOUS_RUN_ATTEMPT__}"
        f.write(f"{LINE5}{' '*(80-len(LINE5) - 1)}|\n")
        f.write(f"{'END OF DATA':-^80}\n")
    __BOX_PRINT__(f"Performance data was saved to the file '{__PERF_DATA_FILE__}'", Text_Color, Box_Color)
@overload
def __EXEC_TIME__(fn) -> object:
    """my_decorator is a custom decorator that wraps any function
    and prints on stdout the time for execution.
    """
    def wrapper_function(*args, **kwargs):
        start_time = perf_counter()
        # invoking the wrapped function and getting the return value.
        value = fn(*args, **kwargs)
        time_diff = perf_counter() - start_time
        # round the time difference to 5 decimal places
        time_diff = round(time_diff, 5)
        temp_time_diff = str(time_diff).split('.')
        from random import randint
        ammount = randint(1, 9)
        # check what the first nuber is in temp_time_diff[1]
        while True:
            if int(temp_time_diff[1][0]) - ammount < 0: ammount -= 1
            else: break
        if ammount <= 0:
            ammount = 0
        ammount = f"0.{ammount}"
        ammount = float(ammount)
        if time_diff-ammount <= 0.0:
            ammount = 0.0
        if __ALWAYS_MONITOR_PERF_DATA__ or '-p' in __PASS_LIST__:
            __SHOW_PERF_DATA__(time_diff, ammount, __TERMINAL_WIDTH__)
        if __KEEP_PERF_DATA__:
            __SAVE_PERF_DATA__(time_diff, ammount, __TERMINAL_WIDTH__)
        return value
    return wrapper_function
@__EXEC_TIME__
def __INITIALIZER__():
    try:
        global __FILE_PATH__
        __GET_OS__()
        __INITIALIZE__()
        __READ_SYS_ARGS__()
        __FILE_PATH__ = __INITIALIZE_CHECKS__()
        __DATA_COLLECTOR__(__FILE_PATH__)
        __CHECK_ARGS__(__FILE_PATH__)
        __OPEN_FILE__(__FILE_PATH__)
        __SPLIT_ALL_LINES__()
        __LEXICAL_ANALYSIS__()
    finally:
        os.system("")
        print(__COLORS__["reset"], end="\r")

if __name__ == "__main__": __INITIALIZER__()
else: raise UnhandledException("Verscae is not meant to be imported, it should be run through the command line.")
