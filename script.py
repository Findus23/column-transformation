from pathlib import Path
from sys import argv

inputfile = Path(argv[1])
outputfile = Path(argv[2])

counter = {}

with inputfile.open() as ip:
    next(ip)  # skip the first line
    for line in ip:  # go through all lines
        columns = line.split("\t")
        value = int(columns[1])
        names = columns[0].split("|")
        for name in names:
            if name not in counter:
                # if this is the first time the name showed up,
                # set the counter to the value
                counter[name] = value
            else:
                # otherwise increase it by the value
                counter[name] += value
print(counter)

with outputfile.open("w") as wf:
    for name, count in counter.items():
        wf.write(f"{name};{count}\n")  # Cinema;4
