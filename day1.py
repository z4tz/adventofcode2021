from inputreader import aocinput


def depthincreases(depths, offset=1):
    return sum([depths[i] < depths[i+offset] for i in range(len(depths)-offset)])


def main(day):
    data = aocinput(day)
    data = [int(line) for line in data]
    print(depthincreases(data))
    print(depthincreases(data, 3))


if __name__ == '__main__':
    main(int(__file__.split('/')[-1][3:-3]))