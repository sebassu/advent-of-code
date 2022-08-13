from hashlib import md5
from itertools import count
from argparse import ArgumentParser

argumentParser = ArgumentParser()
argumentParser.add_argument("-z", "--zeroesCount", type=int, default=5,
                            help="The number of zero (0) characters expected as a prefix")
expectedPrefix = '0' * argumentParser.parse_args().zeroesCount
for number in count():
    result = md5(f"ckczppom{number}".encode()).hexdigest()
    if result.startswith(expectedPrefix):
        print(f"Smallest number found: {number}")
        break
