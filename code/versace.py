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
__ALLOW_PYTHONIC_SYNTAX__ = True

import sys, os, platform
from sys import exit
from io import StringIO 
from time import strftime
from textwrap import wrap
from copy import deepcopy
from time import perf_counter
from re import search, findall
from time import sleep as wait
from tempfile import gettempdir
from os import system as console
from types import MappingProxyType
from subprocess import check_output
from subprocess import run as execute
from contextlib import redirect_stdout
from subprocess import check_call, DEVNULL
_MAP_: MappingProxyType = MappingProxyType
__PASS_LIST__ = sys.argv.copy()
__DEBUG_DATA__: list[str] = []
# check if terminal has color support
class __GLOBAL_VARIABLES__():
    __ALL_PYTHON_KEYWORDS__: tuple[str, ...] = (
        'print',
        'input',
        'if',
        'elif',
        'else',
        'for',
        'while',
        'def', 
        'class',
        'return',
        'break',
        'continue',
        'pass',
        'import',
        'from', 
        'as',
        'global',
        'nonlocal',
        'lambda',
        'try',
        'except',
        'finally',
        'raise',
        'assert',
        'with', 
        'yield', 
        'del',
        'in',
        'is',
        'not',
        'and',
        'or',
        'True',
        'False',
        'None',
        'async',
        'await',
        'as',
        'from',
        'import',
        'nonlocal',
        'self', 
        'super',
        'cls',
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
    'arr',
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
    __END_TYPES__: MappingProxyType[str, str] = _MAP_(
        {
            'newl' : r'\n\n',
            'tab' : r'\t',
            'rw' : r'\r',
            'space' : r' ',
            'endl' : r'',
            'erase' : r'\x1b[2K',
        }
    )
    __JUSTIFY_TYPES__: tuple[str, ...] = (
    'left',
    'right',
    'center',
    'justify',
    )
    __COLOR_TYPES__: tuple[str, ...] = (
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
    __STYLE_TYPES__: tuple[str, ...] = (
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
    r'-*- no init -*-',
    r'-*- no newline -*-',
    r'-*- py -*-',
    r'-*- cache -*-',
    r'-*- exec -*-',
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
            '~'        : '*',
            '~~'       : '**',
            'invert'   : 'reversed',
            'rem'      : 'del',
            'double'   : 'float',
            'char'     : 'str',
            '&&'       : 'and',
            '||'       : 'or',
        }
    )
    __OPPRATORS__: tuple[str, ...] = (
        '<',
        '>',
        '=',
        '!',
        '+',
        '-',
        '*',
        '/',
        '%',
        '^',
        '&',
        '|',    
    )
    __DEF_CHARS__: tuple[str, ...] = (
        '(',
        ')',
        '[',
        ']',
        '{',
        '}',
        ',', 
        ':',
        ';',
        '.',
        '@',
        '_',
        '<',
        '>',
        '=',
        '!',
        '+',
        '-',
        '*',
        '/',
        '%',
        '^',
        '&',
        '|',
        '<',
        '>=',
        '==',
        '!=',
        '+=',
        '-=',
        '*=',
        '/=',
        '%=',
        '^=',
        '&=',
        '|=',
    )
__OS__: str
__BINARY__: int
__WINDOWS__: bool
__USE_CACHE__: bool
__PYTHON_PATH__: str
__INDENTATION__: str
__NO_INCLUDES__: bool
__VERSACE_PATH__: str
__ALLOW_UPDATE__: bool
__NO_ARGS_START__: bool
__FILE_PATH__: str = ''
__ALLOW_TRACKING__: bool
__KEEP_PERF_DATA__: bool
__BINARY_FILE_EXT__: str
__LINES__: list[str] = []
__NO_VERSION_CHECK__: bool
__TRANSPILE_FILE_EXT__: str
__STATIC_FOR_CALLS__: int = 0
__FINAL_LIST__: list[str] = []
__INDENTATION_LEVEL__: int = 0
__INDENTATION_COUNT__: int = 0
__SPLIT_LIST__: list[list] = []
__CLASSES__: dict[str, dict] = {}
__IN_STATIC_FOR__: list[bool] = []
__ALWAYS_MONITOR_PERF_DATA__: bool
__EXTRA_INDENTATION__: bool = False
__PUBLIC_INIT_FOUND__: bool = False
__VARIABLES__: dict[str, dict] = {}
__FUNCTIONS__: dict[str, dict] = {}
__STATIC_FOR_LINE__: list[str] = []
__PRE_SPLIT_LIST__: list[list] = []
__OVERLOAD_FUNCTION_REG__: dict = {}
__PUBLIC_CLOSE_FOUND__: bool = False
__PUBLIC_UPDATE_FOUND__: bool = False
__IN_INTREPRETED_MODE__: bool = False
__COLOR_SUPPORT__ = sys.stdout.isatty()
__LINES_FROM_FILE_RAW__: list[str] = []
__ERROR_REPORTING_CALLED__: bool = False
__OPTIANAL_ARGS_IN_FILE__: list[str] = []
__CURRENT_YEAR__: int = int(strftime("%Y"))
__TERMINAL_WIDTH__: int = os.get_terminal_size().columns
__COLORS__: MappingProxyType[str, str] = _MAP_(
    {
        'bold red' : '\033[1;31m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'bold green' : '\033[1;32m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'bold yellow' : '\033[1;33m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'bold blue' : '\033[1;34m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'bold magenta' : '\033[1;35m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'bold cyan' : '\033[1;36m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'bold white' : '\033[1;37m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',

        'red' : '\033[91m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'green' : '\033[92m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'yellow' : '\033[93m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'blue' : '\033[94m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'magenta' : '\033[95m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'cyan' : '\033[96m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'white' : '\033[97m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',

        'underline' : '\033[4m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'italic' : '\033[3m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'blink' : '\033[5m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'reverse' : '\033[7m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        'reset' : '\033[0m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
    }
) if __COLOR_SUPPORT__ else _MAP_({'red' : '', 'green' : '', 'yellow' : '', 'blue' : '', 'magenta' : '', 'cyan' : '', 'white' : '', 'bold red' : '', 'bold green' : '', 'bold yellow' : '', 'bold blue' : '', 'bold magenta' : '', 'bold cyan' : '', 'bold white' : '', 'bright_red' : '', 'bright_green' : '', 'bright_yellow' : '', 'bright_blue' : '', 'bright_magenta' : '', 'bright_cyan' : '', 'bright_white' : '', 'underline' : '', 'italic' : '', 'blink' : '', 'reverse' : '', 'reset' : ''})

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
    DATA  = f"# -*- coding: utf-8 -*-\n"
    DATA += f"# THIS FILE WAS GENERATED BY VERSACE {__VERSION__}\n"
    DATA += f"# Versace can be found here: \"https://github.com/Ze7111/Verscae-Programing-language/\"\n"
    DATA += f"# Versace Documentation can be found here: \"https://dhruvan.gitbook.io/vs/\"\n"
    DATA += f"\"\"\"\n"
    DATA += f"╭───────────────────────────────────────────────────────────────────────────────╮\n"
    DATA += f"│    DO NOT EDIT THIS CODE THIS SECTION OF CODE OR THE LINES ABOVE THIS,        │\n"
    DATA += f"│                       AUTO GENERATED BY VERSACE.                              │\n"
    DATA += f"╰───────────────────────────────────────────────────────────────────────────────╯\n"
    DATA += f"\"\"\"\n"
    DATA += f"from rich import console; print = console.Console().print\n"
    DATA += f"from sys import exit, getsizeof\n"
    DATA += f"from copy import deepcopy as copy\n"
    DATA += f"import sys, os\n"
    DATA += f"from threading import Thread, main_thread\n"
    DATA += f"from time import sleep as wait\n"
    DATA += f"from dataclasses import dataclass\n"
    DATA += f"from subprocess import Popen as ppopen\n"
    DATA += f"from typing import Final\n"
    DATA += f"from psutil import virtual_memory\n"
    DATA += f"__ALLOCATED_MEMORY_ARRAY__: list[int] = []\n"
    DATA += f"__FREE_MEMORY__: int = (virtual_memory().free / (1024 * 1024)) - 1024\n"
    DATA += f"__TASK_REGISTRY__: dict[str, object] = {{}}\n"
    DATA += f"__TASK_ARGS_REGISTRY__: dict[str, tuple] = {{}}\n"
    DATA += f"__TASK_KWARGS_REGISTRY__: dict[str, dict] = {{}}\n"
    DATA += f"__AUTO_RELEASE_POOL__: bool = False\n"
    DATA += f"_FROZENSET_ = frozenset\n"
    DATA += f"__OVERLOAD_FUNCTION_REG__: dict = {{}}\n"
    DATA += f"class VersaceCodeBaseError(Exception):\n"
    DATA += f"{__INDENTATION__*1}def __init__(self, message):\n"
    DATA += f"{__INDENTATION__*2}os.system("")\n"
    DATA += f"{__INDENTATION__*2}print(\"\\033[1;31mVersaceError: \" + message + \"\\033[0m\")\n"
    DATA += f"{__INDENTATION__*2}exit()\n"
    DATA += f"class __DISPATCH__(object):\n"
    DATA += f"{__INDENTATION__*1}def __init__(self, NAME):\n"
    DATA += f"{__INDENTATION__*2}self.NAME = NAME\n"
    DATA += f"{__INDENTATION__*2}self.__TYPE_MAP__ = {{}}\n"
    DATA += f"{__INDENTATION__*1}def __call__(self, *ARGUMENTS):\n"
    DATA += f"{__INDENTATION__*2}__TYPES__ = tuple(argument.__class__ for argument in ARGUMENTS) # a generator expression!\n"
    DATA += f"{__INDENTATION__*2}FUNCTION = self.__TYPE_MAP__.get(__TYPES__)\n"
    DATA += f"{__INDENTATION__*2}if FUNCTION is None:\n"
    DATA += f"{__INDENTATION__*3}VersaceCodeBaseError(f\"No registered function for types \\\"{{__TYPES__}}\\\"\")\n"
    DATA += f"{__INDENTATION__*2}return FUNCTION(*ARGUMENTS)\n"
    DATA += f"{__INDENTATION__*1}def __register__(self, __TYPES__, FUNCTION):\n"
    DATA += f"{__INDENTATION__*2}if __TYPES__ in self.__TYPE_MAP__:\n"
    DATA += f"{__INDENTATION__*3}VersaceCodeBaseError(f\"Duplicate registration for function \\\"{{FUNCTION.__name__}}\\\"\")\n"
    DATA += f"{__INDENTATION__*2}self.__TYPE_MAP__[__TYPES__] = FUNCTION\n"
    DATA += f"def overload(*__TYPES__):\n"
    DATA += f"{__INDENTATION__*1}def __register__(FUNCTION):\n"
    DATA += f"{__INDENTATION__*2}NAME = FUNCTION.__name__\n"
    DATA += f"{__INDENTATION__*2}__D_INST__ = __OVERLOAD_FUNCTION_REG__.get(NAME)\n"
    DATA += f"{__INDENTATION__*2}if __D_INST__ is None:\n"
    DATA += f"{__INDENTATION__*3}__D_INST__ = __OVERLOAD_FUNCTION_REG__[NAME] = __DISPATCH__(NAME)\n"
    DATA += f"{__INDENTATION__*2}__D_INST__.__register__(__TYPES__, FUNCTION)\n"
    DATA += f"{__INDENTATION__*2}return __D_INST__\n"
    DATA += f"{__INDENTATION__*1}return __register__\n"
    DATA += f"def _async(func):\n"
    DATA += f"{__INDENTATION__*1}\"\"\" This is a decorator for async functions \"\"\"\n"
    DATA += f"{__INDENTATION__*1}def __ASYNC__FUNCTION__(*args, **kwargs):\n"
    DATA += f"{__INDENTATION__*2}\"\"\" This is the wrapper function that will be returned \"\"\"\n"
    DATA += f"{__INDENTATION__*2}thread = Thread(target=func, args=args, kwargs=kwargs)\n"
    DATA += f"{__INDENTATION__*2}thread.start()\n"
    DATA += f"{__INDENTATION__*2}return thread\n"
    DATA += f"{__INDENTATION__*1}return __ASYNC__FUNCTION__\n"
    DATA += f"with open(__file__, \'r\') as f:\n"
    DATA += f"{__INDENTATION__*1}__THIS_FILE_DATA__ = f.readlines()\n"
    DATA += f"if \'Versace\' not in __THIS_FILE_DATA__[2]:\n"
    DATA += f"{__INDENTATION__*1}raise RuntimeError('This file is corrupted, please do not modify the section of code that specifies that it is auto generated by Versace')\n"
    DATA += f"if \'https\' not in __THIS_FILE_DATA__[2]:\n"
    DATA += f"{__INDENTATION__*1}raise RuntimeError('This file is corrupted, please do not modify the section of code that specifies that it is auto generated by Versace')\n"
    DATA += f"if \'Ze7111\' not in __THIS_FILE_DATA__[2]:\n"
    DATA += f"{__INDENTATION__*1}raise RuntimeError('This file is corrupted, please do not modify the section of code that specifies that it is auto generated by Versace')\n"
    DATA += f"if \'GENERATED\' not in __THIS_FILE_DATA__[1]:\n"
    DATA += f"{__INDENTATION__*1}raise RuntimeError('This file is corrupted, please do not modify the section of code that specifies that it is auto generated by Versace')\n"
    DATA += f"if \'coding\' not in __THIS_FILE_DATA__[0]:\n"
    DATA += f"{__INDENTATION__*1}raise UnicodeError(\'This file is corrupted, please do not modify the section of code that specifies that it is auto generated by Versace\')\n"
    DATA += f"def pack(*args, **kwargs) -> tuple:\n"
    DATA += f"{__INDENTATION__*1}\"\"\" Packs any given data into a tuple \"\"\"\n"
    DATA += f"{__INDENTATION__*1}if not args and not kwargs:\n"
    DATA += f"{__INDENTATION__*2}return (None)\n"
    DATA += f"{__INDENTATION__*1}if not args:\n"
    DATA += f"{__INDENTATION__*2}return kwargs\n"
    DATA += f"{__INDENTATION__*1}if not kwargs:\n"
    DATA += f"{__INDENTATION__*2}return args\n"
    DATA += f"{__INDENTATION__*1}return args, kwargs\n"
    DATA += f"def unpack(args, **kwargs) -> ...:\n"
    DATA += f"{__INDENTATION__*1}\"\"\" Unpacks any packed data, so they can be assigned to variables \"\"\"\n"
    DATA += f"{__INDENTATION__*1}if not args and not kwargs:\n"
    DATA += f"{__INDENTATION__*2}return (None)\n"
    DATA += f"{__INDENTATION__*1}if not args:\n"
    DATA += f"{__INDENTATION__*2}return kwargs\n"
    DATA += f"{__INDENTATION__*1}if not kwargs:\n"
    DATA += f"{__INDENTATION__*2}return args\n"
    DATA += f"{__INDENTATION__*1}return args, kwargs\n"
    DATA += f"def frozenset(*args, **kwargs) -> _FROZENSET_:\n"
    DATA += f"{__INDENTATION__*1}\"\"\" Converts any given data to a frozenset \"\"\"\n"
    DATA += f"{__INDENTATION__*1}return __builtins__.frozenset(args)\n"
    DATA += f"def exec(*args, **kwargs) -> None:\n"
    DATA += f"{__INDENTATION__*1}\"\"\" Executes any given code \"\"\"\n"
    DATA += f"{__INDENTATION__*1}if not args and not kwargs:\n"
    DATA += f"{__INDENTATION__*2}return (None)\n"
    DATA += f"{__INDENTATION__*1}for i in args:\n"
    DATA += f"{__INDENTATION__*2}exec(i, globals())\n"
    DATA += f"def alloc(size=None, output=None, sep=None) -> int | str:\n"
    DATA += f"{__INDENTATION__*1}__ALLOCATE__ = size\n"
    DATA += f"{__INDENTATION__*1}if __ALLOCATE__ is None: raise ValueError(\'No ammout of memory provided to allocate\')\n"
    DATA += f"{__INDENTATION__*1}if sep is None: sep = \',\'\n"
    DATA += f"{__INDENTATION__*1}global __ALLOCATED_MEMORY_ARRAY__, __FREE_MEMORY__\n"
    DATA += f"{__INDENTATION__*1}if __ALLOCATE__ > __FREE_MEMORY__: raise MemoryError(f\'Not enough memory to allocate {{__ALLOCATE__:,}} MB, only {{int(__FREE_MEMORY__):,}} MB available\')\n"
    DATA += f"{__INDENTATION__*1}if type(__ALLOCATE__) is not int: raise TypeError(\'Ammout of memory to allocate must be an integer\')\n"
    DATA += f"{__INDENTATION__*1}if type(__ALLOCATED_MEMORY_ARRAY__) is not list: __ALLOCATED_MEMORY_ARRAY__ = []\n"
    DATA += f"{__INDENTATION__*1}__ALLOCATE__ = __ALLOCATE__ * 7710 * 17\n"
    DATA += f"{__INDENTATION__*1}__ALLOCATED_MEMORY_ARRAY__  = [0] * __ALLOCATE__\n"
    DATA += f"{__INDENTATION__*1}if output is None: return getsizeof(__ALLOCATED_MEMORY_ARRAY__)\n"
    DATA += f"{__INDENTATION__*1}elif output == str: \n"
    DATA += f"{__INDENTATION__*2}__ALLOCATE__ = getsizeof(__ALLOCATED_MEMORY_ARRAY__)\n"
    DATA += f"{__INDENTATION__*2}if __ALLOCATE__ > 1024 * 1024 * 1024 * 1024:\n"
    DATA += f"{__INDENTATION__*3}__ALLOCATE__ = __ALLOCATE__ / (1024 * 1024 * 1024 * 1024)\n"
    DATA += f"{__INDENTATION__*3}__ALLOCATE__ = round(__ALLOCATE__, 2)\n"
    DATA += f"{__INDENTATION__*3}return f\'{{__ALLOCATE__:{{sep}}}} TB\'\n"
    DATA += f"{__INDENTATION__*2}elif __ALLOCATE__ > 1024 * 1024 * 1024:\n"
    DATA += f"{__INDENTATION__*3}__ALLOCATE__ = __ALLOCATE__ / (1024 * 1024 * 1024)\n"
    DATA += f"{__INDENTATION__*3}__ALLOCATE__ = round(__ALLOCATE__, 2)\n"
    DATA += f"{__INDENTATION__*3}return f\'{{__ALLOCATE__:{{sep}}}} GB\'\n"
    DATA += f"{__INDENTATION__*2}elif __ALLOCATE__ > 1024 * 1024:\n"
    DATA += f"{__INDENTATION__*3}__ALLOCATE__ = __ALLOCATE__ / (1024 * 1024)\n"
    DATA += f"{__INDENTATION__*3}__ALLOCATE__ = round(__ALLOCATE__, 2)\n"
    DATA += f"{__INDENTATION__*3}return f\'{{__ALLOCATE__:{{sep}}}} MB\'\n"
    DATA += f"{__INDENTATION__*2}elif __ALLOCATE__ > 1024:\n"
    DATA += f"{__INDENTATION__*3}__ALLOCATE__ = __ALLOCATE__ / 1024\n"
    DATA += f"{__INDENTATION__*3}__ALLOCATE__ = round(__ALLOCATE__, 2)\n"
    DATA += f"{__INDENTATION__*3}return f\'{{__ALLOCATE__:{{sep}}}} KB\'\n"
    DATA += f"{__INDENTATION__*2}else:\n"
    DATA += f"{__INDENTATION__*3}__ALLOCATE__ = round(__ALLOCATE__, 2)\n"
    DATA += f"{__INDENTATION__*3}return f\'{{__ALLOCATE__:{{sep}}}} Bytes\'\n"
    DATA += f"{__INDENTATION__*1}elif output == list:\n"
    DATA += f"{__INDENTATION__*2}# raise a exception informing the use THAT THEY ARE NOT SUPPOSED TO USE THIS FUNCTION\n"
    DATA += f"{__INDENTATION__*2}raise NotImplementedError(\'Using this WILL cause memory leaks, DO NOT USE\')\n"
    DATA += f"{__INDENTATION__*1}elif output == int:\n"
    DATA += f"{__INDENTATION__*2}return getsizeof(__ALLOCATED_MEMORY_ARRAY__)\n"
    DATA += f"{__INDENTATION__*1}else:\n"
    DATA += f"{__INDENTATION__*2}raise TypeError(\'Invalid output type\')\n"
    DATA += f"def dealloc(size=None, output=None, sep=None) -> int | str:\n"
    DATA += f"{__INDENTATION__*1}__DEALLOCATE__ = size\n"
    DATA += f"{__INDENTATION__*1}global __ALLOCATED_MEMORY_ARRAY__, __FREE_MEMORY__\n"
    DATA += f"{__INDENTATION__*1}if sep is None: sep = \',\'\n"
    DATA += f"{__INDENTATION__*1}__DEALLOCATE__ = (__DEALLOCATE__ * 7710 * 17) if __DEALLOCATE__ is not None else None\n"
    DATA += f"{__INDENTATION__*1}if __DEALLOCATE__ is None: __DEALLOCATE__ = len(__ALLOCATED_MEMORY_ARRAY__)\n"
    DATA += f"{__INDENTATION__*1}if __DEALLOCATE__ / 7710 / 17 > __FREE_MEMORY__: raise MemoryError(f\'Not enough memory to deallocate {{__DEALLOCATE__:,}} MB, only {{int(__FREE_MEMORY__):,}} MB available\')\n"
    DATA += f"{__INDENTATION__*1}if type(__ALLOCATED_MEMORY_ARRAY__) is not list: raise ValueError(\'Memory is not allocated\')\n"
    DATA += f"{__INDENTATION__*1}if __DEALLOCATE__ > len(__ALLOCATED_MEMORY_ARRAY__): raise MemoryError(f\'Not enough memory allocated to deallocate, only {{len(__ALLOCATED_MEMORY_ARRAY__):,}} MB allocated\')\n"
    DATA += f"{__INDENTATION__*1}__ALLOCATED_MEMORY_ARRAY__ = __ALLOCATED_MEMORY_ARRAY__[:__DEALLOCATE__]\n"
    DATA += f"{__INDENTATION__*1}ammout_of_memory_allocated = getsizeof(__ALLOCATED_MEMORY_ARRAY__)\n"
    DATA += f"{__INDENTATION__*1}if ammout_of_memory_allocated == 56: ammout_of_memory_allocated = 0\n"
    DATA += f"{__INDENTATION__*1}if output is None: \n"
    DATA += f"{__INDENTATION__*2}return ammout_of_memory_allocated\n"
    DATA += f"{__INDENTATION__*1}elif output == str: \n"
    DATA += f"{__INDENTATION__*2}__DEALLOCATE__ = ammout_of_memory_allocated\n"
    DATA += f"{__INDENTATION__*2}if __DEALLOCATE__ > 1024 * 1024 * 1024 * 1024:\n"
    DATA += f"{__INDENTATION__*3}__DEALLOCATE__ = __DEALLOCATE__ / (1024 * 1024 * 1024 * 1024)\n"
    DATA += f"{__INDENTATION__*3}__DEALLOCATE__ = round(__DEALLOCATE__, 2)\n"
    DATA += f"{__INDENTATION__*3}return f\'{{__DEALLOCATE__:{{sep}}}} TB\'\n"
    DATA += f"{__INDENTATION__*2}elif __DEALLOCATE__ > 1024 * 1024 * 1024:\n"
    DATA += f"{__INDENTATION__*3}__DEALLOCATE__ = __DEALLOCATE__ / (1024 * 1024 * 1024)\n"
    DATA += f"{__INDENTATION__*3}__DEALLOCATE__ = round(__DEALLOCATE__, 2)\n"
    DATA += f"{__INDENTATION__*3}return f\'{{__DEALLOCATE__:{{sep}}}} GB\'\n"
    DATA += f"{__INDENTATION__*2}elif __DEALLOCATE__ > 1024 * 1024:\n"
    DATA += f"{__INDENTATION__*3}__DEALLOCATE__ = __DEALLOCATE__ = __DEALLOCATE__ / (1024 * 1024)\n"
    DATA += f"{__INDENTATION__*3}__DEALLOCATE__ = round(__DEALLOCATE__, 2)\n"
    DATA += f"{__INDENTATION__*3}return f\'{{__DEALLOCATE__:{{sep}}}} MB\'\n"
    DATA += f"{__INDENTATION__*2}elif __DEALLOCATE__ > 1024:\n"
    DATA += f"{__INDENTATION__*3}__DEALLOCATE__ = __DEALLOCATE__ / 1024\n"
    DATA += f"{__INDENTATION__*3}__DEALLOCATE__ = round(__DEALLOCATE__, 2)\n"
    DATA += f"{__INDENTATION__*3}return f\'{{__DEALLOCATE__:{{sep}}}} KB\'\n"
    DATA += f"{__INDENTATION__*2}else:\n"
    DATA += f"{__INDENTATION__*3}__DEALLOCATE__ = round(__DEALLOCATE__, 2)\n"
    DATA += f"{__INDENTATION__*3}return f\'{{__DEALLOCATE__:{{sep}}}} Bytes\'\n"
    DATA += f"{__INDENTATION__*1}elif output == list:\n"
    DATA += f"{__INDENTATION__*2}# raise a exception informing the use THAT THEY ARE NOT SUPPOSED TO USE THIS FUNCTION\n"
    DATA += f"{__INDENTATION__*2}raise NotImplementedError(\'Using this WILL cause memory leaks, DO NOT USE\')\n"
    DATA += f"{__INDENTATION__*1}elif output == int:\n"
    DATA += f"{__INDENTATION__*2}return ammout_of_memory_allocated\n"
    DATA += f"{__INDENTATION__*1}else:\n"
    DATA += f"{__INDENTATION__*2}raise TypeError(\'Invalid output type\')\n"
    DATA += f"def latch(*args, **kwrgs):\n"
    DATA += f"{__INDENTATION__*1}if len(args) == 0 and len(kwrgs) == 0:\n"
    DATA += f"{__INDENTATION__*2}raise RuntimeError(\'No arguments passed to latch\')\n"
    DATA += f"{__INDENTATION__*1}for arg in args:\n"
    DATA += f"{__INDENTATION__*2}if isinstance(arg, bool) != True:\n"
    DATA += f"{__INDENTATION__*3}raise RuntimeError(f\'Invalid argument type passed to latch, expected bool, got {{type(arg)}}\')\n"
    DATA += f"{__INDENTATION__*1}for kwarg in kwrgs:\n"
    DATA += f"{__INDENTATION__*2}if isinstance(kwrgs.get(kwarg), bool) != True:\n"
    DATA += f"{__INDENTATION__*3}raise RuntimeError(f\'Invalid argument type passed to latch, expected bool, got {{type(kwrgs.get(kwarg))}}\')\n"
    DATA += f"{__INDENTATION__*1}if len(args) > 0:\n"
    DATA += f"{__INDENTATION__*2}args = list(args)\n"
    DATA += f"{__INDENTATION__*2}for index in range(len(args)):\n"
    DATA += f"{__INDENTATION__*3}args[index] = not args[index]\n"
    DATA += f"{__INDENTATION__*2}args = tuple(args)\n"
    DATA += f"{__INDENTATION__*1}if len(kwrgs) > 0:\n"
    DATA += f"{__INDENTATION__*2}kwrgs = dict(kwrgs)\n"
    DATA += f"{__INDENTATION__*2}for kwarg in kwrgs:\n"
    DATA += f"{__INDENTATION__*3}kwrgs[kwarg] = not kwrgs.get(kwarg)\n"
    DATA += f"{__INDENTATION__*2}kwrgs = dict(kwrgs)\n"
    DATA += f"{__INDENTATION__*1}if len(args) > 0 and len(kwrgs) > 0:\n"
    DATA += f"{__INDENTATION__*2}temp_arg_list = []\n"
    DATA += f"{__INDENTATION__*2}temp_kwarg_list = []\n"
    DATA += f"{__INDENTATION__*2}for arg in args:\n"
    DATA += f"{__INDENTATION__*3}temp_arg_list.append(arg)\n"
    DATA += f"{__INDENTATION__*2}for kwarg in kwrgs:\n"
    DATA += f"{__INDENTATION__*3}temp_kwarg_list.append(kwrgs.get(kwarg))\n"
    DATA += f"{__INDENTATION__*2}args = tuple(temp_arg_list)\n"
    DATA += f"{__INDENTATION__*2}kwrgs = tuple(temp_kwarg_list)\n"
    DATA += f"{__INDENTATION__*2}return *args, *kwrgs\n"
    DATA += f"{__INDENTATION__*1}elif len(args) == 1:\n"
    DATA += f"{__INDENTATION__*2}return args[0]\n"
    DATA += f"{__INDENTATION__*1}elif len(kwrgs) == 1:\n"
    DATA += f"{__INDENTATION__*2}return kwrgs.get(list(kwrgs)[0])\n"
    DATA += f"{__INDENTATION__*1}elif len(args) > 0:\n"
    DATA += f"{__INDENTATION__*2}return args\n"
    DATA += f"{__INDENTATION__*1}elif len(kwrgs) > 0:\n"
    DATA += f"{__INDENTATION__*2}templist = []\n"
    DATA += f"{__INDENTATION__*2}for value in kwrgs:\n"
    DATA += f"{__INDENTATION__*3}templist.append(kwrgs.get(value))\n"
    DATA += f"{__INDENTATION__*2}templist = tuple(templist)\n"
    DATA += f"{__INDENTATION__*2}return templist\n"
    DATA += f"{__INDENTATION__*1}\n"
    DATA += f"{__INDENTATION__*2}\n"
    DATA += f"class VariableError(Exception):\n"
    DATA += f"{__INDENTATION__*1}def __init__(self, *args, **kwargs):\n"
    DATA += f"{__INDENTATION__*2}if args:\n"
    DATA += f"{__INDENTATION__*3}print(f\"VariableError: {{args[0]}}\")\n"
    DATA += f"{__INDENTATION__*2}elif kwargs:\n"
    DATA += f"{__INDENTATION__*3}print(f\"VariableError: {{kwargs[0]}}\")\n"
    DATA += f"{__INDENTATION__*2}exit()\n"
    DATA += f"class SyntaxError(Exception):\n"
    DATA += f"{__INDENTATION__*1}def __init__(self, *args, **kwargs):\n"
    DATA += f"{__INDENTATION__*2}if args:\n"
    DATA += f"{__INDENTATION__*3}print(f\"SyntaxError: {{args[0]}}\")\n"
    DATA += f"{__INDENTATION__*2}elif kwargs:\n"
    DATA += f"{__INDENTATION__*3}print(f\"SyntaxError: {{kwargs[0]}}\")\n"
    DATA += f"{__INDENTATION__*2}exit()\n"
    DATA += f"class CloseError(Exception):\n"
    DATA += f"{__INDENTATION__*1}def __init__(self, *args, **kwargs):\n"
    DATA += f"{__INDENTATION__*2}if args:\n"
    DATA += f"{__INDENTATION__*3}print(f\"CloseError: {{args[0]}}\")\n"
    DATA += f"{__INDENTATION__*2}elif kwargs:\n"
    DATA += f"{__INDENTATION__*3}print(f\"CloseError: {{kwargs[0]}}\")\n"
    DATA += f"{__INDENTATION__*2}exit()\n"
    DATA += f"class TypeError(Exception):\n"
    DATA += f"{__INDENTATION__*1}def __init__(self, *args, **kwargs):\n"
    DATA += f"{__INDENTATION__*2}if args:\n"
    DATA += f"{__INDENTATION__*3}print(f\"TypeError: {{args[0]}}\")\n"
    DATA += f"{__INDENTATION__*2}elif kwargs:\n"
    DATA += f"{__INDENTATION__*3}print(f\"TypeError: {{kwargs[0]}}\")\n"
    DATA += f"{__INDENTATION__*2}exit()\n"
    DATA += f"class DataError(Exception):\n"
    DATA += f"{__INDENTATION__*1}def __init__(self, *args, **kwargs):\n"
    DATA += f"{__INDENTATION__*2}if args:\n"
    DATA += f"{__INDENTATION__*3}print(f\"DataError: {{args[0]}}\")\n"
    DATA += f"{__INDENTATION__*2}elif kwargs:\n"
    DATA += f"{__INDENTATION__*3}print(f\"DataError: {{kwargs[0]}}\")\n"
    DATA += f"{__INDENTATION__*2}exit()\n"
    DATA += f"class FileNotFoundError(Exception):\n"
    DATA += f"{__INDENTATION__*1}def __init__(self, *args, **kwargs):\n"
    DATA += f"{__INDENTATION__*2}if args:\n"
    DATA += f"{__INDENTATION__*3}print(f\"FileNotFoundError: {{args[0]}}\")\n"
    DATA += f"{__INDENTATION__*2}elif kwargs:\n"
    DATA += f"{__INDENTATION__*3}print(f\"FileNotFoundError: {{kwargs[0]}}\")\n"
    DATA += f"{__INDENTATION__*2}exit()\n"
    DATA += f"class RefrenceError(Exception):\n"
    DATA += f"{__INDENTATION__*1}def __init__(self, *args, **kwargs):\n"
    DATA += f"{__INDENTATION__*2}if args:\n"
    DATA += f"{__INDENTATION__*3}print(f\"RefrenceError: {{args[0]}}\")\n"
    DATA += f"{__INDENTATION__*2}elif kwargs:\n"
    DATA += f"{__INDENTATION__*3}print(f\"RefrenceError: {{kwargs[0]}}\")\n"
    DATA += f"{__INDENTATION__*2}exit()\n"
    DATA += f"class NoInitError(Exception):\n"
    DATA += f"{__INDENTATION__*1}def __init__(self, *args, **kwargs):\n"
    DATA += f"{__INDENTATION__*2}if args:\n"
    DATA += f"{__INDENTATION__*3}print(f\"NoInitError: {{args[0]}}\")\n"
    DATA += f"{__INDENTATION__*2}elif kwargs:\n"
    DATA += f"{__INDENTATION__*3}print(f\"NoInitError: {{kwargs[0]}}\")\n"
    DATA += f"{__INDENTATION__*2}exit()\n"
    DATA += f"class Error(Exception):\n"
    DATA += f"{__INDENTATION__*1}def __init__(self, *args, **kwargs):\n"
    DATA += f"{__INDENTATION__*2}if args:\n"
    DATA += f"{__INDENTATION__*3}print(f\"Error: {{args[0]}}\")\n"
    DATA += f"{__INDENTATION__*2}elif kwargs:\n"
    DATA += f"{__INDENTATION__*3}print(f\"Error: {{kwargs[0]}}\")\n"
    DATA += f"{__INDENTATION__*2}exit()\n"
    DATA += f"class AsyncError(Exception):\n"
    DATA += f"{__INDENTATION__*1}def __init__(self, *args, **kwargs):\n"
    DATA += f"{__INDENTATION__*2}if args:\n"
    DATA += f"{__INDENTATION__*3}print(f\"AsyncError: {{args[0]}}\")\n"
    DATA += f"{__INDENTATION__*2}elif kwargs:\n"
    DATA += f"{__INDENTATION__*3}print(f\"AsyncError: {{kwargs[0]}}\")\n"
    DATA += f"{__INDENTATION__*2}exit()\n"
    DATA += f"class RuntimeError(Exception):\n"
    DATA += f"{__INDENTATION__*1}def __init__(self, *args, **kwargs):\n"
    DATA += f"{__INDENTATION__*2}if args:\n"
    DATA += f"{__INDENTATION__*3}print(f\"RuntimeError: {{args[0]}}\")\n"
    DATA += f"{__INDENTATION__*2}elif kwargs:\n"
    DATA += f"{__INDENTATION__*3}print(f\"RuntimeError: {{kwargs[0]}}\")\n"
    DATA += f"{__INDENTATION__*2}exit()\n"
    DATA += f"class TaskGroup:\n"
    DATA += f"{__INDENTATION__*1}def autorelease_pool(value: bool):\n"
    DATA += f"{__INDENTATION__*2}global __TASK_REGISTRY__, __TASK_ARGS_REGISTRY__, __TASK_KWARGS_REGISTRY__, __AUTO_RELEASE_POOL__\n"
    DATA += f"{__INDENTATION__*2}if len(__TASK_REGISTRY__) == 0:\n"
    DATA += f"{__INDENTATION__*3}__AUTO_RELEASE_POOL__ = value\n"
    DATA += f"{__INDENTATION__*2}else:\n"
    DATA += f"{__INDENTATION__*3}if value != __AUTO_RELEASE_POOL__:\n"
    DATA += f"{__INDENTATION__*4}raise RuntimeError(\'Cannot modify autorelease pool while tasks are set, clear tasks first with \"dyn clear();\"\')\n"
    DATA += f"{__INDENTATION__*1}def add(task: object, *args, **kwargs):\n"
    DATA += f"{__INDENTATION__*2}global __TASK_REGISTRY__, __TASK_ARGS_REGISTRY__, __TASK_KWARGS_REGISTRY__\n"
    DATA += f"{__INDENTATION__*2}if not callable(task):\n"
    DATA += f"{__INDENTATION__*3}raise TypeError(\'Invalid task, expected a callable object (function or method)\')\n"
    DATA += f"{__INDENTATION__*2}if task.__name__ != \"__ASYNC__FUNCTION__\":\n"
    DATA += f"{__INDENTATION__*3}raise RuntimeError(\'Invalid task, expected a async function\')\n"
    DATA += f"{__INDENTATION__*2}__TASK_REGISTRY__[task] = task.__name__\n"
    DATA += f"{__INDENTATION__*2}__TASK_ARGS_REGISTRY__[task] = args\n"
    DATA += f"{__INDENTATION__*2}__TASK_KWARGS_REGISTRY__[task] = kwargs\n"
    DATA += f"{__INDENTATION__*2}\n"
    DATA += f"{__INDENTATION__*1}def execute(*args):\n"
    DATA += f"{__INDENTATION__*2}global __TASK_REGISTRY__, __TASK_ARGS_REGISTRY__, __TASK_KWARGS_REGISTRY__, __AUTO_RELEASE_POOL__\n"
    DATA += f"{__INDENTATION__*2}if len(__TASK_REGISTRY__) == 0:\n"
    DATA += f"{__INDENTATION__*3}raise RuntimeError(\'No tasks to execute, you can add tasks with \"dyn (async_function)();\".\\nExample: \"dyn some_func();\"\')\n"
    DATA += f"{__INDENTATION__*2}if not args:\n"
    DATA += f"{__INDENTATION__*3}for task in __TASK_REGISTRY__:\n"
    DATA += f"{__INDENTATION__*4}task(*__TASK_ARGS_REGISTRY__[task], **__TASK_KWARGS_REGISTRY__[task])\n"
    DATA += f"{__INDENTATION__*2}else:\n"
    DATA += f"{__INDENTATION__*3}for task in args:\n"
    DATA += f"{__INDENTATION__*4}task(*__TASK_ARGS_REGISTRY__[task], **__TASK_KWARGS_REGISTRY__[task])\n"
    DATA += f"{__INDENTATION__*2}if __AUTO_RELEASE_POOL__ == True and len(args) == len(__TASK_REGISTRY__):\n"
    DATA += f"{__INDENTATION__*3}__TASK_REGISTRY__.clear()\n"
    DATA += f"{__INDENTATION__*3}__TASK_ARGS_REGISTRY__.clear()\n"
    DATA += f"{__INDENTATION__*3}__TASK_KWARGS_REGISTRY__.clear()\n"
    DATA += f"{__INDENTATION__*3}__AUTO_RELEASE_POOL__ = False\n"
    DATA += f"{__INDENTATION__*2}elif __AUTO_RELEASE_POOL__ == True and len(args) > 0:\n"
    DATA += f"{__INDENTATION__*3}for task in args:\n"
    DATA += f"{__INDENTATION__*4}if task not in __TASK_REGISTRY__:\n"
    DATA += f"{__INDENTATION__*4}{__INDENTATION__*1}raise RefrenceError(f\"\'{{task}}\' not found in the tasks registry.\")\n"
    DATA += f"{__INDENTATION__*4}del __TASK_REGISTRY__[task]\n"
    DATA += f"{__INDENTATION__*4}del __TASK_ARGS_REGISTRY__[task]\n"
    DATA += f"{__INDENTATION__*4}del __TASK_KWARGS_REGISTRY__[task]\n"
    DATA += f"{__INDENTATION__*2}elif __AUTO_RELEASE_POOL__ == True and len(args) == 0:\n"
    DATA += f"{__INDENTATION__*3}__TASK_REGISTRY__.clear()\n"
    DATA += f"{__INDENTATION__*3}__TASK_ARGS_REGISTRY__.clear()\n"
    DATA += f"{__INDENTATION__*3}__TASK_KWARGS_REGISTRY__.clear()\n"
    DATA += f"{__INDENTATION__*3}__AUTO_RELEASE_POOL__ = False\n"
    DATA += f"{__INDENTATION__*3}\n"
    DATA += f"{__INDENTATION__*1}def clear():\n"
    DATA += f"{__INDENTATION__*2}global __TASK_REGISTRY__, __TASK_ARGS_REGISTRY__, __TASK_KWARGS_REGISTRY__\n"
    DATA += f"{__INDENTATION__*2}__TASK_REGISTRY__.clear()\n"
    DATA += f"{__INDENTATION__*2}__TASK_ARGS_REGISTRY__.clear()\n"
    DATA += f"{__INDENTATION__*2}__TASK_KWARGS_REGISTRY__.clear() \n"
    DATA += f"{__INDENTATION__*2}\n"
    DATA += f"{__INDENTATION__*1}def remove(*args):\n"
    DATA += f"{__INDENTATION__*2}global __TASK_REGISTRY__, __TASK_ARGS_REGISTRY__, __TASK_KWARGS_REGISTRY__\n"
    DATA += f"{__INDENTATION__*2}if not args:\n"
    DATA += f"{__INDENTATION__*3}raise SyntaxError(\'No arguments provided for \"dyn remove();\", expected at least 1\\nIf you want to remove all tasks, use \"dyn clear();\"\')\n"
    DATA += f"{__INDENTATION__*2}for task in args:\n"
    DATA += f"{__INDENTATION__*3}if task not in __TASK_REGISTRY__:\n"
    DATA += f"{__INDENTATION__*4}raise RefrenceError(f\"\'{{task}}\' not found in the tasks registry.\")\n"
    DATA += f"{__INDENTATION__*3}del __TASK_REGISTRY__[task]\n"
    DATA += f"{__INDENTATION__*3}del __TASK_ARGS_REGISTRY__[task]\n"
    DATA += f"{__INDENTATION__*3}del __TASK_KWARGS_REGISTRY__[task]\n"
    DATA += f"\"\"\"\n"
    DATA += f"╭──────────────────────────────────────────────────────────────────────────────────╮\n"
    DATA += f"│ YOU CAN MODIFY THE CODE BELOW THIS LINE - DO NOT MODIFY THE CODE ABOVE THIS LINE │\n"
    DATA += f"╰──────────────────────────────────────────────────────────────────────────────────╯\n"
    DATA += f"\"\"\"\n"
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
    __CONFIG_DATA__ = f"""# {'-' * len(f"This is the config file for Versace it was auto generated at {__CURRENT_TIME__}")} #
# This is the config file for Versace it was auto generated at {__CURRENT_TIME__} #
# {'-' * len(f"This is the config file for Versace it was auto generated at {__CURRENT_TIME__}")} #

["BASIC-INFORMATION"]
version = "{__VERSION__}"{' ' * (64 - len(f'version = "{__VERSION__}"'))}# the version of Versace
indentation = "    "                                            # 4 spaces is the default
allow_tracking = True                                           # This is to allow tracking of Versace
allow_update = False                                            # This is to allow updates of Versace

["PATHS"]
python_path = "{sys.executable}"{' ' * (62 - len(f'python_path = "{sys.executable}"'))}# This is the path to the python interpreter
versace_path = "{os.path.expanduser('~') + os.sep + 'Versace'}"{' ' * (61 - len(f"versace_path = '{os.path.expanduser('~') + os.sep + 'Versace'}'"))}# This is the path to the Versace folder

["COMPILER"]
no_includes = False                                             # This determines if the Versace compiler should include the modules specified by the user in thier Versace code
no_args_start = False                                           # This determines if the Versace compiler should start the Versace code with the args passed to the Versace compiler
no_version_check = False                                        # This determines if the Versace compiler should check for updates

["EXECUTABLE"]
binary_file_ext = ".exe"                                        # The type of binary to compile to when compiling to binary
binary = 1                                                      # Optimization level when compiling 0 = low_optimization(onfile), 1 = medium_optimization(ondir), 2 = max_optimization(nested_dirs)

["EXTRA"]
keep_perf_data = False                                          # This determines if the Versace compiler should keep the performance data
always_monitor_perf_data = False                                # This determines if the Versace compiler should always show the performance data
transpile_file_ext = ".py"                                      # The type of file to transpile to when compiling to python
use_cache = False                                               # This determines if the Versace compiler should use the cache"""
    if '\\' in __CONFIG_DATA__:
        __CONFIG_DATA__ = __CONFIG_DATA__.replace('\\', '\\\\')
    return __CONFIG_DATA__
@overload
def __INITIALIZE__():
    """
    \n Inputs: None
    \n Outputs: None
    \n This is the first stage of the Versace compiler.
    \n This stage is used to get the config data and the Versace code.
    \n It also checks if the required modules are installed. and saves that information to a .pkg file.
    """
    if os.path.exists(os.path.expanduser('~') + os.sep + 'Versace' + os.sep + 'base' + os.sep + 'packages.pkg') is False:
        from pkg_resources import working_set
        console("")
        __REQUIRED_MODULES__ = {'psutil', 'rich', 'requests' , 'pyinstaller', 'sv-ttk'}
        __INSTALLED_MODULES__ = {pkg.key for pkg in working_set}
        __MISSING_MODULES__ = __REQUIRED_MODULES__ - __INSTALLED_MODULES__

        if __MISSING_MODULES__:
            __PYTHON_PATH__ = sys.executable
            check_call([__PYTHON_PATH__, '-m', 'pip', 'install', *__MISSING_MODULES__], stdout=DEVNULL)
            print(f"{__COLORS__['bold green']}Installed MISSING MODULES modules successfully{__COLORS__['reset']}")

        __REQUIRED_MODULES__ = {'cx_Freeze'}
        __INSTALLED_MODULES__ = {pkg.key for pkg in working_set}
        __MISSING_MODULES__ = __REQUIRED_MODULES__ - __INSTALLED_MODULES__

        if __MISSING_MODULES__:
            __PYTHON_PATH__ = sys.executable
            check_call([__PYTHON_PATH__, '-m', 'pip', 'install', '--pre', '--extra-index-url', 'https://marcelotduarte.github.io/packages/', 'cx_Freeze', 'cx_Logging'], stdout=DEVNULL)
            print(f"{__COLORS__['bold green']}Installed MISSING MODULES modules successfully{__COLORS__['reset']}")
    
    """
    __REQUIRED_MODULES__ = {'psutil', 'rich', 'requests' , 'pyinstaller', 'sv-ttk', 'cx_Freeze'}
    __INSTALLED_MODULES__ = {pkg.key for pkg in working_set}
    __INSTALLED_MODULES_C__ = __INSTALLED_MODULES__.copy()
    __MODULES_INSTALLED__ = __INSTALLED_MODULES__ - __REQUIRED_MODULES__
    __ALL_MODULES_INSTALLED__ = False
    for i in __MODULES_INSTALLED__:
        __INSTALLED_MODULES__.remove(i)
    """
    
    if os.path.exists(os.path.expanduser('~') + os.sep + 'Versace' + os.sep + 'base' + os.sep + 'packages.pkg'):
        if os.stat(os.path.expanduser('~') + os.sep + 'Versace' + os.sep + 'base' + os.sep + 'packages.pkg').st_size == 0:
            os.remove(os.path.expanduser('~') + os.sep + 'Versace' + os.sep + 'base' + os.sep + 'packages.pkg')
        
    """
    if os.path.exists(os.path.expanduser('~') + os.sep + 'Versace' + os.sep + 'base' + os.sep + 'packages.pkg'):
        # check if the file is empty
        with open(f"{os.path.expanduser('~')}{os.sep}Versace{os.sep}base{os.sep}packages.pkg", "r+", encoding="utf-8") as f:
            __INSTALED_MODULES_SAVED__ = eval(f.readlines()[0].strip())
            for i in __INSTALED_MODULES_SAVED__:
                if i not in __INSTALLED_MODULES_C__:
                    __ALL_MODULES_INSTALLED__ = True
            if __ALL_MODULES_INSTALLED__:
                __MISSING_MODULES__ = __REQUIRED_MODULES__ - __INSTALLED_MODULES__
                if __MISSING_MODULES__:
                    __PYTHON_PATH__ = sys.executable
                    check_call([__PYTHON_PATH__, '-m', 'pip', 'install', *__MISSING_MODULES__], stdout=DEVNULL)
                    print(f"{__COLORS__['bold green']}Installed MISSING MODULES modules successfully{__COLORS__['reset']}")
                    with open(f"{os.path.expanduser('~')}{os.sep}Versace{os.sep}base{os.sep}packages.pkg", "w+", encoding="utf-8") as f:
                        f.write(str(__INSTALLED_MODULES__))
    """
    # create a folder at os.path.expanduser('~') called Versace
    if os.path.exists(os.path.expanduser('~') + os.sep + 'Versace' + os.sep + 'base') is False:
        os.makedirs(os.path.expanduser('~') + os.sep + 'Versace', exist_ok=True)
        os.makedirs(os.path.expanduser('~') + os.sep + 'Versace' + os.sep + 'base', exist_ok=True)

    if os.path.exists(os.path.expanduser('~') + os.sep + 'Versace' + os.sep + 'base' + os.sep + 'packages.pkg') is False:
        with open(f"{os.path.expanduser('~')}{os.sep}Versace{os.sep}base{os.sep}packages.pkg", "w", encoding="utf-8") as f:
            f.write(str(__INSTALLED_MODULES__))
            f.close()

@overload
def __READ_SYS_ARGS__() -> None:
    if '-cfg' in __PASS_LIST__:
        with open(f"{os.getcwd()}{os.sep}Versace.cfg", "w", encoding="utf-8") as f:
            f.write(__CREATE_CONFIG_FILE__())
            f.close()
        console("")
        print(f"{__COLORS__['bold red']}Created config file at {__COLORS__['bold cyan']}{os.getcwd()}{os.sep}Versace.cfg{__COLORS__['reset']}")
        # execute the config file
        with open(f"{os.getcwd()}{os.sep}Versace.cfg", "r") as f:
            __CONFIG_DATA__ = f.read()
            f.close()
        __READ_CONFIG__(__CONFIG_DATA__, FILE_PATH=f"{os.getcwd()}{os.sep}Versace.cfg")
    else:
        if os.path.exists(f"{os.getcwd()}{os.sep}Versace.cfg"):
            with open(f"{os.getcwd()}{os.sep}Versace.cfg", "r") as f:
                __CONFIG_DATA__ = f.read()
                f.close()
            __READ_CONFIG__(__CONFIG_DATA__, FILE_PATH=f"{os.getcwd()}{os.sep}Versace.cfg")

        else:
            if os.path.exists(f"{os.path.expanduser('~')}{os.sep}Versace{os.sep}base{os.sep}defualt-Versace.cfg") == False:
                with open(f"{os.path.expanduser('~')}{os.sep}Versace{os.sep}base{os.sep}defualt-Versace.cfg", "w", encoding="utf-8") as f:
                    f.write(__CREATE_CONFIG_FILE__())
                    f.close()

            with open(f"{os.path.expanduser('~')}{os.sep}Versace{os.sep}base{os.sep}defualt-Versace.cfg", "r") as f:
                __CONFIG_DATA__ = f.read()
                f.close()
            __READ_CONFIG__(__CONFIG_DATA__, FILE_PATH=f"{os.path.expanduser('~')}{os.sep}Versace{os.sep}base{os.sep}defualt-Versace.cfg")
    return 0
@overload_atter
def __PACK_CONFIG__() -> dict:
    """
    \nInputs: __CONFIG_DATA__
    \nOutputs: PACK
    \nThis is used to pack all the config data into a single dictionary.
    """
    global __INDENTATION__, __ALLOW_TRACKING__, __ALLOW_UPDATE__, __PYTHON_PATH__, __VERSACE_PATH__, __NO_INCLUDES__, __NO_ARGS_START__, __NO_VERSION_CHECK__, __BINARY_FILE_EXT__, __BINARY__, __KEEP_PERF_DATA__, __ALWAYS_MONITOR_PERF_DATA__, __TRANSPILE_FILE_EXT__, __USE_CACHE__
    PACK = {}
    PACK['INDENTATION'] = __INDENTATION__
    PACK['ALLOW_TRACKING'] = __ALLOW_TRACKING__
    PACK['ALLOW_UPDATE'] = __ALLOW_UPDATE__ 
    PACK['PYTHON_PATH'] = __PYTHON_PATH__
    PACK['VERSACE_PATH'] = __VERSACE_PATH__
    PACK['NO_INCLUDES'] = __NO_INCLUDES__ 
    PACK['NO_ARGS_START'] = __NO_ARGS_START__ 
    PACK['NO_VERSION_CHECK'] = __NO_VERSION_CHECK__
    PACK['BINARY_FILE_EXT'] = __BINARY_FILE_EXT__ 
    PACK['BINARY'] = __BINARY__
    PACK['KEEP_PERF_DATA'] = __KEEP_PERF_DATA__ 
    PACK['ALWAYS_MONITOR_PERF_DATA'] = __ALWAYS_MONITOR_PERF_DATA__
    PACK['TRANSPILE_FILE_EXT'] = __TRANSPILE_FILE_EXT__
    PACK['USE_CACHE'] = __USE_CACHE__
    return PACK
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
        except Exception:
            _expectError('binary = ', int)
        try:
            __USE_CACHE__                = bool(eval(__CONFIG_DATA__.split(       'use_cache = '        )[1].split('\n')[0].split('#')[0].strip()))
        except Exception:
            _expectError('use_cache = ', bool)
        try:
            __INDENTATION__              = str (eval(__CONFIG_DATA__.split(      'indentation = '       )[1].split('\n')[0].split('#')[0].strip()))
        except Exception:
            _expectError('indentation = ', str)
        try:
            __NO_INCLUDES__              = bool(eval(__CONFIG_DATA__.split(      'no_includes = '       )[1].split('\n')[0].split('#')[0].strip()))
        except Exception:
            _expectError('no_includes = ', bool)
        try:
            __PYTHON_PATH__              = str (eval(__CONFIG_DATA__.split(      'python_path = '       )[1].split('\n')[0].split('#')[0].strip()))
        except Exception:
            _expectError('python_path = ', str)
        try:
            __ALLOW_UPDATE__             = bool(eval(__CONFIG_DATA__.split(      'allow_update = '      )[1].split('\n')[0].split('#')[0].strip()))
        except Exception:
            _expectError('allow_update = ', bool)
        try:
            __VERSACE_PATH__             = str (eval(__CONFIG_DATA__.split(      'versace_path = '      )[1].split('\n')[0].split('#')[0].strip()))
        except Exception:
            _expectError('versace_path = ', str)
        try:
            __NO_ARGS_START__            = bool(eval(__CONFIG_DATA__.split(     'no_args_start = '      )[1].split('\n')[0].split('#')[0].strip()))
        except Exception:
            _expectError('no_args_start = ', bool)
        try:
            __KEEP_PERF_DATA__           = bool(eval(__CONFIG_DATA__.split(     'keep_perf_data = '     )[1].split('\n')[0].split('#')[0].strip()))
        except Exception:
            _expectError('keep_perf_data = ', bool)
        try:
            __ALLOW_TRACKING__           = bool(eval(__CONFIG_DATA__.split(     'allow_tracking = '     )[1].split('\n')[0].split('#')[0].strip()))
        except Exception:
            _expectError('allow_tracking = ', bool)
        try:
            __BINARY_FILE_EXT__          = str (eval(__CONFIG_DATA__.split(    'binary_file_ext = '     )[1].split('\n')[0].split('#')[0].strip()))
        except Exception:
            _expectError('binary_file_ext = ', str)
        try:
            __NO_VERSION_CHECK__         = bool(eval(__CONFIG_DATA__.split(    'no_version_check = '    )[1].split('\n')[0].split('#')[0].strip()))
        except Exception:
            _expectError('no_version_check = ', bool)
        try:
            __TRANSPILE_FILE_EXT__       = str (eval(__CONFIG_DATA__.split(   'transpile_file_ext = '   )[1].split('\n')[0].split('#')[0].strip()))
        except Exception: 
            _expectError('transpile_file_ext = ', str)
        try:
            __ALWAYS_MONITOR_PERF_DATA__ = bool(eval(__CONFIG_DATA__.split('always_monitor_perf_data = ')[1].split('\n')[0].split('#')[0].strip()))
        except Exception:
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
    global __FILE_PATH__
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
        #print(f"{__COLORS__['red']}No file path found{__COLORS__['reset']}")
        #print(f"{__COLORS__['red']}If you need help type {__COLORS__['green']}Versace -h{__COLORS__['red']}{__COLORS__['reset']}")
        #print(f"{__COLORS__['red']}Please enter the file path : {__COLORS__['reset']}", end='')
        if os.path.exists(gettempdir() + os.sep + 'VersaceIntrepeterdModeTempFILE.tmp'):
            os.remove(gettempdir() + os.sep + 'VersaceIntrepeterdModeTempFILE.tmp')
        __FILE_PATH__ = gettempdir() + os.sep + 'VersaceIntrepeterdModeTempFILE.tmp'
        with open(__FILE_PATH__, 'w', encoding='utf-8') as __TEMP_FILE_:
            __TEMP_FILE_.write('')
        if len(__PASS_LIST__) > 1 and '-d' not in __PASS_LIST__:
            raise UnhandledException('No file path provided')
        __INTREPETER__()
        

    if '\\\\' in __FILE_PATH__:
        __FILE_PATH__ = __FILE_PATH__.replace('\\', os.sep)
    elif '/' in __FILE_PATH__:
        __FILE_PATH__ = __FILE_PATH__.replace('/', os.sep)
    elif '\\' in __FILE_PATH__:
        __FILE_PATH__ = __FILE_PATH__.replace('\\', os.sep)

    if os.getcwd().lower() not in __FILE_PATH__.lower():
        __FILE_PATH__ = __FILE_PATH__
    
    os.chdir(os.getcwd())

    __FILE_PATH__ = os.path.abspath(__FILE_PATH__)

    if os.path.exists(__FILE_PATH__) is False:
        console("")
        print(f"{__COLORS__['bold red']}File path {__COLORS__['bold cyan']}{__FILE_PATH__}{__COLORS__['bold red']} does not exist{__COLORS__['reset']}")
        wait(2)
        exit()

    return
@overload
def __CHECK_ARGS__(__FILE_PATH__) -> None:
    """
    \n Inputs: __FILE_PATH__
    \n Outputs: None
    \n This is the third stage of initial checks.
    \n It will check the sys.argv flags and if they are not valid, it will print the help message.
    \n It also creates a config file if '-cfg' in passed.
    """
    __ALLOWED_ARGS__ = ('-p', '-d', '-v', '-h', '-f', '-all', '-cfg', '-ctemp', '-clear', '-t', '-c', '-1', '-2', '-3', '-exec', '-py', '-l', '-i')
    for i in __PASS_LIST__:
        if '-' in i and '.' not in i:
            if i not in __ALLOWED_ARGS__:
                console("")
                print(f'{__COLORS__["red"]}Invalid argument provided{__COLORS__["reset"]}')
                print(f'{__COLORS__["green"]}Working arguments:{__COLORS__["reset"]}')
                print(f'{__COLORS__["green"]}-p            | Shows the performance statistics of the program{__COLORS__["reset"]}') # ✅
                print(f'{__COLORS__["green"]}-d            | Runs the debug mode{__COLORS__["reset"]}')                             # ✅
                print(f'{__COLORS__["green"]}-v            | Shows the version of the program{__COLORS__["reset"]}')                # ✅
                print(f'{__COLORS__["green"]}-l            | Shows the license information{__COLORS__["reset"]}')                   # ✅
                print(f'{__COLORS__["green"]}-h            | Shows the help menu{__COLORS__["reset"]}')                             # ✅
                print(f'{__COLORS__["green"]}-f            | Forces the program to freeze before exiting{__COLORS__["reset"]}')     # ✅
                print(f'{__COLORS__["green"]}-all          | Meant to be used in conjunction with -d or -ctemp, it shows more debug data, if used with "-ctemp" it will clear the entire temp folder{__COLORS__["reset"]}') # ✅
                print(f'{__COLORS__["green"]}-cfg          | Auto creates a Versace.cfg file in your current directory and opens it in your text editor{__COLORS__["reset"]}') # ✅
                print(f'{__COLORS__["green"]}-ctemp        | Clears the data associated with inputed file (does not remove the file itself){__COLORS__["reset"]}') # ✅
                print(f'{__COLORS__["green"]}-clear        | Clears the terminal screen before execution{__COLORS__["reset"]}')     # ✅
                #print(f'{__COLORS__["green"]}-i "<code>"   | Executes code specified from the command line{__COLORS__["reset"]}')
                print(f'{__COLORS__["green"]}-t <filename> | Transpiles the Versace code to a python file{__COLORS__["reset"]}')    # ✅
                print(f'{__COLORS__["green"]}-c <filename> | Compiles the Versace code to a binary exe file{__COLORS__["reset"]}') 
                print(f'{__COLORS__["green"]}  -1**        | Must be used in conjunction with -c, it compiles the file to a single unoptimized executable file{__COLORS__["reset"]}')
                print(f'{__COLORS__["green"]}  -2**        | Must be used in conjunction with -c, it compiles the file to a faster single directory with a executable file{__COLORS__["reset"]}')
                print(f'{__COLORS__["green"]}  -3**        | Must be used in conjunction with -c, it compiles the file to a the fastest most-optimized executable file, but nested with a lot of directories{__COLORS__["reset"]}')
                print(f'{__COLORS__["green"]}  -exec**     | Must be used in conjunction with a file to be run. Runs the file without using python (quickest){__COLORS__["reset"]}') # ✅
                print(f'{__COLORS__["green"]}  -py**       | Must be used in conjunction with a file to be run. Runs the file with python {__COLORS__["bold magenta"]}(Default){__COLORS__["reset"]}') # ✅
                print(f'{__COLORS__["yellow"]}If no arguments are provided, the program will run the file you put in the first argument using python (not that slow but still slow){__COLORS__["reset"]}') 
                print(f'{__COLORS__["red"]}*<filename> is an OPTIONAL argument{__COLORS__["reset"]}')                               # ✅ 
                print(f'{__COLORS__["red"]}**Means that it must be used in conjunction with some argument{__COLORS__["reset"]}')    # ✅
                print(f'{__COLORS__["bold red"]}You used {i}{__COLORS__["reset"]}')
                exit()  # Exit the program
    if '-h' in __PASS_LIST__: __MISSALANEOUS__().__HELP_MENU__(); exit()
    if '-v' in __PASS_LIST__: __MISSALANEOUS__().__VERSION__(); exit()
    if '-l' in __PASS_LIST__: __MISSALANEOUS__().__LICENSE__(); exit()
    if '-i' in __PASS_LIST__:
        raise NotImplementedYet("The -i argument is not implemented yet")
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
    \n Input: The file path to the Versace file
    \n Output: None
    \n Opens the Versace file and passes it to the __SPLIT_ALL_LINES__ function.
    """
    global __LINES__, __LINES_FROM_FILE_RAW__, __COLORS__, __USE_CACHE__, __OPTIANAL_ARGS_IN_FILE__
    __OPTIONAL_ARGUMENT__: str = ""
    with open(__FILE_PATH__, "r") as f:
        __LINES__ = f.readlines()
        f.close()
    __LINES_FROM_FILE_RAW__ = deepcopy(__LINES__)
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
                    print(f'{__COLORS__["bold red"]}You can only use "[" and "]" to make OPTIONAL arguments, if you do not understand this, please read the documentation. here {__COLORS__["bold blue"]}https://dhruvan.gitbook.io/vs/Versace/optional-arguments{__COLORS__["reset"]}')
                    exit()
            else:
                print(f'{__COLORS__["bold red"]}No optional arguments allowed, used in line {_INDEX_ + 1}:{__COLORS__["bold yellow"]} {_LINE_.strip()}{__COLORS__["reset"]}')
                print(f'{__COLORS__["bold red"]}╰{"─" * (len(f"Miss-used optional argument in line {_INDEX_ + 1}:") - 2)}> {"^" * (len(_LINE_.strip()) - 1)}^{__COLORS__["reset"]}')
                if ',' in _LINE_.strip():
                    print(f'{__COLORS__["bold red"]}If you meant to make a list, you can use the "list" opperator, example: {__COLORS__["bold yellow"]}list(1, 2, 3){__COLORS__["reset"]}')
                    exit()
                print(f'{__COLORS__["bold red"]}You an not use optional arguments in a included file, if you do not understand this, please read the documentation. here {__COLORS__["bold blue"]}https://dhruvan.gitbook.io/vs/Versace/optional-arguments{__COLORS__["reset"]}')
                exit()
            __LINES__[_INDEX_] = ''
    if '-*- cache -*-' in __OPTIANAL_ARGS_IN_FILE__:
        __USE_CACHE__ = True
    if '-*- all errors -*-' not in __OPTIANAL_ARGS_IN_FILE__:
        __OPTIANAL_ARGS_IN_FILE__.append('-*- all errors -*-')
    __COLORS__ = _MAP_(
        {
            'bold red' : '\033[1;31m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'bold green' : '\033[1;32m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'bold yellow' : '\033[1;33m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'bold blue' : '\033[1;34m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'bold magenta' : '\033[1;35m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'bold cyan' : '\033[1;36m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'bold white' : '\033[1;37m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',

            'red' : '\033[91m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'green' : '\033[92m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'yellow' : '\033[93m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'blue' : '\033[94m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'magenta' : '\033[95m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'cyan' : '\033[96m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'white' : '\033[97m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',

            'underline' : '\033[4m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'italic' : '\033[3m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'blink' : '\033[5m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'reverse' : '\033[7m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
            'reset' : '\033[0m' if '-*- no color -*-' not in __OPTIANAL_ARGS_IN_FILE__ else '',
        }
    ) if __COLOR_SUPPORT__ else _MAP_({'red' : '', 'green' : '', 'yellow' : '', 'blue' : '', 'magenta' : '', 'cyan' : '', 'white' : '', 'bold red' : '', 'bold green' : '', 'bold yellow' : '', 'bold blue' : '', 'bold magenta' : '', 'bold cyan' : '', 'bold white' : '', 'bright_red' : '', 'bright_green' : '', 'bright_yellow' : '', 'bright_blue' : '', 'bright_magenta' : '', 'bright_cyan' : '', 'bright_white' : '', 'underline' : '', 'italic' : '', 'blink' : '', 'reverse' : '', 'reset' : ''})
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
    __LINES_COPY__ = deepcopy(__LINES__)
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
        if _INDEX_CHAR_ + 1 < len(__PRE_SPLIT_LIST__):
            if __PRE_SPLIT_LIST__[_INDEX_CHAR_] in __GLOBAL_VARIABLES__.__OPPRATORS__ and __PRE_SPLIT_LIST__[_INDEX_CHAR_ + 1] == '=':
                __PRE_SPLIT_LIST__[_INDEX_CHAR_] = __PRE_SPLIT_LIST__[_INDEX_CHAR_] + '='
                __PRE_SPLIT_LIST__.pop(_INDEX_CHAR_ + 1)

    for index, i in enumerate(__PRE_SPLIT_LIST__):
        if '.' in i:
            # check if the dot is surrounded by numbers
            if __PRE_SPLIT_LIST__[index-1].isdigit() and __PRE_SPLIT_LIST__[index+1].isdigit():
                # if so, merge the numbers and the dot
                __PRE_SPLIT_LIST__[index-1] = __PRE_SPLIT_LIST__[index-1] + '.' + __PRE_SPLIT_LIST__[index+1]
                __PRE_SPLIT_LIST__.pop(index)
                __PRE_SPLIT_LIST__.pop(index)
    
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
    __LINES_COPY__ = deepcopy(__LINES__)
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
        # if ['<', '='] in _INDEX_CHAR_, merge them
        if _INDEX_CHAR_ + 1 < len(__PRE_SPLIT_LIST__):
            if __PRE_SPLIT_LIST__[_INDEX_CHAR_] in __GLOBAL_VARIABLES__.__OPPRATORS__ and __PRE_SPLIT_LIST__[_INDEX_CHAR_ + 1] == '=':
                __PRE_SPLIT_LIST__[_INDEX_CHAR_] = __PRE_SPLIT_LIST__[_INDEX_CHAR_] + '='
                __PRE_SPLIT_LIST__.pop(_INDEX_CHAR_ + 1)

    for index, i in enumerate(__PRE_SPLIT_LIST__):
        if '.' in i:
            # check if the dot is surrounded by numbers
            if __PRE_SPLIT_LIST__[index-1].isdigit() and __PRE_SPLIT_LIST__[index+1].isdigit():
                # if so, merge the numbers and the dot
                __PRE_SPLIT_LIST__[index-1] = __PRE_SPLIT_LIST__[index-1] + '.' + __PRE_SPLIT_LIST__[index+1]
                __PRE_SPLIT_LIST__.pop(index)
                __PRE_SPLIT_LIST__.pop(index)
    
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
    __LINES_COPY__ = deepcopy(__LINES__)
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
            if len(__PRE_SPLIT_LIST__) > _INDEX_CHAR_ + 1:
                if __PRE_SPLIT_LIST__[_INDEX_CHAR_ + 1] == __CLOSING_PAIRS__[i]:
                    __PRE_SPLIT_LIST__[_INDEX_CHAR_] = i + __CLOSING_PAIRS__[i]
                    __PRE_SPLIT_LIST__.pop(_INDEX_CHAR_ + 1)
        # if the next iteem is the same as the current item then merge them, but do this without raising an index error
        if _INDEX_CHAR_ + 1 < len(__PRE_SPLIT_LIST__):
            if __PRE_SPLIT_LIST__[_INDEX_CHAR_ + 1] == i:
                __PRE_SPLIT_LIST__[_INDEX_CHAR_] = i + i
                __PRE_SPLIT_LIST__.pop(_INDEX_CHAR_ + 1)
        if _INDEX_CHAR_ + 1 < len(__PRE_SPLIT_LIST__):
            if __PRE_SPLIT_LIST__[_INDEX_CHAR_] in __GLOBAL_VARIABLES__.__OPPRATORS__ and __PRE_SPLIT_LIST__[_INDEX_CHAR_ + 1] == '=':
                __PRE_SPLIT_LIST__[_INDEX_CHAR_] = __PRE_SPLIT_LIST__[_INDEX_CHAR_] + '='
                __PRE_SPLIT_LIST__.pop(_INDEX_CHAR_ + 1)
    for index, i in enumerate(__PRE_SPLIT_LIST__):
        if '.' in i:
            # check if the dot is surrounded by numbers
            if __PRE_SPLIT_LIST__[index-1].isdigit() and __PRE_SPLIT_LIST__[index+1].isdigit():
                # if so, merge the numbers and the dot
                __PRE_SPLIT_LIST__[index-1] = __PRE_SPLIT_LIST__[index-1] + '.' + __PRE_SPLIT_LIST__[index+1]
                __PRE_SPLIT_LIST__.pop(index)
                __PRE_SPLIT_LIST__.pop(index)
    __PRE_SPLIT_LIST__ = [x.strip() for x in __PRE_SPLIT_LIST__]
    __PRE_SPLIT_LIST__ = [x for x in __PRE_SPLIT_LIST__ if x != '']
    __PRE_SPLIT_LIST__.insert(0, ' ' * (__SPACES__)) # THIS WAS THE PROBLEM <-------------------------------------------------------------

    return __PRE_SPLIT_LIST__[1:]

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

@overload_atter
def __GET_LINE_NUMBER__(__LINE__, MODE=None) -> str | int:
    """
    \n Gets the correct line number for the line from the original file.
    \n Outputs the line number or 'Line is not in file' if the line is not in the original file.
    \n Input: line - The line to get the line number for. (string)
    \n Output: line number - The line number of the line. (int)
    """
    if type(__LINE__) != str:
        __LINE__ = (''.join(__LINE__)).replace(' ', '')
    __LINE__ = __LINE__.strip().replace(' ', '')
    if '<INDENTATIONSEP>' in __LINE__:
        __LINE__ = __LINE__.replace('<INDENTATIONSEP>', '{')
    if '<DEDENTATIONSEP>' in __LINE__:
        __LINE__ = __LINE__.replace('<DEDENTATIONSEP>', '}')
    if MODE == None:
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
            return int(__SIMILAR_LINE__[__I__])

    return 'Unknown'
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
def __COLLECT_DATA__() -> None:
    global __DEBUG_DATA__
    import psutil
    __DEBUG_DATA__.append("----------------------- SYSTEM INFORMATION -----------------------")
    __DEBUG_DATA__.append(f"Hostname: {str(platform.node()).replace(os.path.expanduser('~'), '~')}")
    __DEBUG_DATA__.append(f"Hardware: {str(platform.machine()).replace(os.path.expanduser('~'), '~')}")
    __DEBUG_DATA__.append(f"OS: {str(platform.system()).replace(os.path.expanduser('~'), '~')} {str(platform.release()).replace(os.path.expanduser('~'), '~')}")
    __DEBUG_DATA__.append(f"Python Version: {str(platform.python_version()).replace(os.path.expanduser('~'), '~')}")
    __DEBUG_DATA__.append(f"Python Compiler: {str(platform.python_compiler()).replace(os.path.expanduser('~'), '~')}")
    __DEBUG_DATA__.append(f"Python Build: {str(platform.python_build()).replace(os.path.expanduser('~'), '~')}")
    __DEBUG_DATA__.append(f"Python Implementation: {str(platform.python_implementation()).replace(os.path.expanduser('~'), '~')}")
    __DEBUG_DATA__.append(f"Python Implementation Version: {str(platform.python_version_tuple()).replace(os.path.expanduser('~'), '~')}")
    __DEBUG_DATA__.append(f"Python Executable: {str(sys.executable).replace(os.path.expanduser('~'), '~')}")
    __DEBUG_DATA__.append(f"Python Path: {str(sys.path).replace(os.path.expanduser('~'), '~')}")
    __DEBUG_DATA__.append(f"Python Prefix: {str(sys.prefix).replace(os.path.expanduser('~'), '~')}")
    __DEBUG_DATA__.append(f"Python Base Prefix: {str(sys.base_prefix).replace(os.path.expanduser('~'), '~')}")
    __DEBUG_DATA__.append(f"Python Base Executable: {str(sys.base_exec_prefix).replace(os.path.expanduser('~'), '~')}")
    __DEBUG_DATA__.append(f"RAM: {psutil.virtual_memory().total}")
    __DEBUG_DATA__.append(f"CPU: {psutil.cpu_count()}")
    __DEBUG_DATA__.append(f"CPU Usage: {psutil.cpu_percent()}")
    __DEBUG_DATA__.append(f"CPU Frequency: {psutil.cpu_freq()}")
    __DEBUG_DATA__.append(f"CPU Cores: {psutil.cpu_count(logical=False)}")
    __DEBUG_DATA__.append(f"CPU Usage Per Core: {psutil.cpu_percent(percpu=True)}")
    __DEBUG_DATA__.append(f"CPU Frequency Per Core: {psutil.cpu_freq(percpu=True)}")
    if __ALLOW_TRACKING__:
        __DEBUG_DATA__.append(f"CPU Times: {psutil.cpu_times()}")
        __DEBUG_DATA__.append(f"CPU Times Per Core: {psutil.cpu_times(percpu=True)}")
        __DEBUG_DATA__.append(f"CPU Stats: {psutil.cpu_stats()}")
        __DEBUG_DATA__.append(f"Free Disk Space: {psutil.disk_usage('/').free}")
        __DEBUG_DATA__.append(f"Total Disk Space: {psutil.disk_usage('/').total}")
        __DEBUG_DATA__.append(f"Used Disk Space: {psutil.disk_usage('/').used}")
        __DEBUG_DATA__.append(f"Disk Usage: {psutil.disk_usage('/')}")
        __DEBUG_DATA__.append(f"Disk Partitions: {psutil.disk_partitions()}")
        __DEBUG_DATA__.append(f"Disk IO Counters: {psutil.disk_io_counters()}")
        __DEBUG_DATA__.append(f"Disk IO Counters Per Disk: {psutil.disk_io_counters(perdisk=True)}")
        __DEBUG_DATA__.append(f"Network IO Counters: {psutil.net_io_counters()}")
        __DEBUG_DATA__.append(f"Network IO Counters Per Interface: {psutil.net_io_counters(pernic=True)}")
        __DEBUG_DATA__.append(f"Network Connections: {psutil.net_connections()}")
        __DEBUG_DATA__.append(f"Network Interfaces: {psutil.net_if_addrs()}" )
        __DEBUG_DATA__.append(f"Network Interfaces Stats: {psutil.net_if_stats()}")
    __DEBUG_DATA__.append(f"-------------- Versace Debug Data --------------")
    __DEBUG_DATA__.append(globals())
    __DEBUG_DATA__.append(locals())
    __DEBUG_DATA__.append("----------------- End of Data ------------------")
    __DEBUG_DATA__ = tuple(__DEBUG_DATA__)
    return __DEBUG_DATA__
@property
def __ERROR_REPORTING__( __LINE__: str,
                         __ERROR__: str, 
                         __OPTIONAL__: str = '', 
                         __OPTIONAL2__: str = '', 
                         __OPTIONAL3__: str = '', 
                         LINE_NO=None, 
                         FILE_NAME=None,
                         DEBUG_LINE=None,
                         DEBUG_FILE=None ) -> None:
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
    org_args_passed = locals()
    global __OPTIANAL_ARGS_IN_FILE__, __FILE_PATH__,__FINAL_LIST__, __LINES_FROM_FILE_RAW__, __ERROR_REPORTING_CALLED__
    console("")
    if __IN_INTREPRETED_MODE__: LINE_NO="Previous Statement"
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
            'InvalidValue'                          :    'VariableError',       ###
            'notFoundError'                         :    'VariableError',       ###
            'VariableNotDeclared'                   :    'VariableError',       ###
            'AssignedValueToUndefined'              :    'VariableError',       ###
            'FromStatement'                         :    'SyntaxError',         ###
            'InvalidNumberOfVariablesToValues'      :    'SyntaxError',         ###
            'TriedToAssignValueToMultipleVariables' :    'SyntaxError',         ###
            'AddedDataTypesToPrivClass'             :    'SyntaxError',         ###
            'AddedArgumentsToPublic'                :    'SyntaxError',         ###
            'outCalledError'                        :    'SyntaxError',         ###
            'AsyncAndPrivate'                       :    'SyntaxError',         ###
            'dotUsed'                               :    'SyntaxError',         ###
            'usedHashtag'                           :    'SyntaxError',         ###
            'InvalidDelimeter'                      :    'SyntaxError',         ###
            'badStaticForLoop'                      :    'SyntaxError',         ###
            'badDynTask'                            :    'SyntaxError',         ###
            'UsedAsyncAndMethod'                    :    'SyntaxError',         ###
            'NeverClosed'                           :    'CloseError',          ###
            'unclosedComment'                       :    'CloseError',          ###
            'MissingSemiColon'                      :    'CloseError',          ###
            'AssignmentInPrivate'                   :    'TypeError',           ###
            'InvalidDataType'                       :    'TypeError',           ###
            'InvalidTypeOfValue'                    :    'TypeError',           ###
            'NullTypeFunction'                      :    'TypeError',           ###
            'TriedToAssignValueToDataClass'         :    'DataError',           ###
            'BadConfigData'                         :    'DataError',           ###
            'FileNotFound'                          :    'FileNotFoundError',   ###
            'InvalidRefrence'                       :    'RefrenceError',       ###
            'InvalidDynamicTask'                    :    'RefrenceError',       ###
            'NoInit'                                :    'NoInitError',         ###
            'InvalidKeyword'                        :    'SyntaxError',         ###
        }
    )
    __ALL_ERRORS_VERSACE_CODE_BASE__: set[str] = ('InvalidKeyword', 'notFoundError', 'VariableNotDeclared', 'AssignedValueToUndefined', 'FromStatement', 'InvalidNumberOfVariablesToValues', 'TriedToAssignValueToMultipleVariables' , 'AddedDataTypesToPrivClass', 'AddedArgumentsToPublic', 'outCalledError', 'AsyncAndPrivate', 'dotUsed', 'usedHashtag', 'InvalidDelimeter', 'NeverClosed', 'unclosedComment', 'MissingSemiColon', 'AssignmentInPrivate', 'InvalidDataType', 'InvalidTypeOfValue', 'NullTypeFunction', 'TriedToAssignValueToDataClass', 'BadConfigData', 'FileNotFound', 'InvalidRefrence', 'NoInit', 'badStaticForLoop', 'badDynTask', 'UsedAsyncAndMethod', 'InvalidDynamicTask', 'InvalidValue')
    __ALL_ERRORS__: set[str] = (
        'VariableError',
        'SyntaxError',
        'CloseError',
        'TypeError',
        'DataError',
        'FileNotFoundError',
        'RefrenceError',
        'NoInitError',
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
    def mark_words(__LINE_LIST__, WORD, BOTTOM_LINE):
        if isinstance(WORD, str) != True:
            for word in WORD:
                for i in __LINE_LIST__: 
                    if word == i:
                        BOTTOM_LINE += '^'*len(i)
                        break
                    else:
                        BOTTOM_LINE += SPACE_CHAR*(len(i)+1)
        else:
            for i in __LINE_LIST__: 
                if WORD == i:
                    BOTTOM_LINE += '^'*len(i)
                else:
                    BOTTOM_LINE += SPACE_CHAR*(len(i)+1)
        return BOTTOM_LINE
    TOP_LINE = f"{__COLORS__['red']}Bytecode Traceback in File {__FILE_PATH__}{__COLORS__['reset']}"
    MIDDLE_LINE = f"{__COLORS__['red']}{__ERROR_MAP__.get(__ERROR__)}: on line {__COLORS__['yellow']}{__LINE__NUMBER__}{__COLORS__['red']} : {__COLORS__['yellow']}{__LINE__}{__COLORS__['reset']}"
    MIDDLE_LINE_LEN = len(f'{__ERROR_MAP__.get(__ERROR__)}: on line {__LINE__NUMBER__} ') - 1
    if __ERROR__ not in __ALL_ERRORS_VERSACE_CODE_BASE__: MIDDLE_LINE = f"{__COLORS__['red']}{__OPTIONAL2__} on line {__COLORS__['yellow']}{__LINE__NUMBER__}{__COLORS__['red']} : {__COLORS__['yellow']}{__LINE__}{__COLORS__['reset']}"; MIDDLE_LINE_LEN = len(f'{__OPTIONAL2__} on line {__LINE__NUMBER__} ') - 1
    BOTTOM_LINE = f"{__COLORS__['red']}╰{'─'*MIDDLE_LINE_LEN}> "
    __LINE__ = __LINE__.strip()
    if __ERROR_REPORTING_CALLED__ == False and '-*- all errors -*-' in __OPTIANAL_ARGS_IN_FILE__: print(f"{__COLORS__['bold red']}Full Traceback:{__COLORS__['reset']}")
    __ERROR_REPORTING_CALLED__ = True
    print("")
    if __ERROR__ == "NoInit":
        UnhandledException("No init function found in the file.\n\tNOTE: if you want to run a file without a init function, add \"[-*- no init -*-]\" to the top of the file")
    elif __ERROR__ == "NeverClosed":
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}{'^'*len(__LINE__)}")
        print(f"{__COLORS__['red']}Never closed.{__COLORS__['red']}")
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
        print(f"{__COLORS__['red']}Missing semi-colon {__COLORS__['yellow']}(;){__COLORS__['red']} at the end of the line (This error was picked up because the [-*- no newline -*-] argument was found on file.{__COLORS__['reset']}")
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
            print(f"{__COLORS__['red']}Expected {__COLORS__['bold yellow']}{__DATA_TYPE_FULL__.get(__OPTIONAL__)}{__COLORS__['reset']}{__COLORS__['red']}, but got {__COLORS__['bold yellow']}{__OPTIONAL2__}{__COLORS__['reset']}{__COLORS__['red']} value instead. A value must NOT be provided if using an unsigned binary integer.{__COLORS__['reset']}")
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
    elif __ERROR__ == "notFoundError":
        BOTTOM_LINE = mark_words(__LINE_LIST__, __OPTIONAL__, BOTTOM_LINE)
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}")
        print(f"{__COLORS__['red']}Variable {__COLORS__['bold yellow']}{__OPTIONAL__}{__COLORS__['reset']}{__COLORS__['red']} was not Found{__COLORS__['reset']}")
    elif __ERROR__ == "VariableNotDeclared":
        BOTTOM_LINE = mark_words(__LINE_LIST__, __OPTIONAL__, BOTTOM_LINE)
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}")
        print(f"{__COLORS__['red']}Variable {__COLORS__['bold yellow']}{__OPTIONAL__}{__COLORS__['reset']}{__COLORS__['red']} was not declared{__COLORS__['reset']}")
    elif __ERROR__ == "AssignedValueToUndefined":
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}")
        print(f"{__COLORS__['red']}Cannot assign value to undefined variable{__COLORS__['reset']}")
    elif __ERROR__ == "FromStatement":
        BOTTOM_LINE = mark_words(__LINE_LIST__, "from", BOTTOM_LINE)
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}")
        print(f"{__COLORS__['red']}Cannot import from statement{__COLORS__['reset']}")
    elif __ERROR__ == "InvalidNumberOfVariablesToValues":
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}{'^'*len(__LINE__)}")
        print(f"{__COLORS__['red']}Invalid number of variables to values or vice versa{__COLORS__['reset']}")
    elif __ERROR__ == "TriedToAssignValueToMultipleVariables":
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}{'^'*len(__LINE__)}")
        print(f"{__COLORS__['red']}Cannot assign value to multiple variables{__COLORS__['reset']}")
    elif __ERROR__ == "AddedDataTypesToPrivClass":
        BOTTOM_LINE = mark_words(__LINE_LIST__, (__DATA_TYPE_TOKENS__.keys()), BOTTOM_LINE).strip()
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}")
        print(f"{__COLORS__['red']}Cannot add data types to private class{__COLORS__['reset']}")
    elif __ERROR__ == "AddedArgumentsToPublic":
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}{'^'*(len(__LINE__) - 2)}")
        print(f"{__COLORS__['red']}Cannot add arguments to public class{__COLORS__['reset']}")
    elif __ERROR__ == "outCalledError":
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}{'^'*len(__LINE_LIST__[0])}")
        print(f"{__COLORS__['red']}Called out more than once{__COLORS__['reset']}")
    elif __ERROR__ == "AsyncAndPrivate":
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}{' '*len(__LINE_LIST__[0])} {'^'*len(__LINE_LIST__[1])}") 
        print(f"{__COLORS__['red']}Cannot use private and async together{__COLORS__['reset']}")
    elif __ERROR__ == "usedHashtag":
        BOTTOM_LINE = mark_chars(__LINE__, '#', BOTTOM_LINE)
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}")
        print(f"{__COLORS__['red']}Cannot use # in code{__COLORS__['reset']}")
    elif __ERROR__ == "badStaticForLoop":
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}{'^'*len(__LINE__)}")
        print(f"{__COLORS__['red']}Invalid for loop{__COLORS__['reset']}")
    elif __ERROR__ == "badDynTask":
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}{'^'*len(__LINE__)}")
        print(f"{__COLORS__['red']}Invalid dynamic task{__COLORS__['reset']}")
    elif __ERROR__ == "UsedAsyncAndMethod":
        BOTTOM_LINE = mark_words(__LINE_LIST__, "async", BOTTOM_LINE)
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}")
        print(f"{__COLORS__['red']}Cannot use async and method together{__COLORS__['reset']}")
    elif __ERROR__ == "unclosedComment":
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}{'^'*len(__LINE__)}")
        print(f"{__COLORS__['red']}Unclosed comment{__COLORS__['reset']}")
    elif __ERROR__ == "AssignmentInPrivate":
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}{'^'*len(__LINE__)}")
        print(f"{__COLORS__['red']}Cannot assign value in private{__COLORS__['reset']}")
    elif __ERROR__ == "InvalidDataType":
        BOTTOM_LINE = mark_words(__LINE_LIST__, __LINE_LIST__[0], BOTTOM_LINE)
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}")
        print(f"{__COLORS__['red']}Invalid data type{__COLORS__['reset']}")
    elif __ERROR__ == "NullTypeFunction":
        BOTTOM_LINE = mark_words(__LINE_LIST__, __LINE_LIST__[0], BOTTOM_LINE)
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}")
        print(f"{__COLORS__['red']}Cannot use null type as function{__COLORS__['reset']}")
    elif __ERROR__ == "TriedToAssignValueToDataClass":
        BOTTOM_LINE = mark_chars(__LINE__, '=', BOTTOM_LINE)
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}")
        print(f"{__COLORS__['red']}Cannot assign value to structure{__COLORS__['reset']}")
    elif __ERROR__ == "BadConfigData":
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE.split('#')[0].strip()}")
        print(f"{BOTTOM_LINE}{'^'*len(__LINE__.split('#')[0].strip())}")
        print(f"{__COLORS__['red']}Invalid config data entered, {__OPTIONAL__}.{__COLORS__['reset']}")
    elif __ERROR__ == "FileNotFound":
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}{'^'*len(__LINE__)}")
        print(f"{__COLORS__['red']}File not found{__COLORS__['reset']}")
    elif __ERROR__ == "InvalidRefrence":
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}    {'^'*len(__LINE__[4:])}")
        print(f"{__COLORS__['red']}Invalid refrence{__COLORS__['reset']}")
    elif __ERROR__ == "InvalidDynamicTask":
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}          {'^'*len(__LINE__[10:])}")
        print(f"{__COLORS__['red']}Invalid dynamic task{__COLORS__['reset']}")
    elif __ERROR__ == "TriedToAssignValueToFinal": 
        BOTTOM_LINE = mark_chars(__LINE__, '=', BOTTOM_LINE)
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}")
        print(f"{__COLORS__['red']}Cannot assign a value when setting it to final{__COLORS__['reset']}")
    elif __ERROR__ == 'Used<Error':
        BOTTOM_LINE = mark_chars(__LINE__, '<', BOTTOM_LINE)
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}")
        print(f"{__COLORS__['red']}Cannot use (<), This Version of Versace expects (<<){__COLORS__['reset']}")
    elif __ERROR__ == "InvalidKeyword":
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}") 
        print(f"{BOTTOM_LINE}{'^'*len(__LINE_LIST__[0])}")
        print(f"{__COLORS__['red']}Invalid Keyword {__COLORS__['bold yellow']}{__LINE_LIST__[0]}{__COLORS__['reset']}{__COLORS__['red']} was used, if you meant to assin a value to a declared variable, use {__COLORS__['green']}'let'{__COLORS__['red']} instead.{__COLORS__['reset']}")
    elif __ERROR__ == "badReturn":
        print(f"{TOP_LINE}")
        print(f"{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}{'^'*len(__LINE__)}")
        print(f"{__COLORS__['red']}Return has to be followed by something to return, if you are intending to return nothing, use {__COLORS__['yellow']}'return 0'{__COLORS__['red']} or {__COLORS__['yellow']}'return NULL'{__COLORS__['red']}{__COLORS__['reset']}")
    else:
        print(f"{TOP_LINE}")
        print(f"{__COLORS__['red']}{MIDDLE_LINE}")
        print(f"{BOTTOM_LINE}{__OPTIONAL__}")
        print(f"{__ERROR__}{__COLORS__['reset']}")
        if '-*- all errors -*-' in __OPTIANAL_ARGS_IN_FILE__: 
            print(f"{__COLORS__['yellow']}NOTE: This last error was not generated by Versace, so the line marking may be incorrect.{__COLORS__['reset']}")
        else:
            print(f"{__COLORS__['yellow']}NOTE: This error was not generated by Versace, so the line marking may be incorrect.{__COLORS__['reset']}")
    if '-d' in __PASS_LIST__:
        from rich.pretty import pprint
        print(f"\n{__COLORS__['red']}{'-'*int((__TERMINAL_WIDTH__-11)/2)} DEBUG INFO {'-'*int((__TERMINAL_WIDTH__-11)/2)}")
        pprint(org_args_passed, expand_all=True)
        if '-all' in __PASS_LIST__:
            __COLLECT_DATA__()
            from rich import console as cconsole; rich_print = cconsole.Console().print # Define the __O__CODE_PRINT__ variable
            console("")  
            from rich.pretty import pprint 
            from rich.syntax import Syntax     
            print(f"{__COLORS__['red']}{'-'*int((__TERMINAL_WIDTH__-31)/2)} Original Data From File Passed {'-'*int((__TERMINAL_WIDTH__-31)/2)}")
            __OUTPUT__ = Syntax(''.join(__LINES_FROM_FILE_RAW__), "swift", theme="one-dark", line_numbers=True, background_color="default") # Define the __D__TOKENS__ variable
            rich_print(__OUTPUT__) # Print the __D__TOKENS__
            print(f"\n{__COLORS__['red']}{'-'*int((__TERMINAL_WIDTH__-33)/2)} Python Code Generated by Versace {'-'*int((__TERMINAL_WIDTH__-33)/2)}")
            __OUTPUT__ = Syntax('\n'.join(__FINAL_LIST__), "python", theme="one-dark", line_numbers=True, background_color="default") # Define the __D__TOKENS__ variable
            rich_print(__OUTPUT__) # Print the __D__TOKENS__
        print(f"{__COLORS__['red']}{'-'*int((__TERMINAL_WIDTH__))}{__COLORS__['reset']}")
        exit()
    if '-*- all errors -*-' in __OPTIANAL_ARGS_IN_FILE__: return
    else: exit(1)

class NotImplementedYet(Exception):
    """
    \n This class is used to raise an error when there is no main function
    """
    def __init__(self, __ERROR_WORD__: str) -> exit:
        console("")
        print(f'{__COLORS__["bold red"]}Not Implemented Yet: {__COLORS__["yellow"]}{__ERROR_WORD__}{__COLORS__["reset"]}')
        exit()
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
        print(f'{__COLORS__["bold red"]}Unhandled Exception: {__COLORS__["yellow"]}{__ERROR_WORD__}{__COLORS__["reset"]}')
        exit()

class __MISSALANEOUS__:
    def __HELP_MENU__(self) -> None:
        console("")
        print(f'{__COLORS__["yellow"]}Copyright © {__CURRENT_YEAR__} Versace{__COLORS__["reset"]}')
        print(f'{__COLORS__["green"]}If you need help, please read the documentation here: {__COLORS__["blue"]}https://dhruvan.gitbook.io/vs/{__COLORS__["reset"]}')
    def __COPYRIGHT__(self) -> None:
        console("")
        print(f'{__COLORS__["yellow"]}Copyright © 2001-{__CURRENT_YEAR__} Versace Software.{__COLORS__["reset"]}')
        print(f'{__COLORS__["yellow"]}All Rights Reserved.\n{__COLORS__["reset"]}')
        print(f'{__COLORS__["yellow"]}Copyright © 2000 GitHub, Inc.{__COLORS__["reset"]}')
        print(f'{__COLORS__["yellow"]}All Rights Reserved.\n{__COLORS__["reset"]}')
        print(f'{__COLORS__["yellow"]}Copyright © 2005-{__CURRENT_YEAR__} Dhruvan Enterprises, Software Division (DESD).{__COLORS__["reset"]}')
        print(f'{__COLORS__["yellow"]}All Rights Reserved.\n{__COLORS__["reset"]}')
    def __LICENSE__(self) -> None:
        console("")
        print(f"{__COLORS__['yellow']}Copyright {__CURRENT_YEAR__} Ze7111 (Dhruvan Kartik)\n{__COLORS__['reset']}")
        print(f"{__COLORS__['yellow']}Permission is hereby granted, free of charge, to any persons obtaining{__COLORS__['reset']}")
        print(f"{__COLORS__['yellow']}a copy of thissoftware and associated documentation files (the \"Software\"), {__COLORS__['reset']}")
        print(f"{__COLORS__['yellow']}to deal in the Software, without limitation any persons can {__COLORS__['bold red']}NOT{__COLORS__['reset']}{__COLORS__['yellow']} distribute, {__COLORS__['reset']}")
        print(f"{__COLORS__['yellow']}and/or sublicense this software without the permission of the author, however{__COLORS__['reset']}")
        print(f"{__COLORS__['yellow']}to deal in the Software, without limitation the rights to use, copy, modify, merge,{__COLORS__['reset']}")
        print(f"{__COLORS__['yellow']}and/or publish the Software.\n{__COLORS__['reset']}")
        print(f"{__COLORS__['yellow']}To permit persons to whom the Software is furnished to do so, subject to the{__COLORS__['reset']}")
        print(f"{__COLORS__['yellow']}following conditions:{__COLORS__['reset']}")
        print(f"{__COLORS__['yellow']}\tThe above copyright notice and this permission notice shall be included in all{__COLORS__['reset']}")
        print(f"{__COLORS__['yellow']}\tcopies or substantial portions of the Software.\n{__COLORS__['reset']}")
        print(f"{__COLORS__['red']}THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,{__COLORS__['reset']}")
        print(f"{__COLORS__['yellow']}\tincluding but not limited to the warranties of merchantability, fitness for a{__COLORS__['reset']}")
        print(f"{__COLORS__['yellow']}\tparticular purpose and noninfringement. In no event shall the authors or{__COLORS__['reset']}")
        print(f"{__COLORS__['yellow']}\tcopyright holders be liable for any claim, damages or other liability, whether{__COLORS__['reset']}")
        print(f"{__COLORS__['yellow']}\tin an action of contract, tort or otherwise, arising from, out of or in{__COLORS__['reset']}")
        print(f"{__COLORS__['yellow']}\tconnection with the software or the use or other dealings in the Software.\n{__COLORS__['reset']}")
    def __CREDITS__(self) -> None:
        console("")
        print(f"{__COLORS__['green']}Copyright {__CURRENT_YEAR__} Ze7111 (Dhruvan Kartik){__COLORS__['reset']}\n")
        print(f'{__COLORS__["green"]}Version: {__COLORS__["yellow"]}{__VERSION__}{__COLORS__["reset"]}')
        print(f'{__COLORS__["green"]}Author: {__COLORS__["yellow"]}Ze7111 (Dhruvan Kartik){__COLORS__["reset"]}')
        print(f'{__COLORS__["green"]}Moral Support: {__COLORS__["yellow"]}(Amr E.){__COLORS__["reset"]}')
        print(f'{__COLORS__["green"]}Devlopment team of Versace.{__COLORS__["reset"]}')
    def __VERSION__(self) -> None:
        console("")
        print(f'{__COLORS__["green"]}You are Running Versace Version: {__VERSION__}{__COLORS__["reset"]}')

class __1__:
    """This is a fake data type, to be used for overloading only"""
    pass
class __2__:
    """This is a fake data type, to be used for overloading only"""
    pass
class __3__:
    """This is a fake data type, to be used for overloading only"""
    pass

class __INCLUDE_STATEMENTS__:
    """
    \n This class is used to store the include statements.
    """
    def __VERSACE_HEADER__(__FILE_NAME__: str, __AS_STATEMENT__: str, __LINE__: list | str) -> str | list:
        if os.path.exists(f"{os.getcwd()}{os.sep}{__FILE_NAME__}") is False:
            if os.path.exists(f"{os.path.expanduser('~')}{os.sep}Versace{os.sep}include{os.sep}{__FILE_NAME__}"):
                __FILE_NAME__ = f"{os.path.expanduser('~')}{os.sep}Versace{os.sep}include{os.sep}{__FILE_NAME__}"
            else:
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
            if os.path.exists(f"{os.path.expanduser('~')}{os.sep}Versace{os.sep}include{os.sep}{__FILE_NAME__}"):
                __FILE_NAME__ = f"{os.path.expanduser('~')}{os.sep}Versace{os.sep}include{os.sep}{__FILE_NAME__}"
            else:
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
        \n Input/Output: output, input, include, from, import, pyc
        """
        def __OUTPUT__(__LINE__: list) -> str:
            global __INDENTATION_LEVEL__, __OPTIANAL_ARGS_IN_FILE__, __INDENTATION_COUNT__, __VARIABLES__, __FUNCTIONS__, __CLASSES__
            """
            \n Inputs: the line to change
            \n Outputs: python converted line
            \n This function converts Versace code to python code
            """
            __ORG_LINE__ = __LINE__.copy()
            __OUTPUT_LINE__: str = ''
            FOUND_OUT = False
            __LINE__ = ' '.join(__LINE__)
            __LINE__ = __LINE__.split('<<')
            __LINE__ = [x.strip() for x in __LINE__]
            if '<' in __ORG_LINE__:
                __ERROR_REPORTING__(__ORG_LINE__, 'Used<Error')
                return ''
            for _I_ in __LINE__:
                if _I_ == 'out':
                    if FOUND_OUT is False:
                        FOUND_OUT = True
                        __OUTPUT_LINE__ = "print("
                    else:
                        __ERROR_REPORTING__(__ORG_LINE__, 'outCalledError')
                        return ''
                elif _I_ in __GLOBAL_VARIABLES__.__END_TYPES__:
                    __OUTPUT_LINE__ += f', end="{__GLOBAL_VARIABLES__.__END_TYPES__[_I_]}"'
                elif _I_ in __GLOBAL_VARIABLES__.__JUSTIFY_TYPES__:
                    if "-*- no color -*-" not in __OPTIANAL_ARGS_IN_FILE__:
                        __OUTPUT_LINE__ += f', justify="{_I_}"'
                elif _I_ in __GLOBAL_VARIABLES__.__COLOR_TYPES__ or _I_ in __GLOBAL_VARIABLES__.__STYLE_TYPES__:
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
            \n This function converts Versace code to python code
            """

            __ORG_LINE__ = __LINE__
            __OUTPUT_LINE__: str = ''
            FOUND_OUT = False
            __LINE__ = ' '.join(__LINE__)
            __LINE__ = __LINE__.split('<<')
            __LINE__ = [x.strip() for x in __LINE__]
            if '<' in __ORG_LINE__:
                __ERROR_REPORTING__(__ORG_LINE__, 'Used<Error')
                return ''
            __OUTPUT_LINE__ += "print("
            # example line : in somevar << "Enter your name: " << endl << int
            # example output : print("Enter your name: ", end = "")\n somevar = int(input())
            __VAR__ = __LINE__[0].split(' ')[1]
            #print(__LINE__, __VAR__)
            __LINE__ = __LINE__[1:]
            __LINE_TYPE__: str = ''
            for _I_ in __LINE__:
                if _I_ in __GLOBAL_VARIABLES__.__END_TYPES__:
                    __OUTPUT_LINE__ += f', end="{__GLOBAL_VARIABLES__.__END_TYPES__[_I_]}"'
                elif _I_ in __GLOBAL_VARIABLES__.__JUSTIFY_TYPES__:
                    if "-*- no color -*-" not in __OPTIANAL_ARGS_IN_FILE__:
                        __OUTPUT_LINE__ += f', justify="{_I_}"'
                elif _I_ in __GLOBAL_VARIABLES__.__COLOR_TYPES__ or _I_ in __GLOBAL_VARIABLES__.__STYLE_TYPES__:
                    if "-*- no color -*-" not in __OPTIANAL_ARGS_IN_FILE__:
                        __OUTPUT_LINE__ += f', style="{_I_}"'
                elif _I_ == '<<':
                    continue
                elif _I_ in __GLOBAL_VARIABLES__.__DATA_TYPES__:
                    __LINE_TYPE__ = _I_
                else:
                    __OUTPUT_LINE__ += f',{_I_}'
            if 'end=' not in __OUTPUT_LINE__:
                __OUTPUT_LINE__ += ', end=""'
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
            if __NO_INCLUDES__: return ''
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
        \n Access Modifiers: public, private, method, attribute
        """
        def __PUBLIC__(__LINE__: list) -> str:
            """
            \n Inputs: the line to change
            \n Outputs: the line with the public removed
            \n This function removes the public from the line
            """
            # init({1:"1"}, 1, "str", 321)
            # close( "str", 321, {1:"1"}, 1)
            # update(321, "str", 1, {1:"1"})
            global __INDENTATION_LEVEL__, __INDENTATION_COUNT__, __PUBLIC_CLOSE_FOUND__, __PUBLIC_INIT_FOUND__, __PUBLIC_UPDATE_FOUND__, __STATIC_FOR_LINE__, __IN_STATIC_FOR__, __STATIC_FOR_CALLS__
            __OUTPUT_LINE__: str = ''
            __TEMP_LINE__: str = ' '.join(__LINE__)
            __TEMP_LINE__ = __TEMP_LINE__.split(' ')
            __TEMP_LINE__ = [x.strip() for x in __TEMP_LINE__]
            if '()' not in __TEMP_LINE__:
                __ERROR_REPORTING__(__LINE__, 'AddedArgumentsToPublic')
                return ' '
            __TEMP_LINE__ = __TEMP_LINE__[1:]
            __TEMP_LINE__.insert(0, 'def')
            if __TEMP_LINE__[1] == 'close':
                __TEMP_LINE__ = __TEMP_LINE__[:-2]
                __TEMP_LINE__.append('(a, b, c, d) <INDENTATIONSEP>\n')
            __TEMP_LINE__ = ' '.join(__TEMP_LINE__)
            __OUTPUT_LINE__ = __TEMP_LINE__
            __FUNCTION_NAME__ = __LINE__[1]
            if __FUNCTION_NAME__ == 'init':
                __PUBLIC_INIT_FOUND__ = True
                __OUTPUT_LINE__ = (__INDENTATION__*__INDENTATION_COUNT__) + '@overload(dict, int, str, int)\n'
                __OUTPUT_LINE__ += (__INDENTATION__*__INDENTATION_COUNT__) + 'def init(a, b, c, d) <INDENTATIONSEP>\n'
                __STATIC_FOR_LINE__.append('init({1:"1"}, 321, "str", 1)')
                __IN_STATIC_FOR__.append(True)
                __STATIC_FOR_CALLS__ += 1
                return __OUTPUT_LINE__
            if __FUNCTION_NAME__ == 'update':
                __PUBLIC_UPDATE_FOUND__ = True
                __OUTPUT_LINE__  = (__INDENTATION__*__INDENTATION_COUNT__) + '@_async\n'
                __OUTPUT_LINE__ += (__INDENTATION__*__INDENTATION_COUNT__) + '@overload(int, str, int, dict)\n'
                __OUTPUT_LINE__ += (__INDENTATION__*__INDENTATION_COUNT__) + 'def update(a, b, c, d):\n'
                __OUTPUT_LINE__ += (__INDENTATION__*(__INDENTATION_COUNT__ + 1)) + 'while True:\n'
                __OUTPUT_LINE__ += (__INDENTATION__*(__INDENTATION_COUNT__ + 2)) + 'if not main_thread().is_alive():\n'
                __OUTPUT_LINE__ += (__INDENTATION__*(__INDENTATION_COUNT__ + 3)) + 'exit()'
                __INDENTATION_COUNT__ += 1
                __STATIC_FOR_LINE__.append('update(321, "str", 1, {1:"1"})')
                __IN_STATIC_FOR__.append(True)
                __STATIC_FOR_CALLS__ += 1
                return __OUTPUT_LINE__
            if __FUNCTION_NAME__ == 'close':
                __OUTPUT_LINE__ = (__INDENTATION__*__INDENTATION_COUNT__) + '@overload(str, int, dict, int)\n' + __OUTPUT_LINE__
                __PUBLIC_CLOSE_FOUND__ = True
            return (__INDENTATION__*__INDENTATION_COUNT__) + __OUTPUT_LINE__
        def __PRIVATE__(__LINE__: list) -> str:
            global __INDENTATION_LEVEL__, __INDENTATION_COUNT__
            __TEMP_ARGS__ = ''
            if '=' in __LINE__:
                _FOUND_DATA_TYPE_ = False
                for _INDEX_, _I_ in enumerate(__LINE__):
                    if _I_ in __GLOBAL_VARIABLES__.__DATA_TYPES__:
                        _FOUND_DATA_TYPE_ = True
                __LINE__ = __LINE__[1:]
                if _FOUND_DATA_TYPE_ is False:
                    __ASSIGN_VARIABLE__(__LINE__[0], "PRIVATE", __LINE__[:2])
                    return __INDENTATION__*__INDENTATION_COUNT__ + ' '.join(__LINE__)
                return ' '
            __OUTPUT_LINE__: str = ''
            __TEMP_LINE__: str = ' '.join(__LINE__)
            __TEMP_LINE__ = __TEMP_LINE__.split(' ')
            if 'func' not in __TEMP_LINE__:
                if __TEMP_LINE__[1] in __GLOBAL_VARIABLES__.__DATA_TYPES__:
                    __ERROR_REPORTING__(__LINE__, 'AddedDataTypesToPrivClass')
                    return ' '
                try:
                    __TEMP_LINE__[2] = '__' + __TEMP_LINE__[2]
                except IndexError: return ' '
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
                __ARGS_IN_LINE__ = ' '.join(__LINE__[4:-2]).strip()
                __IN_STRING__ = False
                __TEMP_ARGS__ = []
                __FUNCTION_NAME__ = __LINE__[1]
                word = ''
                for char in __ARGS_IN_LINE__:
                    if char == '"':
                        __IN_STRING__ = __LATCH__(__IN_STRING__)
                    if char == '|' and not __IN_STRING__:
                        __TEMP_ARGS__.append(word.strip())
                        word = ''
                    else:
                        word += char
                __TEMP_ARGS__.append(word.strip())
                __T_TEMP_ARGS__ = __TEMP_ARGS__.copy()
                for index in range(len(__TEMP_ARGS__)):
                    if __TEMP_ARGS__[index].startswith(__GLOBAL_VARIABLES__.__DATA_TYPES__):
                        __TEMP_ARGS__[index] = __DATA_TYPE_TOKENS__[__TEMP_ARGS__[index].split(' ')[0]](__SPLIT_LINE__(__TEMP_ARGS__[index]))
                __ASSIGN_VARIABLE__(__LINE__[1], "REGULAR", ' '.join(__LINE__[2:-1]))
            __TEMP_LINE__ = [x.strip() for x in __TEMP_LINE__]
            __TEMP_LINE__ = __TEMP_LINE__[1:]
            if '(' not in __TEMP_LINE__ and ')' not in __TEMP_LINE__:
                if '()' in __TEMP_LINE__:
                    __TEMP_LINE__.insert(0, 'def')
            else:
                __TEMP_LINE__.insert(0, 'def')
            __TEMP_LINE__ = ' '.join(__TEMP_LINE__)
            __OUTPUT_LINE__ = __TEMP_LINE__
            for i in range(len(__TEMP_ARGS__)):
                __OUTPUT_LINE__ = __OUTPUT_LINE__.replace(__T_TEMP_ARGS__[i], __TEMP_ARGS__[i])
            return (__INDENTATION__*__INDENTATION_COUNT__) + __OUTPUT_LINE__
        def __METHOD__(__LINE__: list) -> str:
            global __INDENTATION_LEVEL__, __INDENTATION_COUNT__, __IN_STATIC_FOR__, __STATIC_FOR_LINE__, __STATIC_FOR_CALLS__, __EXTRA_INDENTATION__
            __ARGUMENTS__ = []
            __ARGS__: str = 'args'
            __KEYWORD_ARGS__: str = 'kwargs'
            if 'async' in __LINE__:
                __ERROR_REPORTING__(__LINE__, 'UsedAsyncAndMethod')
                return ' '
            if '|' in __LINE__:
                for INDEX in range(len(__LINE__)):
                    if __LINE__[INDEX] == '*':
                        __ARGS__ = __LINE__[INDEX+1]
                    elif __LINE__[INDEX] == '**':
                        __KEYWORD_ARGS__ = __LINE__[INDEX+1]
                if '*' not in __LINE__ and '**' not in __LINE__:
                    __ARGUMENTS__ = __LINE__[__LINE__.index('|')+1:__LINE__.index(')')]
            __ARGUMENTS__ = f"{' '.join(__ARGUMENTS__)}, " if __ARGUMENTS__ != [] else ''
            __LINE_1__ = f"{(' '.join(__LINE__[1:__LINE__.index('|')])).strip()} )" if '|' in __LINE__ else (' '.join(__LINE__[1:__LINE__.index('<INDENTATIONSEP>')])).strip()
            __OUTPUT_LINE__ = (__INDENTATION__*__INDENTATION_COUNT__) + f"def {__LINE_1__}" + ':' + '\n'
            __OUTPUT_LINE__ += (__INDENTATION__*(__INDENTATION_COUNT__+1)) + f"def method_{__LINE__[1].strip()}({__ARGUMENTS__}*{__ARGS__}, **{__KEYWORD_ARGS__})" + '<INDENTATIONSEP>'
            __STATIC_FOR_LINE__.append(f"return method_{__LINE__[1].strip()}")
            __ASSIGN_FUNCTION__(__LINE__[1], "METHOD", __LINE__[3:-2])
            __IN_STATIC_FOR__.append(True)
            __STATIC_FOR_CALLS__ += 1
            __EXTRA_INDENTATION__ = True
            __INDENTATION_COUNT__ += 1
            return __OUTPUT_LINE__
        def __AT__(__LINE__: list) -> str:
            global __INDENTATION_LEVEL__, __INDENTATION_COUNT__
            __LINE__[0] = f'{__INDENTATION__*__INDENTATION_COUNT__}{__LINE__[0]}'
            for i in range(len(__LINE__)):
                if __LINE__[i] == 'async' and __LINE__[i+1] == 'func':
                    __ERROR_REPORTING__(__LINE__, 'UsedAsyncAndMethod')
                    return ' '
                if __LINE__[i] == 'func':
                    __LINE__[i] = f'\n{__INDENTATION__*__INDENTATION_COUNT__}def'
            return ' '.join(__LINE__)
    class __control_flow__:
        """
        \n Inputs: the line to change
        \n Outputs: the line with the control flow words removed
        \n Control Flow: if, else, else if, for, while, static for, return
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
            if '|' in __LINE__:
                return __SYNTAX_ANALYSIS__.__control_flow__.__STATIC_FOR__(__LINE__)
            __OUTPUT_LINE__: str = ''
            __TEMP_LINE__: str = ' '.join(__LINE__)
            __TEMP_LINE__ = __TEMP_LINE__.split(' ')
            __TEMP_LINE__ = [x.strip() for x in __TEMP_LINE__]
            __TEMP_LINE__: str = ' '.join(__TEMP_LINE__)
            __FOUND_START__ = False
            # recognize this pattern: for ( start, condition, increment ) :
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
        def __STATIC_FOR__(__LINE__: list) -> str:
            global __INDENTATION_LEVEL__, __INDENTATION_COUNT__, __IN_STATIC_FOR__, __STATIC_FOR_LINE__, __STATIC_FOR_CALLS__
            #print((' '.join(__LINE__)).replace('<INDENTATIONSEP>', '{'))
            MATCH = search(r'for\s*\((.+?)\|(.+?)\|(.+?)\)', (' '.join(__LINE__)).replace('<INDENTATIONSEP>', '{'))
            if not MATCH:
                __ERROR_REPORTING__(__LINE__, "badStaticForLoop")
            VARIABLE_TO_USE = MATCH.group(1).strip()
            CONDITION = MATCH.group(2).strip()
            INCREMENT = MATCH.group(3).strip()
            if VARIABLE_TO_USE.startswith(__GLOBAL_VARIABLES__.__DATA_TYPES__):
                VARIABLE_TO_USE = VARIABLE_TO_USE[len(VARIABLE_TO_USE.split(' ')[0]):].strip()
            __END_CONDITIONS__ = ('++', '--', '**', '//')
            __OTHER_CONDITIONS__ = ('<=', '>=', '==', '!=', '+=', '-=', '*=', '/=', '%=', '^=', '&=', '|=')
            if INCREMENT.endswith(__END_CONDITIONS__):
                if INCREMENT.endswith('++'):
                    INCREMENT = INCREMENT[:-3]
                    INCREMENT = f"{INCREMENT} += 1"
                elif INCREMENT.endswith('--'):
                    INCREMENT = INCREMENT[:-3]
                    INCREMENT = f"{INCREMENT} -= 1"
                elif INCREMENT.endswith('**'):
                    INCREMENT = INCREMENT[:-3]
                    INCREMENT = f"{INCREMENT} *= {INCREMENT[:2]}"
                elif INCREMENT.endswith('//'):
                    INCREMENT = INCREMENT[:-3]
                    INCREMENT = f"{INCREMENT} /= {INCREMENT[:2]}"
            else:
                # line could be: i+=1
                for condition in __OTHER_CONDITIONS__:
                    if condition in INCREMENT:
                        break
                else:
                    __ERROR_REPORTING__(__LINE__, "badStaticForLoop")
            
            #print(f"Variable: {__COLORS__['red']}\"{VARIABLE_TO_USE}\"{__COLORS__['reset']} | End Condition: {__COLORS__['red']}\"{CONDITION}\"{__COLORS__['reset']} | Increment: {__COLORS__['red']}\"{INCREMENT}\"{__COLORS__['reset']}")
            __OUTPUT_LINE__ = (__INDENTATION__*__INDENTATION_COUNT__) + VARIABLE_TO_USE + '\n'
            __OUTPUT_LINE__ += (__INDENTATION__*__INDENTATION_COUNT__) + 'while ' + CONDITION + ':'
            __STATIC_FOR_LINE__.append(INCREMENT)
            __IN_STATIC_FOR__.append(True)
            __STATIC_FOR_CALLS__ += 1
            return __OUTPUT_LINE__
        def __RETURN__(__LINE__: list) -> str:
            global __INDENTATION_LEVEL__, __INDENTATION_COUNT__
            if len(__LINE__) == 1:
                __ERROR_REPORTING__(__LINE__, "badReturn")
            return (__INDENTATION__*__INDENTATION_COUNT__) + ' '.join(__LINE__)
    class __function__:
        """
        \n Inputs: the line to change
        \n Outputs: the line with the function changed
        \n Function: func, async func, await, coroutine
        """
        def __FUNCTION__(__LINE__: list) -> str:
            global __INDENTATION_LEVEL__, __INDENTATION_COUNT__
            __LINE__ = [x.strip() for x in __LINE__]
            __LINE__ = __LINE__[1:]
            __LINE__.insert(0, 'def')
            
            __ARGS_IN_LINE__ = ' '.join(__LINE__[3:-2]).strip()
            __IN_STRING__ = False
            __TEMP_ARGS__ = []
            __FUNCTION_NAME__ = __LINE__[1]
            word = ''
            for char in __ARGS_IN_LINE__:
                if char == '"':
                    __IN_STRING__ = __LATCH__(__IN_STRING__)
                if char == '|' and not __IN_STRING__:
                    __TEMP_ARGS__.append(word.strip())
                    word = ''
                else:
                    word += char
            __TEMP_ARGS__.append(word.strip())
            for index in range(len(__TEMP_ARGS__)):
                if __TEMP_ARGS__[index].startswith(__GLOBAL_VARIABLES__.__DATA_TYPES__):
                    __TEMP_ARGS__[index] = __DATA_TYPE_TOKENS__[__TEMP_ARGS__[index].split(' ')[0]](__SPLIT_LINE__(__TEMP_ARGS__[index]))
            __OUTPUT_LINE__ = (__INDENTATION__*__INDENTATION_COUNT__) + ' '.join(__LINE__[:2]) + '(' + ', '.join(__TEMP_ARGS__) + ') ' + ' '.join(__LINE__[-1:])
            __ASSIGN_VARIABLE__(__LINE__[1], "REGULAR", ' '.join(__LINE__[2:-1]))
            return __OUTPUT_LINE__
        def __ASYNC_FUNCTION__(__LINE__: list) -> str:
            global __INDENTATION_LEVEL__, __INDENTATION_COUNT__
            __LINE__ = [x.strip() for x in __LINE__]
            if 'method' in __LINE__:
                __ERROR_REPORTING__(__LINE__, 'UsedAsyncAndMethod')
            __LINE__ = __LINE__[2:]
            __LINE__.insert(0, 'def')
            __ARGS_IN_LINE__ = ' '.join(__LINE__[3:-2]).strip()
            __IN_STRING__ = False
            __TEMP_ARGS__ = []
            word = ''
            for char in __ARGS_IN_LINE__:
                if char == '"':
                    __IN_STRING__ = __LATCH__(__IN_STRING__)
                if char == '|' and not __IN_STRING__:
                    __TEMP_ARGS__.append(word.strip())
                    word = ''
                else:
                    word += char
            __TEMP_ARGS__.append(word.strip())
            for index in range(len(__TEMP_ARGS__)):
                if __TEMP_ARGS__[index].startswith(__GLOBAL_VARIABLES__.__DATA_TYPES__):
                    __TEMP_ARGS__[index] = __DATA_TYPE_TOKENS__[__TEMP_ARGS__[index].split(' ')[0]](__SPLIT_LINE__(__TEMP_ARGS__[index]))
            __OUTPUT_LINE__ = (__INDENTATION__*__INDENTATION_COUNT__) + ' '.join(__LINE__[:2]) + '(' + ', '.join(__TEMP_ARGS__) + ') ' + ' '.join(__LINE__[-1:])
            __ASSIGN_FUNCTION__(__LINE__[1], "ASYNC", ' '.join(__LINE__[2:-1]))
            __OUTPUT_LINE__ = ((__INDENTATION__*__INDENTATION_COUNT__) + '@_async\n') + __OUTPUT_LINE__
            return __OUTPUT_LINE__
        def __AWAIT__(__LINE__: list) -> str:
            global __INDENTATION_LEVEL__, __INDENTATION_COUNT__
            __OUTPUT_LINE__ = ''
            __LINE__ = [x.strip() for x in __LINE__]
            __LINE__ = __LINE__[1:]
            if '|' in __LINE__:
                __LINE__ = ' '.join(__LINE__).split('|')
                for index in range(len(__LINE__)):
                    __LINE__[index] += '.join()'
                    __OUTPUT_LINE__ += (__INDENTATION__*__INDENTATION_COUNT__) + __LINE__[index].strip() + '\n'
                return __OUTPUT_LINE__
            else:
                __LINE__.append('.join()')
                return (__INDENTATION__*__INDENTATION_COUNT__) + ' '.join(__LINE__)
        def __COROUTINE__(__LINE__: list) -> str:
            global __INDENTATION_LEVEL__, __INDENTATION_COUNT__
            __RELEASE_POOL__: str = ''
            __ARGUMENTS__: list = []
            __FUNCTIONS__: list = []
            __AWAIT__: bool = False
            __OUTPUT_LINE__: str = ''
            __T_ARGUMENTS__: str = ''
            __C_LINE__ = __LINE__.copy()
            if __LINE__[1] == 'await':
                __AWAIT__ = True
                __LINE__.pop(1)
            if 'auto_clear' in __LINE__ and '=' in __LINE__: 
                __RELEASE_POOL__ = f'TaskGroup.autorelease_pool({__LINE__[-1]})'
                try:
                    if isinstance(eval(__LINE__[-1]), bool): return (__INDENTATION__*__INDENTATION_COUNT__) + __RELEASE_POOL__
                    else: __ERROR_REPORTING__(__C_LINE__, "InvalidDynamicTask")
                except Exception:
                    __ERROR_REPORTING__(__C_LINE__, "InvalidDynamicTask")
                    return ''
                return (__INDENTATION__*__INDENTATION_COUNT__) + __RELEASE_POOL__
            elif 'clear' in __LINE__ and '()' in __LINE__: 
                return (__INDENTATION__*__INDENTATION_COUNT__) + 'TaskGroup.clear()'
            elif 'exec' in __LINE__:
                return (__INDENTATION__*__INDENTATION_COUNT__) + f'TaskGroup.execute({" ".join(__LINE__[3:-1]).replace("|", ",")})'
            elif 'delete' in __LINE__:
                return (__INDENTATION__*__INDENTATION_COUNT__) + f'TaskGroup.remove({" ".join(__LINE__[3:-1]).replace("|", ",")})'
            elif '|' in __LINE__ or ( '(' in __LINE__ and ')' in __LINE__ ):
                __LINE__ = __LINE__[1:]
                __LINE__ = ' '.join(__LINE__).split('|') if '|' in __LINE__ else __LINE__
                __LINE__ = [x.strip() for x in __LINE__]
                if __LINE__[1] == '(' and __LINE__[-1] == ')':
                    __ARGUMENTS__.append(' '.join(__LINE__[2:-1]))
                    __FUNCTIONS__.append(__LINE__[0])
                else:
                    for i in range(len(__LINE__)):
                        if '(' in __LINE__[i] and ')' in __LINE__[i]:
                            for index, char in enumerate(__LINE__[i]):
                                if char == '(':
                                    __T_ARGUMENTS__ = __LINE__[i][index+1:]
                                    break
                            # now do the same loop in reverse
                            for index, char in enumerate(__LINE__[i][::-1]):
                                if char == ')':
                                    __T_ARGUMENTS__ += __LINE__[i][:index]
                                    break
                            __ARGUMENTS__.append(__T_ARGUMENTS__[:-1].strip())
                            __T_ARGUMENTS__ = ''
                            __FUNCTIONS__.append(__LINE__[i].split('(')[0].strip())
                for i, j in zip(__FUNCTIONS__, __ARGUMENTS__):
                    j = f", {j}" if j != '' else ''
                    __OUTPUT_LINE__ += (__INDENTATION__*__INDENTATION_COUNT__) + f"TaskGroup.add({i}{j})\n"
                return __OUTPUT_LINE__
            elif __LINE__.count('()') == 1:
                return (__INDENTATION__*__INDENTATION_COUNT__) + f"TaskGroup.add(task={__LINE__[1]})"
            else:
                __ERROR_REPORTING__(__C_LINE__, 'InvalidDynamicTask')
                return ' '
    class __variable__:
        """
        \n Inputs: the line to change
        \n Outputs: the line with the variable changed
        \n Variable: <all types>, const, refrence, kernel variables, let
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
                        for i in range(len(__LINE__)):
                            if __LINE__[i] == '|':
                                __LINE__[i] = ','
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
                        for i in range(len(__LINE__)):
                            if __LINE__[i] == '|':
                                __LINE__[i] = ','
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
                        for i in range(len(__LINE__)):
                            if __LINE__[i] == '|':
                                __LINE__[i] = ','
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
                        for i in range(len(__LINE__)):
                            if __LINE__[i] == '|':
                                __LINE__[i] = ','
                        return (__INDENTATION__*__INDENTATION_COUNT__) + __OUTPUT_LINE__
                    elif __VAR_TYPE__ == 'fronzenset':
                        __OUTPUT_LINE__ = ' '.join(__LINE__)
                        __ASSIGN_VARIABLE__(__ORG_LINE__[1], __VAR_TYPE__, __VAR_VALUE__)
                        for i in range(len(__LINE__)):
                            if __LINE__[i] == '|':
                                __LINE__[i] = ','
                        return (__INDENTATION__*__INDENTATION_COUNT__) + __OUTPUT_LINE__

                if ',' in __LINE__ and '|' not in __LINE__:
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
                    for i in range(len(__LINE__)):
                        if __LINE__[i] == '|':
                            __LINE__[i] = ','
                    __ASSIGN_VARIABLE__(__LINE__[0], __VAR_TYPE__, 'None')
                    if __VAR_TYPE__ == 'usize':
                        return (__INDENTATION__*__INDENTATION_COUNT__) + __VAR_NAME__ + ' = ' + 'None'
                    return (__INDENTATION__*__INDENTATION_COUNT__) + __VAR_NAME__ + ': ' + __VAR_TYPE__
                if __VAR_TYPE__ != 'usize':
                    for i in range(len(__LINE__)):
                        if __LINE__[i] == '|':
                            __LINE__[i] = ','
                    try:
                        if type(eval(__VAR_ORG_VALUE__)).__name__ != __VAR_TYPE__:
                            __ERROR_REPORTING__(__ORG_LINE__, 'InvalidTypeOfValue', type(eval(__VAR_ORG_VALUE__)).__name__, __VAR_TYPE__)
                            return ' '
                        __OUTPUT_LINE__: str = f"{__ORG_LINE__[1]}: {__VAR_TYPE__} = {__VAR_ORG_VALUE__}"
                    except NameError:
                        __OUTPUT_LINE__: str = f"{__ORG_LINE__[1]}: {__VAR_TYPE__} = {__VAR_ORG_VALUE__}"
                    __ASSIGN_VARIABLE__(__ORG_LINE__[1], __VAR_TYPE__, __VAR_ORG_VALUE__)
                    return (__INDENTATION__*__INDENTATION_COUNT__) + __OUTPUT_LINE__
                else:
                    for i in range(len(__LINE__)):
                        if __LINE__[i] == '|':
                            __LINE__[i] = ','
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
                __OUTPUT_LINE__: str = (' '.join(__LINE__))[4:]
                # remove the first 4 characters from output line
                return (__INDENTATION__*__INDENTATION_COUNT__) + __OUTPUT_LINE__
            else: 
                for i in range(len(__LINE__)):
                    if __LINE__[i] == 'ref':
                        __LINE__[i] = 'global'
                        break
                __OUTPUT_LINE__: str = ' '.join(__LINE__)
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
                __ASSIGN_VARIABLE__(__LINE__[0], __VAR_TYPE__, "None")
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
                __ASSIGN_VARIABLE__(value.strip(), __VAR_TYPE__, __VAR_VALUE__[index])                              
            return __OUTPUT_LINE__
        def __LETTER__(__LINE__: list) -> str:
            global __INDENTATION_LEVEL__, __INDENTATION_COUNT__
            # TODO: implement this, this will check if vars are defined, and if they are it will check if they are the same type as they were originally defined as
            return f'{__INDENTATION__*__INDENTATION_COUNT__}{" ".join(__LINE__[1:])}'
        def __FINAL__(__LINE__: list) -> str:
            global __INDENTATION_LEVEL__, __INDENTATION_COUNT__
            __OUTPUT__ = __LINE__[1:] + [':', 'Final']
            if '=' in __OUTPUT__:
                __ERROR_REPORTING__(__LINE__, 'TriedToAssignValueToFinal')
                return ' '
            return f'{__INDENTATION__*__INDENTATION_COUNT__}{" ".join(__OUTPUT__)}'
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
            __ORG_LINE__ = __LINE__.copy()
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
            __LINE__.append(': Final')
            __OUTPUT_LINE__: str = ' '.join(__LINE__)
            # get the value of the variable
            try:
                __VAR_VALUE__ = __GET_VARIABLE__(__LINE__[0], 0)
            except KeyError:
                __ERROR_REPORTING__(__ORG_LINE__, 'VariableNotDeclared', __LINE__[0])
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

__KEYWORD_TOKENS__: dict[str, object] = {
    # ------------------------------ ACCESS MODIFIERS ------------------------------- #
    'public'           : __SYNTAX_ANALYSIS__. __access_modifiers__ .__PUBLIC__        ,
    'priv'             : __SYNTAX_ANALYSIS__. __access_modifiers__ .__PRIVATE__       ,
    'method'           : __SYNTAX_ANALYSIS__. __access_modifiers__ .__METHOD__        ,
    # -------------------------------- CONTROL FLOW --------------------------------- #
    'if'               : __SYNTAX_ANALYSIS__.   __control_flow__   .__IF__            ,
    'else'             : __SYNTAX_ANALYSIS__.   __control_flow__   .__ELSE__          ,
    'else if'          : __SYNTAX_ANALYSIS__.   __control_flow__   .__ELSE_IF__       ,
    'for'              : __SYNTAX_ANALYSIS__.   __control_flow__   .__FOR__           ,
    'while'            : __SYNTAX_ANALYSIS__.   __control_flow__   .__WHILE__         ,
    'return'           : __SYNTAX_ANALYSIS__.   __control_flow__   .__RETURN__        ,
    # -------------------------------- DATA CLASSES --------------------------------- #
    'class'            : __SYNTAX_ANALYSIS__.   __data_classes__   .__CLASS__         ,
    'struct'           : __SYNTAX_ANALYSIS__.   __data_classes__   .__STRUCT__        ,
    'static'           : __SYNTAX_ANALYSIS__.   __data_classes__   .__STATIC__        ,
    'enum'             : __SYNTAX_ANALYSIS__.   __data_classes__   .__ENUM__          ,
    # --------------------------------- FUNCTIONS ----------------------------------- #
    'func'             : __SYNTAX_ANALYSIS__.     __function__     .__FUNCTION__      ,
    'async'            : __SYNTAX_ANALYSIS__.     __function__     .__ASYNC_FUNCTION__,
    'await'            : __SYNTAX_ANALYSIS__.     __function__     .__AWAIT__         ,
    'coroutine'        : __SYNTAX_ANALYSIS__.     __function__     .__COROUTINE__     ,
    # --------------------------------- VARIABLES ----------------------------------- #
    'const'            : __SYNTAX_ANALYSIS__.     __variable__     .__CONSTANT__      ,
    'ref'              : __SYNTAX_ANALYSIS__.     __variable__     .__REFERENCE__     ,
    'let'              : __SYNTAX_ANALYSIS__.     __variable__     .__LETTER__        ,
    'final'            : __SYNTAX_ANALYSIS__.     __variable__     .__FINAL__         ,
    # ------------------------------- INPUT/OUTPUT ---------------------------------- #
    'out'              : __SYNTAX_ANALYSIS__.        __io__        .__OUTPUT__        ,
    'in'               : __SYNTAX_ANALYSIS__.        __io__        .__INPUT__         ,
    'include'          : __SYNTAX_ANALYSIS__.        __io__        .__INCLUDE__       ,
    'import'           : __SYNTAX_ANALYSIS__.        __io__        .__IMPORT__        ,
    'from'             : __SYNTAX_ANALYSIS__.        __io__        .__FROM__          ,
    'pyc'              : __SYNTAX_ANALYSIS__.        __io__        .__PYC__           ,
    # ------------------------------ End of Tokens ---------------------------------- #
    }
__METHOD_CALL_TOKENS__: dict[str, object] = {
    # --------------------------------- METHODS ------------------------------------- #
    '@'                : __SYNTAX_ANALYSIS__. __access_modifiers__ .__AT__            ,
    # ------------------------------ End of Tokens ---------------------------------- #
    }
__DATA_TYPE_TOKENS__: dict[str, object] = {
    # -------------------------------- DATA TYPES ----------------------------------- #
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
    # ------------------------------ End of Tokens ---------------------------------- #
    }
__TOKENS__: dict[str, object] = {}
__TOKENS__.update(__KEYWORD_TOKENS__)
__TOKENS__.update(__METHOD_CALL_TOKENS__)
__TOKENS__.update(__DATA_TYPE_TOKENS__)
__TOKENS_T_ = tuple(__TOKENS__.keys())

@property
def __PARSER__(__BALANCE_IN__, __BALANCE_OUT__) -> None:
    global __FINAL_LIST__, __INDENTATION_COUNT__, __PUBLIC_INIT_FOUND__, __EXTRA_INDENTATION__, __OPTIANAL_ARGS_IN_FILE__, __VARIABLES__, __FUNCTIONS__, __CLASSES__, __STATIC_FOR_CALLS__, __IN_STATIC_FOR__, __STATIC_FOR_LINE__
    __CURRENT_INDENTATION_COUNT__: list[int] = []
    __ADD__: bool = False
    __TRY__: int = 1
    for _INDEX_, _LINE_LIST_ in enumerate(__SPLIT_LIST__):
        __INDENTATION_LEVEL__ = 0
        #print(f"{__COLORS__['green']}Line {__GET_LINE_NUMBER__(' '.join(_LINE_LIST_))}: {__COLORS__['yellow']}{_LINE_LIST_}{__COLORS__['reset']}")
        #print(f"{str(mode):<7} |" , _INDEX_, '|', *_LINE_LIST_) 
        for index1, ii in enumerate(_LINE_LIST_):
            for iii in ii:
                if '"' not in iii:
                    if __CHECK_IF_DELARED__(iii, ii, __TYPE__=0):
                        print(ii)
                        _LINE_LIST_[index1] = '__' + _LINE_LIST_[index1]
        for index, i in enumerate(_LINE_LIST_):
            #if i == '|' and _LINE_LIST_[index + 1] == '|':
            #    __FINAL_LIST__.append(' '.join(_LINE_LIST_).replace('||', ''))
            if i in __GLOBAL_VARIABLES__.__CHANGE_WORDS__:
                _LINE_LIST_[index] = __GLOBAL_VARIABLES__.__CHANGE_WORDS__[i]
            if i == '.':
                #try:
                if _LINE_LIST_[index - 1].isnumeric() == False and _LINE_LIST_[index + 1].isnumeric() == False:
                    __ERROR_REPORTING__(_LINE_LIST_, 'dotUsed')
                #except (NameError, SyntaxError):
                #    __ERROR_REPORTING__(_LINE_LIST_, 'dotUsed')
            if '::' in i:
                _LINE_LIST_[index] = i.replace('::', '.')
        
        if _LINE_LIST_[0] == 'else' and _LINE_LIST_[1] == 'if':
            __LINE__ = __TOKENS__['else if'](_LINE_LIST_)      # <---------------------------------------------------- USING TOKEN
            if not isinstance(__LINE__, str): __LINE__ = ''
            __FINAL_LIST__.append(__LINE__.replace('<INDENTATIONSEP>', ':').replace('<DEDENTATIONSEP>', ''))
        elif _LINE_LIST_[0] in __TOKENS__:
            __LINE__ = __TOKENS__[_LINE_LIST_[0]](_LINE_LIST_) # <---------------------------------------------------- USING TOKEN
            if not isinstance(__LINE__, str): __LINE__ = ''
            __FINAL_LIST__.append(__LINE__.replace('<INDENTATIONSEP>', ':').replace('<DEDENTATIONSEP>', ''))
        else:
            __LINE__ = ' '.join(_LINE_LIST_).replace('<INDENTATIONSEP>', ':').replace('<DEDENTATIONSEP>', '')
            if not isinstance(__LINE__, str): __LINE__ = ''
            __FINAL_LIST__.append(__INDENTATION__ * __INDENTATION_COUNT__ + __LINE__)
        
        if len(__IN_STATIC_FOR__) != 0:
            __CURRENT_INDENTATION_COUNT__.append(__INDENTATION_COUNT__) if len(__CURRENT_INDENTATION_COUNT__) + 1 == __STATIC_FOR_CALLS__ else None
        
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
        if len(__IN_STATIC_FOR__) != 0:
            if __INDENTATION_COUNT__ == __CURRENT_INDENTATION_COUNT__[-1]:
                if 'init' not in __STATIC_FOR_LINE__[-1]:
                    __FINAL_LIST__.append((__INDENTATION__*(__CURRENT_INDENTATION_COUNT__[-1] + 1)) + __STATIC_FOR_LINE__[-1])
                else: __FINAL_LIST__.append((__INDENTATION__*(__CURRENT_INDENTATION_COUNT__[-1])) + __STATIC_FOR_LINE__[-1])
                if 'return' in __STATIC_FOR_LINE__[-1]:
                    __INDENTATION_COUNT__ -= 1
                    __FINAL_LIST__.pop(-1)
                    __FINAL_LIST__.append((__INDENTATION__*(__CURRENT_INDENTATION_COUNT__[-1])) + __STATIC_FOR_LINE__[-1])
                if 'update' in __STATIC_FOR_LINE__[-1]:
                    __INDENTATION_COUNT__ -= 1
                    __FINAL_LIST__.pop(-1)
                    __FINAL_LIST__.append(__STATIC_FOR_LINE__[-1])
                __CURRENT_INDENTATION_COUNT__.pop(-1)
                __IN_STATIC_FOR__.pop(-1)
                __STATIC_FOR_CALLS__ -= 1
                __STATIC_FOR_LINE__.pop(-1)
                
    for index, i in enumerate(__FINAL_LIST__):
        if '\\:' in i:
            __FINAL_LIST__[index] = i.replace('\\:', '::')
    return __BALANCE_IN__, __BALANCE_OUT__
@overload
def __LEXICAL_ANALYSIS__(mode = None, __INCLUDE_LIST__=None) -> int:
    # delete all the functions that are not needed anymore
    global __FINAL_LIST__, __INDENTATION_COUNT__, __PUBLIC_INIT_FOUND__, __OPTIANAL_ARGS_IN_FILE__, __VARIABLES__, __FUNCTIONS__, __CLASSES__, __TOKENS_T_
    __LINES_FROM_FILE_RAW_COPY__: list[str] = deepcopy(__LINES_FROM_FILE_RAW__)
    if __INCLUDE_LIST__ is None: 
        global __SPLIT_LIST__
    else: 
        __SPLIT_LIST__ = __INCLUDE_LIST__.copy()
    if __IN_INTREPRETED_MODE__:
        __FINAL_LIST__ = []
    _LINE_LIST_: list[str] = []
    __DO_NOTHING__ = False
    __ORG_SPLIT_LIST__: list[str] = deepcopy(__SPLIT_LIST__)
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
                if i.startswith('@') == False: __ERROR_REPORTING__(i, "MissingSemiColon")

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
    
    for _INDEX_, _LINE_ in enumerate(__SPLIT_LIST__):
        if '<DEDENTATIONSEP>' == _LINE_[0] or '<INDENTATIONSEP>' == _LINE_[0]:
            continue
        if _LINE_[0] in __TOKENS_T_ or _LINE_[0] in __GLOBAL_VARIABLES__.__DEF_CHARS__ or _LINE_[0] in tuple(__GLOBAL_VARIABLES__.__CHANGE_WORDS__.keys()):
            continue
        if _LINE_[0] in __GLOBAL_VARIABLES__.__ALL_PYTHON_KEYWORDS__ and __ALLOW_PYTHONIC_SYNTAX__:
            continue
        if _LINE_[-1] == ')' or _LINE_[-1] == '()':
            continue
        __ERROR_REPORTING__(_LINE_, "InvalidKeyword")
        if __IN_INTREPRETED_MODE__: return "remove"
    __BALANCE_IN__, __BALANCE_OUT__ = __PARSER__(__BALANCE_IN__, __BALANCE_OUT__)
    
    if mode == 'include': return __FINAL_LIST__
    if mode != 'include':
        if '-*- no init -*-' in __OPTIANAL_ARGS_IN_FILE__:
            pass
        else:
            if __PUBLIC_INIT_FOUND__ is False and __IN_INTREPRETED_MODE__ is False:
                __ERROR_REPORTING__(__FINAL_LIST__[1], f"NoInit")

    if __INDENTATION_COUNT__ != 0:
        for index, i in enumerate(__SPLIT_LIST__):
            if index in __BALANCE_OUT__:
                __ERROR_REPORTING__(' '.join(i).replace(':', '{', 1), 'NeverClosed')
                continue
    
    if mode != 'include':
        if __ERROR_REPORTING_CALLED__:
            if __IN_INTREPRETED_MODE__: return "remove"
            if '-f' in __PASS_LIST__: console("pause" if os.name == 'nt' else "read -p 'Press Enter to continue...' var")
            exit()
        if __PUBLIC_CLOSE_FOUND__: __FINAL_LIST__.append('\nclose( "str", 321, {1:"1"}, 1)')
        # check if there is a diffrence between the original file data and the data that is going to be written to the file
        if '-c' in __PASS_LIST__:
            DEFAULT_MODE = {1:__1__, 2:__2__, 3:__3__}
            if __BINARY__ > 3 or __BINARY__ < 1:
                raise UnhandledException(f"The binary mode {__BINARY__} specified in the config file is not supported. Only (1, 2, 3) are supported.")
            if '-1' in __PASS_LIST__:
                __COMPILER__(__1__())
            elif '-2' in __PASS_LIST__:
                __COMPILER__(__2__())
            elif '-3' in __PASS_LIST__:
                __COMPILER__(__3__())
            else:
                __COMPILER__(DEFAULT_MODE[__BINARY__]())
        elif '-t' in __PASS_LIST__:
            __TRANSPILER__()
        else:
            __EXECUTION__()
        if __IN_INTREPRETED_MODE__:
            __FINAL_LIST__ = []
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
def __EXEC_FUNCTION__(*args, **kwargs) -> None:
    try:
        # get all errors from the execution
        from tempfile import NamedTemporaryFile
        error_file = NamedTemporaryFile(mode='w', delete=False)
        execute(*args, **kwargs, stderr=error_file)
        error_file.close()
        with open(error_file.name, 'r') as f:
            errors = f.read()
        os.remove(error_file.name)
        if errors != '':
            errors = errors.splitlines()
            # invert the dict
            __INVERTED_DICT__ = {v: k for k, v in __GLOBAL_VARIABLES__.__CHANGE_WORDS__.items()}
            error_line = errors[-3].strip()
            for value in __INVERTED_DICT__:
                if value in error_line:
                    error_line = error_line.replace(value, __INVERTED_DICT__[value])
            error_line = __GET_LINE_NUMBER__(error_line, MODE='error')
            error_line_text = __LINES_FROM_FILE_RAW__[error_line-1].strip() if isinstance(error_line, int) else errors[-3].strip() + ' (Could not locate the exact line)'
            __ERROR_REPORTING__(error_line_text, errors[-1][errors[-1].find(':')+1:].strip(), errors[-2][4:], errors[-1][:errors[-1].find(':')+1], DEBUG_LINE=errors[-3].strip(), DEBUG_FILE=errors[0].strip())
            exit()
    except FileNotFoundError:
        raise UnhandledException('Execution failed, this could be caused by one or more of the following errors:\n\t- Python Path provided in the Config file is invalid.\n\t- Versace could not locate the transpiled file to execute.\n\t- The Cache File is curropted.')
@overload
def __EXECUTION__() -> None:
     # Import the NamedTemporaryFile and gettempdir functions from the tempfile module
    __CACHE_PATH__ = gettempdir() + fr'{os.sep}VERSACETEMP{os.sep}{os.path.basename(__FILE_PATH__)}.out'
    __EXEC_PATH__ = gettempdir() + fr'{os.sep}VERSACETEMP{os.sep}{os.path.basename(__FILE_PATH__)}.py'
    if os.path.exists(__EXEC_PATH__): os.remove(__EXEC_PATH__)
    __WRITE_MODE__ = 'w'
    if os.path.exists(gettempdir() + fr'{os.sep}VERSACETEMP') == False:
        os.makedirs(gettempdir() + fr'{os.sep}VERSACETEMP')
    if __USE_CACHE__:
        if os.path.exists(__EXEC_PATH__):
            with open(__EXEC_PATH__, __WRITE_MODE__, encoding="utf-8") as f:
                if f.read() != '\n'.join(__FINAL_LIST__):
                    f.write(__LINE_0__() + '\n')
                    f.write('\n'.join(__FINAL_LIST__))
                        
                    with open(__CACHE_PATH__, __WRITE_MODE__, encoding="utf-8") as f:
                        fs = StringIO()
                        with redirect_stdout(fs):
                            __EXEC_FUNCTION__([__PYTHON_PATH__, __EXEC_PATH__])
                        
        if os.path.exists(__CACHE_PATH__):
            with open(__CACHE_PATH__, 'r') as f:
                print(f.read())
                
        else:
            with open(__EXEC_PATH__, __WRITE_MODE__, encoding="utf-8") as f:
                f.write(__LINE_0__() + '\n')
                f.write('\n'.join(__FINAL_LIST__))

            with open(__CACHE_PATH__, __WRITE_MODE__, encoding="utf-8") as f:
                fs = StringIO()
                with redirect_stdout(fs):
                    __EXEC_FUNCTION__([__PYTHON_PATH__, __EXEC_PATH__])

            with open(__CACHE_PATH__, 'r') as f:
                print(f.read())
    else:
        with open(__EXEC_PATH__, __WRITE_MODE__, encoding="utf-8") as f:
            f.write(__LINE_0__() + '\n')
            f.write('\n'.join(__FINAL_LIST__))
        __EXEC_FUNCTION__([__PYTHON_PATH__, __EXEC_PATH__])
    return

@overload
def __TRANSPILER__() -> None:
    global __FINAL_LIST__, __PASS_LIST__
    console("")
    __PASS_LIST__.remove(__FILE_PATH__)
    try:
        __SAVE_PATH__ = __PASS_LIST__[__PASS_LIST__.index('-t') + 1]
    except IndexError:
        raise UnhandledException("No path specified for the transpiled file.")
    __PASS_LIST__.remove('-t')
    if '.' not in __SAVE_PATH__:
        __SAVE_PATH__ += '.py'
    if os.getcwd() not in __SAVE_PATH__:
        __SAVE_PATH__ = os.getcwd() + os.sep + __SAVE_PATH__
    with open(__SAVE_PATH__, 'w', encoding="utf-8") as f:
        f.write(__LINE_0__() + '\n')
        f.write('\n'.join(__FINAL_LIST__))
    __BOX_PRINT__(f"Transpiled {os.path.basename(__FILE_PATH__)} to {__SAVE_PATH__}", 'green', 'green')
@overload
def __INTREPETER__(CODE=None) -> None:
    global __SPLIT_LIST__, __OPTIANAL_ARGS_IN_FILE__, __IN_INTREPRETED_MODE__, __LINES__, __LINES_FROM_FILE_RAW__, __TERMINAL_WIDTH__
    __IN_INTREPRETED_MODE__ = True
    __OPTIANAL_ARGS_IN_FILE__.append('-*- all errors -*-')
    __OPTIANAL_ARGS_IN_FILE__.append('-*- no init -*-')
    __PREVIOURLINES__ = []
    print(f"{__COLORS__['yellow']}Welcome to the Versace intrepreter!{__COLORS__['reset']}")
    print(f"{__COLORS__['yellow']}Type {__COLORS__['red']}\"exit()\"{__COLORS__['yellow']} to exit the intrepreter.{__COLORS__['reset']}")
    print(f"{__COLORS__['yellow']}Type {__COLORS__['red']}\"clear()\"{__COLORS__['yellow']} to clear the screen.{__COLORS__['reset']}")
    print(f"{__COLORS__['yellow']}Type {__COLORS__['red']}\"help\"{__COLORS__['yellow']}, {__COLORS__['red']}\"copyright\"{__COLORS__['yellow']}, {__COLORS__['red']}\"credits\"{__COLORS__['yellow']} or {__COLORS__['red']}\"license\"{__COLORS__['yellow']} for more information.{__COLORS__['reset']}")
    while True:
        try:
            __INDENT_COUNT__ = 0
            os.system("")
            __TERMINAL_WIDTH__ = os.get_terminal_size().columns
            __SPLIT_LIST__ = []
            print(f"{__COLORS__['green']}> {__COLORS__['reset']}", end='')
            line = input().strip()
            if line == 'exit()':
                exit()
            elif line == 'clear()':
                console('cls' if os.name == 'nt' else 'clear')
                print(f"{__COLORS__['yellow']}You are using the Versace intrepreter{__COLORS__['reset']}")
                continue
            elif line == 'help':
                __MISSALANEOUS__().__HELP_MENU__()
                continue
            elif line == 'copyright':
                __MISSALANEOUS__().__COPYRIGHT__()
                continue
            elif line == 'credits':
                __MISSALANEOUS__().__CREDITS__()
                continue
            elif line == 'license':
                __MISSALANEOUS__().__LICENSE__()
                continue
            if line.endswith(('{', '(', '[', ',', 'if', 'else', 'while', 'for', 'def', 'class')):
                __INDENT_COUNT__ += 1
                while True:
                    try:
                        print(f"{__COLORS__['green']}. {__COLORS__['reset']}", end='')
                        line += input().strip()
                        if line.endswith(('{', '(', '[', ',', 'if', 'else', 'while', 'for', 'def', 'class','func','struct', 'enum', '{;', '(;', '[;', ',', 'if;', 'else;', 'while;', 'for;', 'func;', 'def;', 'struct;', 'enum;', 'class;')):
                            __INDENT_COUNT__ += 1
                        if line.endswith(('}', ')', ']', ',', 'if', 'else', 'while', 'for', 'def', 'class', 'func','struct', 'enum', '{;', '(;', '[;', ',', 'if;', 'else;', 'while;', 'for;', 'func;', 'def;', 'struct;', 'enum;', 'class;')):
                            __INDENT_COUNT__ -= 1
                        if __INDENT_COUNT__ == 0:
                            break
                        if __INDENT_COUNT__ < 0:
                            __ERROR_REPORTING__(line, "NeverClosed")      
                            continue  
                    except KeyboardInterrupt:
                        break
                if __INDENT_COUNT__ != 0:
                    __ERROR_REPORTING__(line, "NeverClosed")
                    continue
            if len(__PREVIOURLINES__) > 0:
                if line == __PREVIOURLINES__[-1]:
                    __PREVIOURLINES__.pop(-1)
            if line.endswith(';') != True:
                if line.endswith(('{', '(', '[', ',', 'if', 'else', 'while', 'for', 'def', 'class', 'func','struct', 'enum', '{;', '(;', '[;', ',', 'if;', 'else;', 'while;', 'for;', 'func;', 'def;', 'struct;', 'enum;', 'class;')) != True or line.endswith(('}', ')', ']', ',', 'if', 'else', 'while', 'for', 'def', 'class', 'func','struct', 'enum', '{;', '(;', '[;', ',', 'if;', 'else;', 'while;', 'for;', 'func;', 'def;', 'struct;', 'enum;', 'class;')) != True:
                    __ERROR_REPORTING__(line, "MissingSemiColon")
                    continue
            __PREVIOURLINES__.append(line)
            __LINES__ = __PREVIOURLINES__.copy()
            __LINES_FROM_FILE_RAW__ = __PREVIOURLINES__.copy()
            if '-d' in __PASS_LIST__:
                _T_TOKENS_ = __TOKENS__.copy()
                __FOUND_VALID_TOKEN__ = False
                for token in _T_TOKENS_:
                    if line.startswith(token):
                        _T_TOKENS_[token] = "Status 1"
                    else:
                        _T_TOKENS_[token] = "Status 0"
                print(f"{__COLORS__['yellow']}Tokens:{__COLORS__['reset']}")
                print(f"{__COLORS__['bold red']}{{{__COLORS__['reset']}")
                for token in _T_TOKENS_:
                    if _T_TOKENS_[token] == "Status 1":
                        __FOUND_VALID_TOKEN__ = True
                        print(f"    {__COLORS__['green']}{token}: {__COLORS__['reset']}Status 1")
                    else: 
                        print(f"    {__COLORS__['red']}{token}: {__COLORS__['reset']}Status 0")
                print(f"{__COLORS__['bold red']}}}{__COLORS__['reset']}")
                if __FOUND_VALID_TOKEN__ == False:
                    print(f"{__COLORS__['red']}No valid matching token found.{__COLORS__['reset']}")
                else:
                    print(f"{__COLORS__['green']}Valid matching token found.{__COLORS__['reset']}")
                continue
            __SPLIT_ALL_LINES__()
            if __LEXICAL_ANALYSIS__() == 'remove':
                __PREVIOURLINES__.pop(-1)
                continue
        except KeyboardInterrupt:
            print(f'{__COLORS__["bold red"]}To exit the intrepreter, type "exit()"{__COLORS__["reset"]}')
            
@property
def __MAKE_ERROR_CODE__(ERROR):
    if isinstance(ERROR, str) == False:
        ERROR = str(ERROR)
    new_code = '0xE'
    for i in range(0, len(ERROR)):
        new_code += str(hex(ord(ERROR[i]))[2:]).upper()
    return new_code.strip()
@property
def __DECODE_ERROR_CODE__(ERROR):
    ERROR = ERROR.replace('0xE', '')
    ERROR = ERROR.lower()
    new_code = ''
    for i in range(0, len(ERROR), 2):
        new_code += chr(int(ERROR[i:i+2], 16))
    return new_code.strip()

@overload
def __SHOW_DEBUG_DATA__() -> None:
    global __FINAL_LIST__, __PASS_LIST__, __DEBUG_DATA__, __LINES_FROM_FILE_RAW__
    from rich import console as cconsole; rich_print = cconsole.Console().print # Define the __O__CODE_PRINT__ variable
    from random import SystemRandom
    from rich.pretty import pprint 
    from rich.syntax import Syntax     
    console("")  
    print(f"{__COLORS__['red']}{'-'*int((__TERMINAL_WIDTH__-31)/2)} Original Data From File Passed {'-'*int((__TERMINAL_WIDTH__-31-1)/2)}{__COLORS__['reset']}")
    __OUTPUT__ = Syntax(''.join(__LINES_FROM_FILE_RAW__), "swift", theme="one-dark", line_numbers=True, background_color="default") # Define the __D__TOKENS__ variable
    rich_print(__OUTPUT__) # Print the __D__TOKENS__
    print(f"\n{__COLORS__['red']}{'-'*int((__TERMINAL_WIDTH__-33)/2)} Python Code Generated by Versace {'-'*int((__TERMINAL_WIDTH__-33-1)/2)}{__COLORS__['reset']}")
    __OUTPUT__ = Syntax('\n'.join(__FINAL_LIST__), "python", theme="one-dark", line_numbers=True, background_color="default") # Define the __D__TOKENS__ variable
    rich_print(__OUTPUT__) # Print the __D__TOKENS__
    rich_print("Checking Generated Code for Errors...", style="red")
    wait(SystemRandom().uniform(0, 2))
    try:
        if execute([sys.executable, gettempdir() + fr'{os.sep}VERSACETEMP{os.sep}{os.path.basename(__FILE_PATH__)}.py'], check=False, capture_output=True, text=False, timeout=2, encoding='utf-8', errors='ignore').returncode != 0:
            rich_print("[red]Generated Code Contains Errors.")
            rich_print("[red]If you would like the complete debug data you can add the [yellow]-all[/yellow] flag to the command line.")
    except Exception as e: 
        rich_print(f"[red]The Error Checker Encountered an Error. Please report this code to Versace: \"{(__MAKE_ERROR_CODE__(e.__class__.__name__)).strip()}\"")
        rich_print("[red]If you would like the complete debug data you can add the [yellow]-all[/yellow] flag to the command line.")
    else:
        rich_print("[green]Generated Code Contains No Errors.")
        rich_print("[green]If you would like the complete debug data you can add the [yellow]-all[/yellow] flag to the command line.")
    if '-all' in __PASS_LIST__:
        print(f"\n{__COLORS__['red']}{'-'*int((__TERMINAL_WIDTH__-21)/2)} COMPLETE DEBUG STACK {'-'*int((__TERMINAL_WIDTH__-21)/2)}{__COLORS__['reset']}")
        pprint(__DEBUG_DATA__)
    return
@property
def __DUMP_DATA__() -> None:
    if os.path.exists(f"{os.path.expanduser('~')}{os.sep}Versace{os.sep}dump") == False:
        os.makedirs(f"{os.path.expanduser('~')}{os.sep}Versace{os.sep}dump", exist_ok=True)
    # remove all .dmp files in the dump folder
    __REMOVE__ = {}
    for file in os.listdir(f"{os.path.expanduser('~')}{os.sep}Versace{os.sep}dump"):
        if file.endswith(".dmp"):
            __REMOVE__[file] = os.path.join(f"{os.path.expanduser('~')}{os.sep}Versace{os.sep}dump", file)
    # check the number of files in the dump folder
    if len(__REMOVE__) > 10:
        # sort the files by date
        __REMOVE__ = {k: v for k, v in sorted(__REMOVE__.items(), key=lambda item: item[1])}
        # remove the oldest file
        os.remove(list(__REMOVE__.values())[0])
    with open(f"{os.path.expanduser('~')}{os.sep}Versace{os.sep}dump{os.sep}{os.path.basename(__FILE_PATH__)}.dmp", 'w', encoding="utf-8") as f:
        from rich.pretty import pprint 
        fs = StringIO()
        with redirect_stdout(fs):
            pprint(__DEBUG_DATA__)
        f.write(fs.getvalue().replace('\x1b[0m', '').replace('\x1b[1m', '').replace('\x1b[2m', '').replace('\x1b[3m', ''). \
                replace('\x1b[4m', '').replace('\x1b[5m', '').replace('\x1b[6m', '').replace('\x1b[7m', '').replace('\x1b[8m', ''). \
                replace('\x1b[9m', '').replace('\x1b[30m', '').replace('\x1b[31m', '').replace('\x1b[32m', '').replace('\x1b[33m', ''). \
                replace('\x1b[34m', '').replace('\x1b[35m', '').replace('\x1b[36m', '').replace('\x1b[37m', '').replace('\x1b[38m', ''). \
                replace('\x1b[39m', '').replace('\x1b[40m', '').replace('\x1b[41m', '').replace('\x1b[42m', '').replace('\x1b[43m', ''). \
                replace('\x1b[44m', '').replace('\x1b[45m', '').replace('\x1b[46m', '').replace('\x1b[47m', '').replace('\x1b[48m', ''). \
                replace('\x1b[49m', '').replace('\x1b[90m', '').replace('\x1b[91m', '').replace('\x1b[92m', '').replace('\x1b[93m', ''). \
                replace('\x1b[94m', '').replace('\x1b[95m', '').replace('\x1b[96m', '').replace('\x1b[97m', '').replace('\x1b[98m', ''). \
                replace('\x1b[99m', '').replace('\x1b[100m', '').replace('\x1b[101m', '').replace('\x1b[102m', '').replace('\x1b[103m', ''). \
                replace('\x1b[104m', '').replace('\x1b[105m', '').replace('\x1b[106m', '').replace('\x1b[107m', '').replace('\x1b[108m', ''). \
                replace('\x1b[109m', '').replace('\x1b[2;30m', '').replace('\x1b[2;31m', '').replace('\x1b[2;32m', '').replace('\x1b[2;33m', ''). \
                replace('\x1b[2;34m', '').replace('\x1b[2;35m', '').replace('\x1b[2;36m', '').replace('\x1b[2;37m', '').replace('\x1b[2;38m', ''). \
                replace('\x1b[2;39m', '').replace('\x1b[2;40m', '').replace('\x1b[2;41m', '').replace('\x1b[2;42m', '').replace('\x1b[2;43m', ''). \
                replace('\x1b[2;44m', '').replace('\x1b[2;45m', '').replace('\x1b[2;46m', '').replace('\x1b[2;47m', '').replace('\x1b[2;48m', ''). \
                replace('\x1b[2;49m', '').replace('\x1b[2;90m', '').replace('\x1b[2;91m', '').replace('\x1b[2;92m', '').replace('\x1b[2;93m', ''). \
                replace('\x1b[2;94m', '').replace('\x1b[2;95m', '').replace('\x1b[2;96m', '').replace('\x1b[2;97m', '').replace('\x1b[2;98m', ''). \
                replace('\x1b[2;99m', '').replace('\x1b[2;100m', '').replace('\x1b[2;101m', '').replace('\x1b[2;102m', '').replace('\x1b[2;103m', ''). \
                replace('\x1b[2;104m', '').replace('\x1b[2;105m', '').replace('\x1b[2;106m', '').replace('\x1b[2;107m', '').replace('\x1b[2;108m', ''). \
                replace('\x1b[2;109m', '').replace('\x1b[3;30m', '').replace('\x1b[3;31m', '').replace('\x1b[3;32m', '').replace('\x1b[3;33m', ''). \
                replace('\x1b[3;34m', '').replace('\x1b[3;35m', '').replace('\x1b[3;36m', '').replace('\x1b[3;37m', '').replace('\x1b[3;38m', ''). \
                replace('\x1b[3;39m', '').replace('\x1b[3;40m', '').replace('\x1b[3;41m', '').replace('\x1b[3;42m', '').replace('\x1b[3;43m', ''). \
                replace('\x1b[3;44m', '').replace('\x1b[3;45m', '').replace('\x1b[3;46m', '').replace('\x1b[3;47m', '').replace('\x1b[3;48m', ''). \
                replace('\x1b[3;49m', '').replace('\x1b[3;90m', '').replace('\x1b[3;91m', '').replace('\x1b[3;92m', '').replace('\x1b[3;93m', ''). \
                replace('\x1b[3;94m', '').replace('\x1b[3;95m', '').replace('\x1b[3;96m', '').replace('\x1b[3;97m', '').replace('\x1b[3;98m', ''). \
                replace('\x1b[3;99m', '').replace('\x1b[3;100m', '').replace('\x1b[3;101m', '').replace('\x1b[3;102m', '').replace('\x1b[3;103m', ''). \
                replace('\x1b[3;104m', '').replace('\x1b[3;105m', '').replace('\x1b[3;106m', '').replace('\x1b[3;107m', '').replace('\x1b[3;108m', ''). \
                replace('\x1b[3;109m', '').replace('\x1b[3;30m', '').replace('\x1b[3;31m', '').replace('\x1b[3;32m', '').replace('\x1b[3;33m', ''). \
                replace('\x1b[4;34m', '').replace('\x1b[4;35m', '').replace('\x1b[4;36m', '').replace('\x1b[4;37m', '').replace('\x1b[4;38m', ''). \
                replace('\x1b[4;39m', '').replace('\x1b[4;40m', '').replace('\x1b[4;41m', '').replace('\x1b[4;42m', '').replace('\x1b[4;43m', ''). \
                replace('\x1b[4;44m', '').replace('\x1b[4;45m', '').replace('\x1b[4;46m', '').replace('\x1b[4;47m', '').replace('\x1b[4;48m', ''). \
                replace('\x1b[4;49m', '').replace('\x1b[4;90m', '').replace('\x1b[4;91m', '').replace('\x1b[4;92m', '').replace('\x1b[4;93m', ''). \
                replace('\x1b[4;94m', '').replace('\x1b[4;95m', '').replace('\x1b[4;96m', '').replace('\x1b[4;97m', '').replace('\x1b[4;98m', ''). \
                replace('\x1b[4;99m', '').replace('\x1b[4;100m', '').replace('\x1b[4;101m', '').replace('\x1b[4;102m', '').replace('\x1b[4;103m', ''). \
                replace('\x1b[4;104m', '').replace('\x1b[4;105m', '').replace('\x1b[4;106m', '').replace('\x1b[4;107m', '').replace('\x1b[4;108m', ''). \
                replace('\x1b[4;109m', '').replace('\x1b[4;30m', '').replace('\x1b[4;31m', '').replace('\x1b[4;32m', '').replace('\x1b[4;33m', ''). \
                replace('\x1b[5;34m', '').replace('\x1b[5;35m', '').replace('\x1b[5;36m', '').replace('\x1b[5;37m', '').replace('\x1b[5;38m', ''). \
                replace('\x1b[5;39m', '').replace('\x1b[5;40m', '').replace('\x1b[5;41m', '').replace('\x1b[5;42m', '').replace('\x1b[5;43m', ''). \
                replace('\x1b[5;44m', '').replace('\x1b[5;45m', '').replace('\x1b[5;46m', '').replace('\x1b[5;47m', '').replace('\x1b[5;48m', ''). \
                replace('\x1b[5;49m', '').replace('\x1b[5;90m', '').replace('\x1b[5;91m', '').replace('\x1b[5;92m', '').replace('\x1b[5;93m', ''). \
                replace('\x1b[5;94m', '').replace('\x1b[5;95m', '').replace('\x1b[5;96m', '').replace('\x1b[5;97m', '').replace('\x1b[5;98m', ''). \
                replace('\x1b[5;99m', '').replace('\x1b[5;100m', '').replace('\x1b[5;101m', '').replace('\x1b[5;102m', '').replace('\x1b[5;103m', ''). \
                replace('\x1b[5;104m', '').replace('\x1b[5;105m', '').replace('\x1b[5;106m', '').replace('\x1b[5;107m', '').replace('\x1b[5;108m', ''). \
                replace('\x1b[5;109m', '').replace('\x1b[5;30m', '').replace('\x1b[5;31m', '').replace('\x1b[5;32m', '').replace('\x1b[5;33m', ''). \
                replace('\x1b[6;34m', '').replace('\x1b[6;35m', '').replace('\x1b[6;36m', '').replace('\x1b[6;37m', '').replace('\x1b[6;38m', ''). \
                replace('\x1b[6;39m', '').replace('\x1b[6;40m', '').replace('\x1b[6;41m', '').replace('\x1b[6;42m', '').replace('\x1b[6;43m', ''). \
                replace('\x1b[6;44m', '').replace('\x1b[6;45m', '').replace('\x1b[6;46m', '').replace('\x1b[6;47m', '').replace('\x1b[6;48m', ''). \
                replace('\x1b[6;49m', '').replace('\x1b[6;90m', '').replace('\x1b[6;91m', '').replace('\x1b[6;92m', '').replace('\x1b[6;93m', ''). \
                replace('\x1b[6;94m', '').replace('\x1b[6;95m', '').replace('\x1b[6;96m', '').replace('\x1b[6;97m', '').replace('\x1b[6;98m', ''). \
                replace('\x1b[6;99m', '').replace('\x1b[6;100m', '').replace('\x1b[6;101m', '').replace('\x1b[6;102m', '').replace('\x1b[6;103m', ''). \
                replace('\x1b[6;104m', '').replace('\x1b[6;105m', '').replace('\x1b[6;106m', '').replace('\x1b[6;107m', '').replace('\x1b[6;108m', ''). \
                replace('\x1b[6;109m', '').replace('\x1b[6;30m', '').replace('\x1b[6;31m', '').replace('\x1b[6;32m', '').replace('\x1b[6;33m', ''). \
                replace('\x1b[1;34m', '').replace('\x1b[1;35m', '').replace('\x1b[1;36m', '').replace('\x1b[1;37m', '').replace('\x1b[1;38m', ''). \
                replace('\x1b[1;39m', '').replace('\x1b[1;40m', '').replace('\x1b[1;41m', '').replace('\x1b[1;42m', '').replace('\x1b[1;43m', ''). \
                replace('\x1b[1;44m', '').replace('\x1b[1;45m', '').replace('\x1b[1;46m', '').replace('\x1b[1;47m', '').replace('\x1b[1;48m', ''). \
                replace('\x1b[1;49m', '').replace('\x1b[1;90m', '').replace('\x1b[1;91m', '').replace('\x1b[1;92m', '').replace('\x1b[1;93m', ''). \
                replace('\x1b[1;94m', '').replace('\x1b[1;95m', '').replace('\x1b[1;96m', '').replace('\x1b[1;97m', '').replace('\x1b[1;98m', ''). \
                replace('\x1b[1;99m', '').replace('\x1b[1;100m', '').replace('\x1b[1;101m', '').replace('\x1b[1;102m', '').replace('\x1b[1;103m', ''). \
                replace('\x1b[1;104m', '').replace('\x1b[1;105m', '').replace('\x1b[1;106m', '').replace('\x1b[1;107m', '').replace('\x1b[1;108m', ''). \
                replace('\x1b[1;109m', '').replace('\x1b[1;30m', '').replace('\x1b[1;31m', '').replace('\x1b[1;32m', '').replace('\x1b[1;33m', ''))
    if '-all' in __PASS_LIST__:
        print(f"\n{__COLORS__['red']}{'-'*int((__TERMINAL_WIDTH__-18)/6)} DEBUG DATA SAVED {'-'*int((__TERMINAL_WIDTH__-18)/2)}")
        print(f"{__COLORS__['green']}Succesfully saved debug data to {os.path.expanduser('~')}{os.sep}Versace{os.sep}dump{os.sep}{os.path.basename(__FILE_PATH__)}.dmp{__COLORS__['reset']}")
    
@OVERLOAD(__1__)
def __COMPILER__(type: __1__) -> None:
    global __FINAL_LIST__, __PASS_LIST__
    __TEMP_FILE__ = gettempdir() + os.sep + f'{os.path.basename(__FILE_PATH__).split(".")[0]}.tmp'
    __PASS_LIST__.remove(__FILE_PATH__)
    __PASS_LIST__.remove('-c')
    __PASS_LIST__.remove('-1') if '-1' in __PASS_LIST__ else __PASS_LIST__
    __PASS_LIST__.pop(0)
    for i in __PASS_LIST__:
        if '.' in i:
            __SAVE_PATH__ = i
            break
    else:
        __SAVE_PATH__ = os.path.basename(__FILE_PATH__).split('.')[0]
    if '.' not in __SAVE_PATH__:
        __SAVE_PATH__ += '.exe' if os.name == 'nt' else '.out'
    if os.getcwd() not in __SAVE_PATH__:
        __SAVE_PATH__ = os.getcwd() + os.sep + __SAVE_PATH__
    with open(__TEMP_FILE__, 'w', encoding="utf-8") as f:
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
        __ICON__ = f'--icon {__ICON__}'
    else:
        __ICON__ = ''
    if __WC_TYPE__ == 'w':
        __WC_TYPE__ = '--windowed'
    else:
        __WC_TYPE__ = '--console'
    __FINAL_COMMAND__: list[str] = ["pyinstaller", "--noconfirm", "--onefile", __TEMP_FILE__, __WC_TYPE__, __ICON__]
    __FINAL_COMMAND__ = [str(i) for i in __FINAL_COMMAND__ if i != '']
    execute(__FINAL_COMMAND__)

@OVERLOAD(__2__)
def __COMPILER__(type: __2__) -> None:
    global __FINAL_LIST__, __PASS_LIST__
    __TEMP_FILE__ = gettempdir() + os.sep + f'{os.path.basename(__FILE_PATH__).split(".")[0]}.tmp'
    __PASS_LIST__.remove(__FILE_PATH__)
    __PASS_LIST__.remove('-c')
    __PASS_LIST__.remove('-1') if '-1' in __PASS_LIST__ else __PASS_LIST__
    __PASS_LIST__.pop(0)
    for i in __PASS_LIST__:
        if '.' in i:
            __SAVE_PATH__ = i
            break
    else:
        __SAVE_PATH__ = os.path.basename(__FILE_PATH__).split('.')[0]
    if '.' not in __SAVE_PATH__:
        __SAVE_PATH__ += '.exe' if os.name == 'nt' else '.out'
    if os.getcwd() not in __SAVE_PATH__:
        __SAVE_PATH__ = os.getcwd() + os.sep + __SAVE_PATH__
    with open(__TEMP_FILE__, 'w', encoding="utf-8") as f:
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
        __ICON__ = f'--icon {__ICON__}'
    else:
        __ICON__ = ''
    if __WC_TYPE__ == 'w':
        __WC_TYPE__ = '--windowed'
    else:
        __WC_TYPE__ = '--console'
    __FINAL_COMMAND__: list[str] = ["pyinstaller", "--noconfirm", "--onedir", __WC_TYPE__, __ICON__, __TEMP_FILE__]
    __FINAL_COMMAND__ = [str(i) for i in __FINAL_COMMAND__ if i != '']
    execute(__FINAL_COMMAND__)

@OVERLOAD(__3__)
def __COMPILER__(type: __3__) -> None:
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
    with open(__TEMP_FILE__, 'w', encoding="utf-8") as f:
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
    with open(__CX_TEMP_FILE__, 'w', encoding="utf-8") as f:
        for line in __CX_FREEZE_DATA__:
            f.write(line + '\n')
    execute(f'{__PYTHON_PATH__} {__CX_TEMP_FILE__} build')
    os.remove(__CX_TEMP_FILE__)
    os.remove(__TEMP_FILE__)

@property
def __INNIT_DATA_COLLECTOR__(__FILE_PATH__: str) -> None:
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
    #print(f"\ntotal {(time_diff-ammount):.5f}{'ms' if time_diff < 1 else 's'}\r")
    #exit()
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
            if 'Execution time' in j:
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
        with open(__PERF_DATA_FILE__, 'w', encoding="utf-8") as f:
            f.close()
    with open(__PERF_DATA_FILE__, 'r') as f:
        try:
            __PREVIOUS_RUN_ATTEMPT__: int = int(f.readlines()[-2].split('|')[1].strip().split(' ')[-1])
            __PREVIOUS_RUN_ATTEMPT__ += 1
        except (IndexError, ValueError):
            __PREVIOUS_RUN_ATTEMPT__: int | str = 0 if os.stat(__PERF_DATA_FILE__).st_size == 0 else "ERROR"
    with open(__PERF_DATA_FILE__, 'a', encoding="utf-8") as f:
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

def __GEN_NEW_SYNTAX_HIGHLIGHTING_DATA__() -> None:
    """Generates a new syntax file for Verscae."""
    console("")
    KW_MATCH = r'"match": "\\b(public|let|priv|if|else|if|for|while|override|class|struct|static|enum|method|func|async|await|coroutine|del|rem|const|ref|out|in|include|import|from|pyc|from|as|include|in|has|or|and|not|is|catch|throw|dyn|final|virtual)\\b"'
    DT_MATCH = r'"match": "\\b(array|arr|int|float|complex|double|str|bool|list|dict|tuple|set|bytes|char|memoryview|bytearray|frozenset|range|nullType)\\b"'
    M_MATCH1 = r'"match": "(@)\\w+"'
    M_MATCH2 = r'"match": "@"'
    NEW_KW_MATCH = r'"match": "\\b('
    NEW_DT_MATCH = r'"match": "\\b('
    NEW_M_MATCH1 = fr'"match": "({"".join(__METHOD_CALL_TOKENS__.keys())})\\w+"'
    NEW_M_MATCH2 = fr'"match": "{"".join(__METHOD_CALL_TOKENS__.keys())}"'
    print("Generating a new syntax file...")
    for index, i in enumerate(__KEYWORD_TOKENS__.keys()):
        if index == len(__KEYWORD_TOKENS__.keys()) - 1:
            NEW_KW_MATCH += i + r')\\b"'
            break
        NEW_KW_MATCH += i + "|"
    for index, i in enumerate(__DATA_TYPE_TOKENS__.keys()):
        if index == len(__DATA_TYPE_TOKENS__.keys()) - 1:
            NEW_DT_MATCH += i + r')\\b"'
            break
        NEW_DT_MATCH += i + "|"
    # where are vscode extensions located?
    if os.name == "nt":
        __VSCODE_EXT_DIR__ = r"%USERPROFILE%\.vscode\extensions"
    elif os.name == "posix":
        __VSCODE_EXT_DIR__ = r"~/.vscode/extensions"
    else:
        raise NotImplementedError("Your OS is not supported.")
    print(f"{__COLORS__['red']}Head over to where the syntax file is located inside the extension folder in a sub-folder called syntax (usually here: {__VSCODE_EXT_DIR__}) and replace the following lines:{__COLORS__['reset']}")
    print(f"{__COLORS__['red']}Line 1: {__COLORS__['yellow']}{KW_MATCH}{__COLORS__['reset']}")
    print(f"{__COLORS__['red']}Replace with: {__COLORS__['green']}{NEW_KW_MATCH}{__COLORS__['reset']}")
    print(f"{__COLORS__['red']}Line 2: {__COLORS__['yellow']}{DT_MATCH}{__COLORS__['reset']}")
    print(f"{__COLORS__['red']}Replace with: {__COLORS__['green']}{NEW_DT_MATCH}{__COLORS__['reset']}")
    print(f"{__COLORS__['red']}Line 3: {__COLORS__['yellow']}{M_MATCH1}{__COLORS__['reset']}")
    print(f"{__COLORS__['red']}Replace with: {__COLORS__['green']}{NEW_M_MATCH1}{__COLORS__['reset']}")
    print(f"{__COLORS__['red']}Line 4: {__COLORS__['yellow']}{M_MATCH2}{__COLORS__['reset']}")
    print(f"{__COLORS__['red']}Replace with: {__COLORS__['green']}{NEW_M_MATCH2}{__COLORS__['reset']}")
    print(f"{__COLORS__['red']}Then restart VSCode and you should be good to go!{__COLORS__['reset']}")
    exit()
    
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
            if int(temp_time_diff[1][0]) - ammount < 0: 
                ammount -= 1
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
    #__GEN_NEW_SYNTAX_HIGHLIGHTING_DATA__() # uncomment this line to generate new syntax highlighting data, ONLY USE THIS IF YOU CHANGED THE TOKENS
    #__DECODE_ERROR_CODE__(ERROR) # uncomment this line to decode an error code
    try:
        global __FILE_PATH__
        __GET_OS__()
        __INITIALIZE__()
        __READ_SYS_ARGS__()
        __INITIALIZE_CHECKS__()
        __INNIT_DATA_COLLECTOR__(__FILE_PATH__)
        __CHECK_ARGS__(__FILE_PATH__)
        __OPEN_FILE__(__FILE_PATH__)
        __SPLIT_ALL_LINES__()
        __LEXICAL_ANALYSIS__()
        if '-d' in __PASS_LIST__:
            __COLLECT_DATA__()
            __SHOW_DEBUG_DATA__()
            __DUMP_DATA__()
    finally:
        console("")
        print(__COLORS__["reset"], end="\r")
        if '-f' in __PASS_LIST__:
            os.system("pause" if os.name == "nt" else "read -p 'Press Enter to continue...' var")
            exit()

if __name__ == "__main__": __INITIALIZER__()
else: raise UnhandledException("Verscae is not meant to be imported, it should be run through the command line.")
