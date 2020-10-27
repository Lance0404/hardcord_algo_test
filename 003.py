#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMaxUnits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY boxes
#  2. LONG_INTEGER_ARRAY unitsPerBox
#  3. LONG_INTEGER truckSize
#

def getMaxUnits(boxes, unitsPerBox, truckSize):
    
    # start accumulate from the product with the highest units Per Box, but lowest boxes
    a = list()
    for i in range(len(boxes)):
      a.append((boxes[i], unitsPerBox[i]))

    # sort by second 
    sa = sorted(a, key=lambda tup: (-tup[1], tup[0]))

    maxu = 0
    while truckSize and len(sa):
      c = sa.pop(0)
      if c[0] <= truckSize:
        maxu += c[0] * c[1]
        truckSize -= c[0]

    return maxu
    
if __name__ == '__main__':
    getMaxUnits([1,2,3], [3,2,1], 3)
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # boxes_count = int(input().strip())

    # boxes = []

    # for _ in range(boxes_count):
    #     boxes_item = int(input().strip())
    #     boxes.append(boxes_item)

    # unitsPerBox_count = int(input().strip())

    # unitsPerBox = []

    # for _ in range(unitsPerBox_count):
    #     unitsPerBox_item = int(input().strip())
    #     unitsPerBox.append(unitsPerBox_item)

    # truckSize = int(input().strip())

    # result = getMaxUnits(boxes, unitsPerBox, truckSize)

    # fptr.write(str(result) + '\n')

    # fptr.close()
