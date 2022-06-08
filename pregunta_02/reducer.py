import sys
elements_reduced = {};

def get_bigger(acc, nxt):
    nxt_param = nxt.split("*")
    actual_value = int(acc.get(nxt_param[0]) or 0)
    acc[nxt_param[0]] = actual_value if actual_value > int(nxt_param[1]) else int(nxt_param[1])
    return acc

for line in sys.stdin:
    get_bigger(elements_reduced, line)

for elements_reduced, index in elements_reduced.items():
    print(elements_reduced + "	" + str(index), end = '\n')
