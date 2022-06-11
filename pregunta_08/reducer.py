#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
sum = {}
counted = {}

def set_bigger_smaller_amount(sum, counted, actual_element):
    element_array = actual_element.split("*")
    sum[element_array[0]] = float(sum.get(element_array[0]) or 0) + float(element_array[1])
    counted[actual_element[0]] = float(counted.get(actual_element[0]) or 0)  +1 
    return sum, counted

for line in sys.stdin:
    set_bigger_smaller_amount(sum, counted, line)

for max, min in zip(sum.items(), counted.items()):
    print( max[0] + "	" + str(max[1]) + "	" + str(float(max[1])/float(min[1])) )