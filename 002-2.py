#!/bin/python3

import math
import os
import random
import re
import sys

# better version of mine, but not sure would it timeout 
# O(n^2)

#
# Complete the 'shortestSubstring' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING givenString as parameter.
#

def shortestSubstring(givenString):
    # Write your code here
    u_set = set()
    for i in givenString:
      u_set.add(i)

    shortest = None
    for i in range(len(givenString)):
      # start from at least the length of all uniq chars
      for j in range(i+len(u_set), len(givenString)+1):
        # skip the rest if the extended string length is equal than the current shortest
        if shortest and len(givenString[i:j]) == shortest:
          break
        Done_chk = False
        uc_set = u_set.copy()
        for k in givenString[i:j]:
          if k in uc_set:
            uc_set.remove(k)
          if not uc_set:
            Done_chk = True
            break
        if Done_chk:
          # No need to continue extending the j if the first matched string has been found
          if not shortest or len(givenString[i:j]) < shortest:
            shortest = len(givenString[i:j])
            print(f'{givenString[i:j]} length {shortest}')
          if shortest == len(u_set):
            return shortest
          break

    return shortest

    # print(a)  

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # givenString = input()

    # result = shortestSubstring(givenString)

    # fptr.write(str(result) + '\n')

    # fptr.close()

  # shortestSubstring('abcddsf')
  shortestSubstring('aaabcdsf')  