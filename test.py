from scanner.scanner import Scanner

s = Scanner('/Users/amirhasan/desktop/compiler/project/compiler/input.txt')
while True:
    t = s.next()
    if t:
        print(t)
    else:
        break