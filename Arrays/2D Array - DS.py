#!/bin/python3

def hourglassSum(arr):
	sums = []

	for row in range(1, 5):
		for col in range(1, 5):
			sum = arr[row][col] + arr[row-1][col-1] + arr[row-1][col] + arr[row-1][col+1] + arr[row+1][col-1] + arr[row+1][col] + arr[row+1][col+1]
			sums.append(sum)
	return max(sums)

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    print(str(result))
