import math
import os
import random
import re
import sys


def minimumSwaps(arr):
    swaps = 0
    for i in range(0,n-1):
        while arr[i] != i+1:
            t = arr[arr[i]-1]
            arr[arr[i]-1] = arr[i]
            arr[i] = t
            swaps += 1
    return swaps

    
    
fptr = open(os.environ['OUTPUT_PATH'], 'w')

n = int(raw_input())

arr = map(int, raw_input().rstrip().split())

res = minimumSwaps(arr)

fptr.write(str(res) + '\n')

fptr.close()
