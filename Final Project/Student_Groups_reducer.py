import sys

oldKey = None
Id = []

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue

    thisKey, thisId = data

    if oldKey and oldKey != thisKey:
        print(f"{oldKey}\t{Id}")
        Id = []

    oldKey = thisKey
    Id.append(thisId)

if oldKey is not None:
    print(f"{oldKey}\t{Id}")
