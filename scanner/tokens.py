import string

whitespaces_ = [
    '\n',
    '\t',
    ' ',
    '\f',
    '\r',
    '\t',
    '\v'
]

keywords_ = [
    'array',
    'assign',
    'boolean',
    'break',
    'begin',
    'char',
    'continue',
    'do',
    'else',
    'end',
    'false',
    'function',
    'procedure',
    'if',
    'integer',
    'of',
    'real',
    'return',
    'string',
    'true',
    'while',
    'var',
]

arithmetic_ = [
    '+',
    '*',
    '&',
    '^',
    '|',
    '%'
]

logical_ = [
    '<=',
    '>',
    '>=',
    '=',
    '<>',
    '~'
]

datatypes_ = [
    'array',
    'boolean',
    'integer',
    'character',
    'real',
    'string'
]

signs_ = [
    '(',
    ')',
    ',',
    ';',
    ':',
    ':=',
    '[',
    ']'
]

digits_ = [
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9'
]

letters_ = list(string.ascii_letters)