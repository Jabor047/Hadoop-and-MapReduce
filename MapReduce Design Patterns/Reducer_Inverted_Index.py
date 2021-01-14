#!/usr/bin/python
import sys

count = 0
oldKey = None

for line in sys.stdin:
    dataMapped = line.strip().split('\t')
    if len(dataMapped) != 2:
        continue

    thisKey, thisValue = dataMapped

    # if thisKey == "fantastically":
    #     print(thisKey, "\t", thisValue)

    if oldKey and thisKey != oldKey:
        if oldKey == "fantastic":
            print oldKey, "\t", count

        oldKey = thisKey
        count = 0

    oldKey = thisKey
    count += 1

if oldKey != None:
    print oldKey, "\t", count
