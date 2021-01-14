import sys

oldAuthor = None
hourCount = [0] * 24

for line in sys.stdin:
    dataMapped = line.strip().split("\t")

    if len(dataMapped) != 2:
        continue

    thisAuthor, thisHour = dataMapped

    if oldAuthor and oldAuthor != thisAuthor:
        for hour, count in enumerate(hourCount):
            if count == max(hourCount):
                print(f"{oldAuthor}\t{hour}")

        hourCount = [0] * 24

    oldAuthor = thisAuthor
    hourCount[int(thisHour)] += 1

if oldAuthor is not None:
    for hour, count in enumerate(hourCount):
        if count == max(hourCount):
            print(f"{oldAuthor}\t{hour}")
