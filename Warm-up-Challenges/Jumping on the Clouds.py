#!/bin/python3


def jumpingOnClouds(c):
	jump_count = 0
	jump = False
	steps = -1
	for index, item in enumerate(c):
		if (jump):
			jump = False
			continue
		if (index<(len(c)-2) and c[index+2]==0):
			jump = True
			jump_count += 1
		steps += 1
	return steps

if __name__ == '__main__':

	n = int(input())
	c = list(map(int, input().rstrip().split()))

	result = jumpingOnClouds(c)
	print(str(result))
