#!/bin/python3

import math
import os
import random
import re
import sys


def divisible_sum_pairs(n, k, ar):
    divisible_numbers_count = 0

    for i in range(n):
        for j in range(n):
            if i < j:
                sum_pairs = ar[i] + ar[j]
                if sum_pairs % k == 0:
                    divisible_numbers_count += 1

    return divisible_numbers_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisible_sum_pairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
