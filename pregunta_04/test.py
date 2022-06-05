#
import os

result = os.popen("cat data.csv | python3 mapper.py | sort | python3 reducer.py").read()

lines = [line.strip().replace("\n", "") for line in result.split("\n")]

expected = """A,12
B,10
C,4
D,1
E,13
""".split(
    "\n"
)

if len(lines) != len(expected):
    raise Exception("Wrong number of lines")

for solution, expected in zip(lines, expected):
    assert solution == expected, f"Expected: {expected}\nGot: {solution}"
