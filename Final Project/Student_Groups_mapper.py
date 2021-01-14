import sys
import csv

reader = csv.reader(sys.stdin, delimiter="\t")

reader.__next__()

for line in reader:
    if len(line) == 19:
        nodeId = line[0]
        authorId = line[3]
        nodeType = line[5]
        questionId = line[7]

        if nodeType == "question":
            print(f"{nodeId}\t{authorId}")
        else:
            print(f"{questionId}\t{authorId}")
