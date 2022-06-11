#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
biggest_purposes = {}


def set_bigger_purpose(dictionary_purposes, actual_element):
    actual_element = actual_element.replace("\n", "")
    letter = actual_element.split(" ") [0]
    if  str(dictionary_purposes.get(letter) or "") == "":
        dictionary_purposes[letter] =    str(dictionary_purposes.get(letter) or "") + actual_element.split(" ") [1]
    else:
        dictionary_purposes[letter] =    str(dictionary_purposes.get(letter) or "") +  "*" + actual_element.split(" ") [1]
    return dictionary_purposes


def sortByColumn3(element):
    return int(element.split(";")[0])


for line in sys.stdin:
    set_bigger_purpose(biggest_purposes, line)

for purpose, values_and_dates in biggest_purposes.items():
    elements = values_and_dates.split("*")
    elements.sort(key =sortByColumn3)
    biggest_purposes[purpose] = elements
    for element in elements:
        print(purpose + "   " + element.split(";")[1] + "   " + element.split(";")[0] )

