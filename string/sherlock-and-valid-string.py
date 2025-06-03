#!/bin/python3

import math
import os
import random
import re
import sys
import collections
#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    m = collections.defaultdict(int)
    for x in s:
        m[x] += 1
    count = collections.defaultdict(int)
    for _, v in m.items():
        count[v] += 1
    if len(count) > 2:
        return "NO"
    if len(count) < 2:
        return "YES"
    if 1 in count.keys() and count[1] == 1:
        return "YES"
    if count[max(count.keys())] > 1 or max(count.keys())-1 != min(count.keys()):
        return "NO"
    return "YES"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
