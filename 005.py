#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countGroups' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY related as parameter.
#

def countGroups(related):
    # Write your code here

    # store the ones that are underneath the diagonal line
    # if choosen this half, then left val > right val 
    one_set = set()
    bucket = dict() # key: each person, value: a set of known people
    for i in range(len(related)):
      # print(related[i])
      for j in range(i):
        print(f'{i} {j}: {related[i][j]}')
        if int(related[i][j]) == 1:
          one_set.add((i,j))
          bucket.setdefault(i, set())
          bucket.setdefault(j, set())
          bucket[i].add(j)
          bucket[j].add(i)          

    print(f'one_set before transitive: {one_set}')
    print(bucket)

    # handle the transtive
    # if (i, a) and (b, i) are true, then (a, b) should also be true
    for i in bucket.values():
      i_lst = sorted(list(i), reverse=True) 
      for j in range(len(i_lst)-1):
        for k in range(j+1, len(i_lst)):
          # print((i_lst[j],i_lst[k]))
          one_set.add((i_lst[j],i_lst[k]))

    print(f'one_set after transitive: {one_set}')

    group_cnt = 0
    while len(one_set):
      a_queue = list()
      a_queue.append(one_set.pop())
      # check all its adjacent cells, till all of its adjacent cells get removed from one_set
      while len(a_queue):
        x, y = a_queue.pop(0)
        for i in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
          if i in one_set:
            one_set.remove(i)
            a_queue.append(i)
      else:
        group_cnt += 1

    print(f'group_cnt {group_cnt}')
    return group_cnt

if __name__ == '__main__':

# case 1
# 1100
# 1110
# 0110
# 0001  
#   countGroups(['1100', '1110', '0110', '0001'])

# case 2
# 11000
# 11100
# 01100
# 00011
# 00011  

  countGroups(['11000', '11100', '01100', '00011', '00011'])