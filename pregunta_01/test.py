#
import os

result = os.popen(
    "cat credit.csv | python3 mapper.py | sort | python3 reducer.py"
).read()

lines = [line.strip().replace("\n", "") for line in result.split("\n")]

expected = """credit_history	1
critical	293
delayed	88
fully repaid	40
fully repaid this bank	49
repaid	530
""".split(
    "\n"
)

if len(lines) != len(expected):
    raise Exception("Wrong number of lines")

for solution, expected in zip(lines, expected):
    assert solution == expected, f"Expected: {expected}\nGot: {solution}"
