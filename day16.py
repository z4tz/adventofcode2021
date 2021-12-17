import os
from inputreader import aocinput
from typing import List
import math

funcdict = {0: sum,
            1: math.prod,
            2: min,
            3: max,
            5: lambda x: int(x[0] > x[1]),
            6: lambda x: int(x[0] < x[1]),
            7: lambda x: int(x[0] == x[1])}


def sumVersions(data: List[str]) -> [int, int]:
    converted = bin(int(data[0], 16))[2:].zfill(len(data[0]*4))  # zfill to keep leading zeros
    versions = []

    def packetreader(start: int) -> [int, int]:
        versions.append(int(converted[start:start + 3], 2))
        typeID = int(converted[start + 3:start + 6], 2)
        if typeID == 4:  # literal value
            n = 0
            number = []
            while True:
                number.append(converted[start + 7 + n * 5:start + 7 + n * 5 + 4])
                if converted[start + 6 + n * 5] == '1':
                    n += 1
                else:
                    break
            return 6 + (n + 1) * 5, int(''.join(number), 2)
        else:  # operators
            if converted[start + 6] == '0':  # length id 0
                length = int(converted[start + 7: start + 7 + 15], 2)
                internalcurrent = start + 7 + 15
                internalValues = []
                while internalcurrent < start + 7 + 15 + length:
                    internallength, internalValue = packetreader(internalcurrent)
                    internalValues.append(internalValue)
                    internalcurrent += internallength
                return 7 + 15 + length, funcdict[typeID](internalValues)
            else:  # length id 1
                subpacketcount = int(converted[start + 7: start + 7 + 11], 2)
                internalcurrent = start + 7 + 11
                internalValues = []
                for _ in range(subpacketcount):
                    internallength, internalValue = packetreader(internalcurrent)
                    internalcurrent += internallength
                    internalValues.append(internalValue)
                return internalcurrent - start, funcdict[typeID](internalValues)

    _, value = packetreader(0)
    return sum(versions), value


def main(day):
    data = aocinput(day)
    result = sumVersions(data)
    print(result)


if __name__ == '__main__':
    main(int(os.path.basename(__file__)[3:-3]))
