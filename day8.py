import os
from inputreader import aocinput
from typing import List, Dict


def countDigits(data: List[str]) -> int:
    return sum((sum(len(word) in [2, 3, 4, 7] for word in line.split('|')[1].split()) for line in data))


def identifyDigits(combination: str) -> Dict[str, str]:
    pass


def countAllDigits(data: List[str]) -> int:
    total = 0
    for line in data:
        parts = line.strip().split('|')
        digitDict = identifyDigits(parts[0])
        total += int(''.join([digitDict[word] for word in parts[1].split()]))
    return total


def main(day: int):
    data = aocinput(day)
    result = countDigits(data)
    print(result)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
