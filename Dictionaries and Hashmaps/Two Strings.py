#!/bin/python3

def twoStrings(s1, s2):
	for char in s1:
		if char in s2:
			return 'YES'
			break;

	return 'NO'

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s1 = input()
        s2 = input()
        result = twoStrings(s1, s2)

        print(result)
