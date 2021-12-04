import os
from inputreader import aocinput
from typing import List


class BingoCard:
    def __init__(self, numbers: List[str]):
        self.numberseries = []  # all rows and columns that can give bingo, diagonals don't count
        tempcolumns = [[] for _ in range(5)]
        for row in numbers:
            temprow = []
            for index, number in enumerate(row.split()):
                number = int(number)
                temprow.append(number)
                tempcolumns[index].append(number)
            self.numberseries.append(temprow)
        self.numberseries.extend(tempcolumns)

    def bingo(self, number: int) -> bool:
        for series in self.numberseries:
            if number in series:
                series.remove(number)
                if not series:  # if no numbers left, BINGO!
                    return True
        return False

    def getRemaining(self) -> int:
        return sum([sum(series) for series in self.numberseries[:5]])  # only first 5 to not count double


def playBingo(data: List[str]) -> [int, int]:
    numbers = [int(value) for value in data[0].split(',')]
    cards = []
    for i in range(0, int((len(data)-1)/6)):
        cards.append(BingoCard(data[2 + i * 6: 2 + i * 6 + 5]))  # separate numbers for each bingo card

    part1, part2 = None, None
    completedCards = []
    for number in numbers:
        for card in cards:
            if card.bingo(number):
                if not part1:  # only save score for part 1 the first time a card gets bingo
                    part1 = card.getRemaining() * number
                completedCards.append(card)
        for completedCard in completedCards:
            cards.remove(completedCard)
        completedCards.clear()
        if not cards:  # if last card is done
            part2 = card.getRemaining() * number
            break

    return part1, part2


def main(day):
    data = aocinput(day)
    result = playBingo(data)
    print(result)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
