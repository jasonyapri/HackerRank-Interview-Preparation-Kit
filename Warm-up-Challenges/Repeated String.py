#!/bin/python3

def repeatedString(s, n):
	occurence = n // len(s)
	occurence_additional = n % len(s)
	return (s.count('a') * occurence) + s[:occurence_additional].count('a')

if __name__ == '__main__':

	s = input()
	n = int(input())
	result = repeatedString(s, n)

	print(str(result))