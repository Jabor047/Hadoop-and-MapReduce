#! usr/bin/python
import sys

oldKey = None
count = 0
totalSales = 0

for line in sys.stdin:
    dataMapped = line.strip().split('\t')
    if len(dataMapped) != 2:
        continue

    thisKey, thisValue = dataMapped

    if oldKey and thisKey != oldKey:
        print oldKey, "\t", float(totalSales / count)

        oldKey = thisKey
        count = 0
        totalSales = 0

    oldKey = thisKey
    count += 1
    totalSales += float(thisValue)

if oldKey != None:
    print oldKey, "\t", float(totalSales/count)