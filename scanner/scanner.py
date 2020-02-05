import re

from scanner.tokens import arithmetic_, datatypes_, keywords_, logical_, signs_, whitespaces_

# class SymbolTable:
#     symbol_table = {}
#     def __init__(self, type=None, value=None):
#         if type == 
# Types
# boolean: 1 byte
# integer: 4 byte, two's complement
# character: 1 byte
# real: 4 byte
# string:‌ Array of characters

class SymbolData:
    def __init__(self, name, type=None, value=None, size=None):
        self.name = name
        self.type = type
        self.value = value
        self.array = False
        self.size = size


symbol_table_stack = []


def init_scope():
    symbol_table = dict()
    symbol_table['boolean'] = SymbolData('boolean', type='boolean', size=1)
    symbol_table['integer'] = SymbolData('integer', type='integer', size=4)
    symbol_table['character'] = SymbolData('character', type='character', size=1)
    symbol_table['real'] = SymbolData('real', type='real', size=4)
    symbol_table_stack.append(symbol

