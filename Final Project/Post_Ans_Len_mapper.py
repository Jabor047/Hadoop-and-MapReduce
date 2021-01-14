import sys
import csv

reader = csv.reader(sys.stdin, delimiter="\t")

reader.__next__()

question = {}
answer = {}
lenList = []

for line in reader:
    if len(line) == 19:
        nodeId = line[0]
        post = line[4]
        nodeType = line[5]
        questionId = str(line[7])
        postLen = len(post)

        # check if post is a question, save in dict
        if nodeType == "question":
            question[nodeId] = postLen

        # check if post is answer and whether it has mutliple answers
        if nodeType == "answer":
            if questionId not in answer:
                answer[questionId] = [postLen]
            else:
                answer[questionId].append(postLen)

# check if a question has been answered and print the length of both question and answer
for Id in question:
    if Id not in answer:
        print(f"{int(Id)}\t{int(question[Id])}\t{0}")
    else:
        for length in answer[Id]:
            print(f"{int(Id)}\t{question[Id]}\t{length}")
