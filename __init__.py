"""
This __init__.py file allows Python to read your package files
and compile them as a package. It is standard practice to leave 
this empty if your package's modules and subpackages do not share
any code.
(If your package is just a module, then you can put that code here.)
"""
import random


CYRILLIC_MAP = {
    'a': 'а',
    # 'q': '𝚚', 
    'u': 'ս',
    'n': 'ո',
    #'t': '𝚝', 
    #'m': '𝚖', 
    'c': 'с',
    'o': 'о',
    'l': 'ӏ'
}

ZWJ_PROBABILITY = 0.2

def replace_letters(input_text):
    output = ""
    for char in input_text:
        output += CYRILLIC_MAP.get(char, char)
    return output

def insert_zwj(input_text):
    output = ""
    zwj = "\u200D"
    for char in input_text:
        output += char
        if random.random() < ZWJ_PROBABILITY:
            output += zwj
    return output

def foggy(inText):
    textRL = replace_letters(inText)
    outText = insert_zwj(textRL)
    return outText



    



