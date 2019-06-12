import math
import os
import random
import re
import sys

def hourglassSum(arr):
    maxVal=-9999
    for i in range(0,4):
        for j in range(0,4):
            firstRow = arr[i][j]+arr[i][j+1]+arr[i][j+2]
            thirdRow=  arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            secondRow= arr[i+1][j+1]
            total=firstRow+secondRow+thirdRow
            maxVal=max(maxVal,total)
    return (maxVal)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
