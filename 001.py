#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'numDuplicates' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY name
#  2. INTEGER_ARRAY price
#  3. INTEGER_ARRAY weight
#

def numDuplicates(name, price, weight):
    # Write your code here
    a = set()
    cnt = 0
    for i in range(len(name)):
        if (name[i], price[i], weight[i]) not in a:
            a.add((name[i], price[i], weight[i])) 
        else:
            cnt+=1
    return cnt

    

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    name_count = int(input().strip())

    name = []

    for _ in range(name_count):
        name_item = input()
        name.append(name_item)

    price_count = int(input().strip())

    price = []

    for _ in range(price_count):
        price_item = int(input().strip())
        price.append(price_item)

    weight_count = int(input().strip())

    weight = []

    for _ in range(weight_count):
        weight_item = int(input().strip())
        weight.append(weight_item)

    result = numDuplicates(name, price, weight)

    fptr.write(str(result) + '\n')

    fptr.close()
