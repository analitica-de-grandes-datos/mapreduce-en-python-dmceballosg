#
import os

result = os.popen("cat data.csv | python3 mapper.py | sort | python3 reducer.py").read()

lines = [line.strip().replace("\n", "") for line in result.split("\n")]

expected = """A	0,1,5,7,8,9,10,12,13,14,15,16,17,18,21,23,24,25,26,27,28,29
B	0,1,2,3,5,6,7,8,9,10,11,12,15,16,17,18,19,20,21,22,23,25,26,27,29
C	0,1,3,4,5,6,7,9,10,11,12,14,15,17,20,21,22,23,25,28,29
D	0,1,3,4,5,6,6,7,8,9,9,10,11,12,12,13,14,15,16,17,18,19,19,20,20,21,23,23,24,26,26,27,28,29,29
F	0,1,2,6,7,8,9,11,12,13,15,17,18,19,20,21,22,23,24,25,26,27,28,29
G	2,4,6,7,9,11,12,14,15,17,20,21,22,24,25,26,27,29
H	0,1,2,4,5,6,7,10,11,12,15,17,18,20,22,23,24,25,26,27,28,29
I	0,1,2,4,7,8,9,11,15,16,18,19,20,22,25,26,27
""".split(
    "\n"
)

if len(lines) != len(expected):
    raise Exception("Wrong number of lines")

for solution, expected in zip(lines, expected):
    assert (
        solution.strip() == expected.strip()
    ), f"Expected: {expected}\nGot: {solution}"
