import random
import sys

from histogram.py import *


def get_random_word(histogram):
    word = random.choice(histogram)
    return word


if __name__ == "__main__":
    print(get_random_word(histogram))


