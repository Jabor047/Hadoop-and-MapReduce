import csv
import sys

reader = csv.reader(sys.stdin, delimiter="\t")

reader.__next__()

for line in reader:
    if len(line) == 19:
        authorId = line[3]
        hour = int(line[8][11:13])
        print(f'{authorId}\t{hour}')
