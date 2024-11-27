#!/bin/python3

import math
import os
import random
import re
import sys


def lonely_integer(a):
    new_array = []

    for i in range(len(a)):
        for j in range(len(a)):
            if i < j:
                if a[i] == a[j]:
                    new_array.append(a[i])

    for k in range(len(a)):
        if not a[k] in new_array:
            result = a[k]

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonely_integer(a)

    fptr.write(str(result) + '\n')

    fptr.close()
