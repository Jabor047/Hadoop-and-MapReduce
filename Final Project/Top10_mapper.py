import sys
import csv

reader = csv.reader(sys.stdin, delimiter="\t")

reader.__next__()

tags = []

for line in reader:
    if len(line) == 19:
        tag = line[2].split(" ")
        nodeType = line[5]

        if nodeType == "question":
            tags.extend(tag)

for tagname in tags:
    print(tagname)
