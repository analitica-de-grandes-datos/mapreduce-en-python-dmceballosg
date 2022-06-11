#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

def clear_spaces(x):
    x = x.replace("\n", "")
    x = x.replace("\r", "")
    return x

def purpose_amount(x):
    return  clear_spaces(x[0]), clear_spaces(x[1]).split(",")

for line in sys.stdin:
    line = line.replace("'","")
    result = line.split('\t')
    number, array = purpose_amount(result) 
    for letter_array in array:
        print(letter_array + "*" + number)