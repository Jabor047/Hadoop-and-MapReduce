import sys

oldKey = None
count = 0
tagsLen = []

for line in sys.stdin:
    if len(line) == 1:
        continue

    thiskey = line

    if oldKey and oldKey != thiskey:
        tagsLen.append([count, oldKey])
        count = 0

    oldKey = thiskey
    count += 1

if oldKey is not None:
    tagsLen.append([count, oldKey])

top10 = sorted(tagsLen, reverse=True)[0:10]
top10 = sorted(top10, reverse=True)

for tag in top10:
    print(f"{tag[1]}\t{tag[0]}")
