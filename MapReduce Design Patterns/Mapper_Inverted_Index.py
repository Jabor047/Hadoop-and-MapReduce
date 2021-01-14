#!/usr/bin/python

import sys
import csv
import string

def mapper():
    reader = csv.reader(sys.stdin, delimiter='t')

    # replace all special characters with white space
    specialChars = ',.!?:;"()<>[]#$=-/'
    trans = string.maketrans(specialChars, ' ' * len(specialChars))
    for line in reader:
        body = line[4]
        nodeId = line[0]
        body = body.translate(trans)
        words = body.strip().split()
        for word in words:
            print "{0}\t{1}".format(word.lower(), nodeId)
