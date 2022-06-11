#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
biggest_purposes = []
count_elements_col_3 = 0


def set_bigger_purpose(array_purposes, actual_element):
    actual_element = actual_element.replace("\n", "")
    biggest_purposes.append(actual_element)
    return array_purposes


def sortByColumn3(element):
    return int(element.split(";")[0])


for line in sys.stdin:
    set_bigger_purpose(biggest_purposes, line)

biggest_purposes.sort(key=sortByColumn3)

for purpose in biggest_purposes:
    count_elements_col_3 = count_elements_col_3 + 1
    element = purpose.split(";")
    print(element[1]+ "   " + element[2] + "   " + element [0])
    if count_elements_col_3 > 5:
        break
     