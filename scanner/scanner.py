import re

from scanner.tokens import arithmetic_, datatypes_, keywords_, logical_, signs_, whitespaces_, digits_, letters_

# Types
# boolean: 1 byte
# integer: 4 byte, two's complement
# character: 1 byte
# real: 4 byte
# string:‌ Array of characters
<<<<<<< HEAD

UNKNOWN, INTEGER, REAL, ID, CHAR, STRING, COMMENT = range(7)

class Scanner():
    def __init__(self, path):
        with open(path, 'r') as f:
            self.text = f.read()+'\n'
        self.index = 0
        self.length = len(self.text)
        self.prev_result = ('', UNKNOWN)
    
    def next(self):
        i = self.index
        text = self.text
        result = ''
        if self.prev_result[0]:
            result = self.prev_result
            self.prev_result = ('', UNKNOWN)
            return result
        prev_result = ''
        t = UNKNOWN
        while i < self.length and text[i] in whitespaces_:
            i += 1
        if i == self.length:
                return
        while True:
            if text[i] in whitespaces_:
                break
            if text[i] in digits_:
                t = INTEGER
                result += text[i]
                i += 1
                while text[i] in digits_:
                    result += text[i]
                    i += 1
                if text[i] == '.':
                    t = REAL
                    result += '.'
                    i += 1
                    while text[i] in digits_:
                        result += text[i]
                        i += 1
            elif text[i] == '.':
                result += '.'
                i += 1
                if text[i] in digits_:
                    t = REAL
                    result += text[i]
                    i += 1
                    while text[i] in digits_:
                        result += text[i]
                        i += 1
            elif text[i] in letters_:
                t = ID
                result += text[i]
                i += 1
                while text[i] in letters_+digits_+['_']:
                    result += text[i]
                    i += 1
            elif text[i] == '\'':
                result += text[i+1]
                i += 2
                if text[i] == '\'':
                    t = CHAR
                    i += 1
            elif text[i] == '"':
                i += 1
                while text[i] != '"':
                    result += text[i]
                    i += 1
                t = STRING
                i += 1
            elif text[i:i+2] == '--':
                t = COMMENT
                i += 2
                while text[i] != '\n':
                    result += text[i]
                    i += 1
                i += 1
            elif text[i:i+3] == '<--':
                t = COMMENT
                i += 3
                while text[i:i+3] != '-->':
                    result += text[i]
                    i += 1
                i += 3
            elif t == UNKNOWN:
                prev_result += text[i]
                i += 1
            else:
                break
        self.index = i
        if prev_result:
            self.prev_result = (result, t)
            return (prev_result, UNKNOWN)
        return (result, t)
=======
>>>>>>> 2ab1597b3fd6acec6c2588295d34cbfef579c90d
