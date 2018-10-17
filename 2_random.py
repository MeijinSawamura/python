#Math functions, importing modules, None, end, sep
#loops, break, continue

import random, os, sys, math #Or can do 'from random import *'

def randomNo(low, high):
    no1 = random.randint(low, high)
    no2 = random.randint(low, high)

    print('The 2 numbers are: ')
    print(no1)
    print(no2)

    print()
    print('Format 2')
    print('The 2 numbers are: ', end=' ')
    print(str(no1), end=' and ')
    print(str(no2))

    print()
    print('Format 3')
    print('Numbers:')
    print(str(no1), str(no2), sep=', ')

print('Select thresholds and we will give you 2 random numbers!')
print()
          
while True:
    print('Enter lower threshold.')
    low = int(input())
    print('Enter higher threshold.')
    high = int(input())
    if low<high :
        break;
    else :
        continue;

randomNo(low, high)
