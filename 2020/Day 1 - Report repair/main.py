from operator import mul
from functools import reduce
from argparse import ArgumentParser

argumentParser = ArgumentParser()
argumentParser.add_argument("-t", "--total", type=int, default=2020,
                            help="The total number to be reached")
argumentParser.add_argument("-c", "--count", type=int, default=2,
                            help="The number of elements to sum in order to get total")


def find_numbers_that_add_up_to(count, total, numbers, index=0):
    for index in range(index, len(numbers)):
        number = numbers[index]
        if number > total:
            continue
        elif count == 1 and number == total:
            return [number]
        else:
            result = find_numbers_that_add_up_to(count - 1, total - number,
                                                 numbers, index + 1)
            if result is not None:
                result.append(number)
                return result
    return None


fileData = [int(x) for x in open("input.txt", "r").readlines()]
arguments = argumentParser.parse_args()
numbersFound = find_numbers_that_add_up_to(arguments.count,
                                           arguments.total, fileData)
print("Result of numbers' multiplication is ",
      f"{reduce(mul, numbersFound, 1)}")
