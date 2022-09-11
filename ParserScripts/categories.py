from string import ascii_letters
from typing import Iterable

def get_categories() -> Iterable:
    with open("ParserScripts/Results/categories.html", "r", encoding='utf-8') as file:
        line = file.read()
        for i in line:
            if i in list(ascii_letters + """1234567890<>="'()/-;.:_,"""):
                line = line.replace(i, '')
        list_with_spaces = [i for i in line.split("  ") if i != '']
        return [i[1:] or i for i in list_with_spaces if i[0] == ' '] + [i for i in list_with_spaces if i[0] != ' '] 