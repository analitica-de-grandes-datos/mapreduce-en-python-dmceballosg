#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

def clear_spaces(x):
    x = x.replace("\n", "")
    x = x.replace("\r", "")
    return x

def purpose_amount(x):
    return  clear_spaces(x[1]) +  "*" + clear_spaces(x[0])

for line in sys.stdin:
    result = line.split(',')
    print(purpose_amount(result))