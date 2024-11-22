#!/bin/python3

def plusMinus(arr):
    count_negative_values = 0
    count_positive_values = 0
    count_zero_values = 0
    for i in arr:
        if i == 0:
            count_zero_values += 1
        elif i > 0:
            count_positive_values += 1
        else:
            count_negative_values += 1
    print(round(count_positive_values / len(arr), 5))
    print(round(count_negative_values / len(arr), 5))
    print(round(count_zero_values / len(arr), 5))

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
