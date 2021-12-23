import os
from inputreader import aocinput
from typing import List
from collections import defaultdict


def diceSum():
    firstThrow = 1
    while True:
        yield firstThrow * 3 + 3
        firstThrow += 3


def dicegame(data: List[str]) -> int:
    positions = [int(line.split(':')[-1]) - 1 for line in data]
    scores = [0, 0]

    activeplayer = 0
    dicegenertor = diceSum()
    while max(scores) < 1000:
        positions[activeplayer] = (positions[activeplayer] + next(dicegenertor)) % 10
        scores[activeplayer] += positions[activeplayer] + 1
        activeplayer = not activeplayer
    return int(min(scores) * (((next(dicegenertor) - 3) / 3) - 1))


def quantumDiceSums():
    """Count outcomes from rolling 3 d3"""
    results = defaultdict(int)
    for a in range(1, 4):
        for b in range(1, 4):
            for c in range(1, 4):
                results[a+b+c] += 1
    return results


def quantumDiceGame(data: List[str]) -> int:
    gameStates = defaultdict(int)  # key:(pos1, pos2, score1, score2)
    gameStates[(*[int(line.split(':')[-1]) - 1 for line in data], 0, 0)] = 1
    activeplayer = 0
    wins = [0, 0]
    diceResults = quantumDiceSums()

    while gameStates:
        newGameStates = defaultdict(int)
        for gameState, statecount in gameStates.items():
            for dievalue, dievaluecount in diceResults.items():
                newGameState = list(gameState)
                newGameState[activeplayer] = (gameState[activeplayer] + dievalue) % 10  # new position
                newScore = gameState[activeplayer + 2] + newGameState[activeplayer] + 1
                if newScore >= 21:
                    wins[activeplayer] += statecount * dievaluecount
                    continue
                newGameState[activeplayer+2] = newScore  # new score
                newGameStates[tuple(newGameState)] += statecount * dievaluecount
        gameStates = newGameStates
        activeplayer = not activeplayer

    return max(wins)


def main(day):
    data = aocinput(day)
    result = dicegame(data)
    result2 = quantumDiceGame(data)
    print(result, result2)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
