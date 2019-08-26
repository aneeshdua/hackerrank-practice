#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    #print(a)
    a.sort()
    maxm=0
    for i in range(0,len(a)):
        m=1
        for j in range(i+1,len(a)):
            #print(a[j])
            if(abs(a[i]-a[j])<=1):
                #print(m)
                m+=1
            else:
                break
        if(m>maxm and m != 1):
            maxm=m
    return maxm                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    #a = list((input().rstrip().split()))
    a = list(map(int, input().rstrip().split()))
    result = pickingNumbers(a)
    fptr.write(str(result) + '\n')
    fptr.close()
