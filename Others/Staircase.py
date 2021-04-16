#!/bin/python3

# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        print(' ' * (n-i-1), end='')
        print('#' * (i+1))
        

if __name__ == '__main__':
    n = int(input())

    staircase(n)
