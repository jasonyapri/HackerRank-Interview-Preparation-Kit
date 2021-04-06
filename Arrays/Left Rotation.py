#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(arr, d):
	new_arr = []
	position = d
	for i in range(len(arr)):
		if (position >= len(arr)):
			position = position - len(arr)
		new_arr.append(arr[position])
		position += 1
	return new_arr

if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])
    d = int(nd[1])
    arr = list(map(int, input().rstrip().split()))
    result = rotLeft(arr, d)

    print(' '.join(map(str, result)))