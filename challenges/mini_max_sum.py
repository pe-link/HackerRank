#!/bin/python3

def miniMaxSum(arr):
    min_list = []
    max_list = []

    for i in arr:
        min_list.append(i)
        max_list.append(i)

    number_min_list = min(min_list)
    number_max_list = max(max_list)
    min_list.remove(number_min_list)
    max_list.remove(number_max_list)

    list_numbers = sorted([sum(min_list), sum(max_list)])
    print(list_numbers[0], list_numbers[1])


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)