import os
from inputreader import aocinput
from typing import List


def syntaxScore(data: List[str]) -> [int, int]:
    syntax = {'<': '>',
              '(': ')',
              '[': ']',
              '{': '}'}
    scoreDict1 = {')': 3,
                  ']': 57,
                  '}': 1197,
                  '>': 25137}
    scoreDict2 = {')': 1,
                  ']': 2,
                  '}': 3,
                  '>': 4}
    score1 = 0
    score2 = []
    for line in data:
        stack = []
        for char in line.strip():
            if char in syntax.values():
                if not stack or char != syntax[stack.pop()]:
                    score1 += scoreDict1[char]
                    break
            else:
                stack.append(char)
        else:
            tempscore = 0
            for char in reversed(stack):
                tempscore *= 5
                tempscore += scoreDict2[syntax[char]]
            score2.append(tempscore)
    return score1, sorted(score2)[int(len(score2)/2)]


def main(day):
    data = aocinput(day)
    result = syntaxScore(data)
    print(result)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
