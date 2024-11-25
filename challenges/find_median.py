#!/bin/python3

import os

def findMedian(arr):
    new_array = sorted(arr)
    if len(new_array) % 2 == 0:
        a = len(new_array) / 2
        b = (len(new_array) / 2) - 1
        result = float((new_array[int(a)] + new_array[int(b)]) / 2)
    else:
        a = ((len(new_array) + 1) / 2) - 1
        result = int(new_array[int(a)])
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
