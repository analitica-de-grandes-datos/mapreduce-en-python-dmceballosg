#
import os

result = os.popen("cat data.csv | python3 mapper.py | sort | python3 reducer.py").read()

lines = [line.strip().replace("\n", "") for line in result.split("\n")]

expected = """A   1990-07-22   0
A   1990-09-26   8
A   1992-09-19   9
A   1990-10-06   10
A   1990-09-05   11
A   1990-08-31   12
A   1997-12-15   13
A   1994-10-25   14
A   1993-01-11   15
A   1992-08-22   16
A   1993-05-08   17
A   1988-04-27   121
B   1995-08-23   1
B   1991-10-01   9
B   1999-10-21   13
B   1997-04-09   14
B   1995-09-06   15
B   1993-03-02   16
B   1999-08-28   17
B   1994-08-30   18
B   1999-06-11   121
B   1998-11-22   131
C   1994-01-25   10
C   1991-02-12   13
C   1994-09-09   15
C   1994-07-27   104
D   1990-10-10   15
E   1998-09-14   2
E   1995-04-25   3
E   1993-07-21   4
E   1993-01-27   9
E   1994-02-14   10
E   1999-09-10   11
E   1999-12-06   12
E   1999-01-14   15
E   1990-05-03   16
E   1985-02-12   17
E   1990-02-09   18
E   1993-12-27   19
E   1991-02-18   141
""".split(
    "\n"
)

if len(lines) != len(expected):
    raise Exception("Wrong number of lines")

for solution, expected in zip(lines, expected):
    assert (
        solution.strip() == expected.strip()
    ), f"Expected: {expected}\nGot: {solution}"
