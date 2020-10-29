#!/bin/python3

import math
import os
import random
import re
import sys

# should be correct!

#
# Complete the 'getMinimumUniqueSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def getMinimumUniqueSum(arr):
    # Write your code here
    
    minUniqSum = 0
    uniq_set = set()
    for i in arr:
        if i not in uniq_set:
            uniq_set.add(i)
        else:
            while i in uniq_set:
                i += 1
            else:
                uniq_set.add(i)
        print(f'sum {minUniqSum} add {i}')
        minUniqSum += i
    print(f'minUniqSum {minUniqSum}')        
    return minUniqSum

if __name__ == '__main__':
    getMinimumUniqueSum([3,1,2,2])