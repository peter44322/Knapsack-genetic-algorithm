#! /usr/bin/env python

import sys
from Item import Item
from Algorithm import Algorithm

filePath = sys.argv[1]

with open(filePath, "r") as file:
    text = file.read()

testCases = text.split("\n\n")

for i in range(1, int(testCases[0])):
    case = testCases[i].strip().split("\n")
    # print(case)

    items = []
    for item in case[2:]:
        weight, value = item.split(" ")
        items.append(Item(int(weight), int(value)))

    size = case[1]

    # print(size)
    al = Algorithm(items, size)
    al.evolve()

    print("caseId :", i, al.bestEver.fitness())
