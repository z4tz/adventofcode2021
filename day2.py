import os
from inputreader import aocinput
from typing import List


def calcPosition(instructions: List[str]) -> int:
    pos = 0
    depth = 0
    for instruction in instructions:
        match instruction[0]:
            case 'f':
                pos += int(instruction[-1])
            case 'd':
                depth += int(instruction[-1])
            case 'u':
                depth -= int(instruction[-1])
            case _:
                print(f'invalid instruction: {instruction}')
                exit()
    return pos*depth


def calcPosition2(instructions: List[str]) -> int:
    pos = 0
    aim = 0
    depth = 0
    for instruction in instructions:
        match instruction[0]:
            case 'f':
                forward = int(instruction[-1])
                pos += forward
                depth += aim * forward
            case 'd':
                aim += int(instruction[-1])
            case 'u':
                aim -= int(instruction[-1])
            case _:
                print(f'invalid instruction: {instruction}')
                exit()
    return pos*depth


def main(day):
    data = aocinput(day)
    data = [line.strip() for line in data]
    result = calcPosition(data)
    result2 = calcPosition2(data)
    print(result, result2)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
