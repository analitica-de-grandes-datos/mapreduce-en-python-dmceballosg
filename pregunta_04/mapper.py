#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

def purpose_amount(x):
    return   x[0]  + "*" + x[2].replace("\r\n","")

for line in sys.stdin:
    line = line.replace("'","")
    result = line.split('   ')
    print(purpose_amount(result))