#
import os

result = os.popen("cat data.csv | python3 mapper.py | sort | python3 reducer.py").read()

lines = [line.strip().replace("\n", "") for line in result.split("\n")]

expected = """C   1994-07-27   1	
C   1991-02-12   2	
A   1990-07-22   4	
A   1990-09-26   5	
B   1997-04-09   6	
E   1998-09-14   7
""".split(
    "\n"
)

if len(lines) != len(expected):
    raise Exception("Wrong number of lines")

for solution, expected in zip(lines, expected):
    assert (
        solution.strip() == expected.strip()
    ), f"Expected: {expected}\nGot: {solution}"
