#!/bin/python3

import math
import os
import random
import re
import sys

# Joe's version

def countGroups(related):

    unvisited = set()
    bucket = dict() # key: each person, value: a set of known people
    for i in range(len(related)):
      unvisited.add(i)
      for j in range(len(related[i])):
        # print(f'{i} {j}: {related[i][j]}')
        if int(related[i][j]) == 1:    
          bucket.setdefault(i, set())
          bucket[i].add(j)

    print(f'bucket {bucket}')
    print(f'unvisited {unvisited}')
    visited_queue = list()
    group_cnt = 0
    # try to empty the unvisited set
    while unvisited:
      visit = unvisited.pop()
      visited_queue.append(visit)
      # use a queue to walk through all the knowns of the knowns
      while visited_queue:
        for i in bucket[visited_queue.pop(0)]:
          # skip self, don't revisit
          if i == visit:
            continue
          if i in unvisited:
            unvisited.remove(i)
            visited_queue.append(i)
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
  countGroups(['1100', '1110', '0110', '0001'])

# case 2
# 11000
# 11100
# 01100
# 00011
# 00011  

  countGroups(['11000', '11100', '01100', '00011', '00011'])

# case 3
# 10110
# 01010
# 10110
# 11110
# 00001

# 2,0
# 3,0
# 3,1
# 3,2
# --
# 2,1
# 1,0

  countGroups(['10110', '01010', '10110', '11110', '00001'])


