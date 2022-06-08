#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys


def purpose_amount(x):
    return x[3] + "*" + x[4]


for line in sys.stdin:
    result = line.split(',')
    print(purpose_amount(result))
