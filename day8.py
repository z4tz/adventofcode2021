import os
from inputreader import aocinput
from typing import List, Dict


def countDigits(data: List[str]) -> int:
    return sum((sum(len(word) in [2, 3, 4, 7] for word in line.split('|')[1].split()) for line in data))


def identifyDigits(patternstring: str) -> Dict[str, str]:
    digitDict = {}
    patterns = [set(pattern) for pattern in patternstring.split()]  # sets are easier to compare (issubset)
    for pattern in patterns[:]:
        match len(pattern):
            case 2:
                digitDict['1'] = pattern
                patterns.remove(pattern)
            case 3:
                digitDict['7'] = pattern
                patterns.remove(pattern)
            case 4:
                digitDict['4'] = pattern
                patterns.remove(pattern)
            case 7:
                digitDict['8'] = pattern
                patterns.remove(pattern)

    for pattern in patterns[:]:
        if len(pattern) == 5:
            if digitDict['1'].issubset(pattern):
                digitDict['3'] = pattern
                patterns.remove(pattern)
            elif digitDict['4'].difference(digitDict['1']).issubset(pattern):  # 4 diff 1 gives middle and top left
                digitDict['5'] = pattern
                patterns.remove(pattern)
            else:
                digitDict['2'] = pattern
                patterns.remove(pattern)
        elif len(pattern) == 6:
            if digitDict['4'].issubset(pattern):
                digitDict['9'] = pattern
            elif digitDict['4'].difference(digitDict['1']).issubset(pattern):  # 4 diff 1 gives middle and top left
                digitDict['6'] = pattern
            else:
                digitDict['0'] = pattern
    return {''.join(sorted(list(pattern))): digit for digit, pattern in digitDict.items()}  # invert dict and convert pattern into strings again


def countAllDigits(data: List[str]) -> int:
    total = 0
    for line in data:
        parts = line.strip().split('|')
        digitDict = identifyDigits(parts[0])
        total += int(''.join([digitDict[''.join(sorted(word))] for word in parts[1].split()]))
    return total


def main(day: int):
    data = aocinput(day)
    result = countDigits(data)
    result2 = countAllDigits(data)
    print(result, result2)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
