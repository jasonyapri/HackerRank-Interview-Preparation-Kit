#!/bin/python3

def countingValleys(steps, path):
	valley = 0
	current_level = 0
	for step in path:
		if step == 'U': current_level += 1
		if step == 'D': current_level -= 1

		if current_level == 0 and step == 'U':
			valley += 1
	
	return valley
	

if __name__ == '__main__':
	steps = int(input().strip())

	path = input()
	result = countingValleys(steps, path)

	print(result)

