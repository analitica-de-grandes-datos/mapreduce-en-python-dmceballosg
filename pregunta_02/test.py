#
import os

result = os.popen(
    "cat credit.csv | python3 mapper.py | sort | python3 reducer.py"
).read()

lines = [line.strip().replace("\n", "") for line in result.split("\n")]

expected = """business	15945
car (new)	14896
car (used)	12976
domestic appliances	3990
education	12612
furniture	14179
others	18424
radio/tv	15653
repairs	11998
retraining	3447
""".split(
    "\n"
)

if len(lines) != len(expected):
    raise Exception("Wrong number of lines")

for solution, expected in zip(lines, expected):
    assert solution == expected, f"Expected: {expected}\nGot: {solution}"
