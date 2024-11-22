#!/bin/python3

def timeConversion(s):
    x = s.split(":")
    hour = x[0]
    min = x[1]
    
    if x[2][-2] == 'P':
        if hour == '12':
            hour = '12'
        else: 
            hour = int(hour) + 12
        sec = x[2].replace('PM', '')
    else:
        if hour == '12':
            hour = '00'
        sec = x[2].replace('AM', '')

    print(f'{hour}:{min}:{sec}')

if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
