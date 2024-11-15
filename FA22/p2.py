
import sys

def convert(sym):
    match sym:
        case '.-':
            return 'a'
        case '-...':
            return 'b'
        case '-.-.':
            return 'c'
        case '-..':
            return 'd'
        case '.':
            return 'e'
        case '..-.':
            return 'f'
        case '--.':
            return 'g'
        case '....':
            return 'h'
        case '..':
            return 'i'
        case '.---':
            return 'j'
        case '-.-':
            return 'k'
        case '.-..':
            return 'l'
        case '--':
            return 'm'
        case '-.':
            return 'n'
        case '---':
            return 'o'
        case '.--.':
            return 'p'
        case '--.-':
            return 'q'
        case '.-.':
            return 'r'
        case '...':
            return 's'
        case '-':
            return 't'
        case '..-':
            return 'u'
        case '...-':
            return 'v'
        case '.--':
            return 'w'
        case '-..-':
            return 'x'
        case '-.--':
            return 'y'
        case '--..':
            return 'z'



lines = []
for line in sys.stdin:
    lines.append(line.strip())

for line in lines:
    line = line.split(" ")
    for letter in line:
        print(f"{convert(letter)}", end='')
    print(" ")
    