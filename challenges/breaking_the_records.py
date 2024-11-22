#!/bin/python3

import math
import os
import random
import re
import sys

def breakingRecords(scores):
    first_max = scores[0]
    first_min = scores[0]
    max_count = 0
    min_count = 0

    for i in range(len(scores)):
        if scores[i] > first_max:
            first_max = scores[i]
            max_count += 1
        if scores[i] < first_min:
            first_min = scores[i]
            min_count += 1

    return[max_count, min_count]
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
