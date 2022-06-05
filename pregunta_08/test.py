#
import os

result = os.popen("cat data.csv | python3 mapper.py | sort | python3 reducer.py").read()

lines = [line.strip().replace("\n", "") for line in result.split("\n")]

expected = """A	165.0	13.75
B	136.0	13.6
C	48.0	12.0
D	15.0	15.0
E	192.0	14.76923076923077
""".split(
    "\n"
)

if len(lines) != len(expected):
    raise Exception("Wrong number of lines")

for solution, expected in zip(lines, expected):
    assert (
        solution.strip() == expected.strip()
    ), f"Expected: {expected}\nGot: {solution}"
