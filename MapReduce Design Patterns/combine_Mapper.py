#! usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter="\t")
writer = csv.writer(sys.stdout, delimiter="\t")

reader.next()

for line in reader:
    