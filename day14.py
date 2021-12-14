import os
from inputreader import aocinput
from typing import List
from collections import defaultdict


def commonElement(data: List[str], steps: int) -> int:
    start = data[0].strip()
    pairCount = defaultdict(int)
    for i in range(len(start)-1):
        pairCount[start[i] + start[i+1]] += 1

    translations = {}
    for line in data[2:]:
        original, insertion = line.strip().split(' -> ')
        translations[original] = [original[0] + insertion, insertion + original[1]]

    for _ in range(steps):
        newCount = defaultdict(int)
        for pair, count in pairCount.items():
            for newPair in translations[pair]:
                newCount[newPair] += count
        pairCount = newCount

    elementCount = defaultdict(int)
    for pair, count in pairCount.items():
        for element in pair:
            elementCount[element] += count/2  # divide by 2 since elements are part of two pairs
    elementCount[start[0]] += 1  # add start and end elements since they wont be counted twice
    elementCount[start[-1]] += 1

    return int(max(elementCount.values()) - min(elementCount.values()))




def main(day):
    data = aocinput(day)
    result = commonElement(data, 10)
    result2 = commonElement(data, 40)
    print(result, result2)

if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
