import sys

oldKey = None
oldquestionLen = None
count = 0
totalAnsLen = 0

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 3:
        continue

    thisKey, questionLen, answerLen = data

    if oldKey and oldKey != thisKey:
        print(f"{oldKey}\t{oldquestionLen}\t{totalAnsLen / float(count)}")

        count = 0
        totalAnsLen = 0

    oldKey = thisKey
    oldquestionLen = questionLen
    totalAnsLen += int(answerLen)
    count += 1

if oldKey is not None:
    print(f"{oldKey}\t{oldquestionLen}\t{totalAnsLen / count}")
