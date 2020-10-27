#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'shortestSubstring' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING givenString as parameter.
#

def shortestSubstring(givenString):
    # Write your code here
    a = set()
    for i in givenString:
      a.add(i)

    def hasAllChar(b: str):
      aa = a.copy()
      for i in b:
        if i in aa:
          aa.remove(i)
        if len(aa) == 0:
          return True    
      return False

    # a.remove('a')
    print(len(a))
    shortest = None
    for i in range(len(givenString)):
      for j in range(i+1, len(givenString)+1):
        # print(givenString[i:j])
        if len(givenString[i:j]) < len(a):
          continue
        if hasAllChar(givenString[i:j]):
          if len(givenString[i:j]) == len(a):
            return len(givenString[i:j])
          else:
            if not shortest:
              shortest = len(givenString[i:j])
            elif (len(givenString[i:j]) < shortest):
              shortest = len(givenString[i:j])
    return shortest

    # print(a)  

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # givenString = input()

    # result = shortestSubstring(givenString)

    # fptr.write(str(result) + '\n')

    # fptr.close()

  shortestSubstring('abcddsf')