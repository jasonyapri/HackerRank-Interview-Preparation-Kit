#!/bin/python3
from collections import Counter

def freqQuery(queries):
	answer = []
	arr = []
	for item in queries:
		if item[0] == 1:
			arr.append(item[1])
		elif item[0] == 2:
			if item[1] in arr:
				arr.remove(item[1])
		elif item[0] == 3:
			occurence = Counter(arr).values()
			if item[1] in occurence:
				answer.append(1)
			else:
				answer.append(0)
	return answer

if __name__ == '__main__':

    q = int(input().strip())

    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    print('\n'.join(map(str, ans)))
