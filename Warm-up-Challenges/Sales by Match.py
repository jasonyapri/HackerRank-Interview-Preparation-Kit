#!/bin/python3

import math
import os
import random
import re
import sys

def unique(list1):
    # insert the list to the set
    list_set = set(list1)
    # convert the set to the list
    unique_list = (list(list_set))
    return unique_list

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = 0
    unique_list = unique(ar)
    for item in unique_list:
        count = ar.count(item)
        pairs += count //2
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
