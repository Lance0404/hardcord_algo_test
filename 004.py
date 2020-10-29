#!/bin/python3

import math
import os
import random
import re
import sys

# wrong version done during the test

#
# Complete the 'getMinimumUniqueSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def getMinimumUniqueSum(arr):
    # Write your code here

    a = set()
    for i in arr:
        a.add(i)

    def getSum(b: str) -> int:
        ca = a.copy()
        dup_a = set()
        sum = 0
        while len(ca) and len(b):
            bb = b[0]
            if bb in ca:
                sum += bb
                ca.remove(bb)
                dup_a.add(bb)
                b.pop(0)
            elif bb in dup_a:
                while bb in a:
                    bb += 1
                sum += bb
                b.pop(0)
        return sum                

    minUniqSum = None
    for i in range(len(arr)):
        # cca = a.copy()
        for j in range(i+1, len(arr)+1):
            if len(arr[i:j]) < len(a):
                continue
            
            tmpSum = getSum(arr[i:j])
            print(arr[i:j], tmpSum)
            if not minUniqSum:
                minUniqSum = tmpSum
            elif tmpSum < minUniqSum:
                minUniqSum = tmpSum

                
    return minUniqSum

if __name__ == '__main__':
    getMinimumUniqueSum([3,1,2,2])