#!/bin/python3

# incomplete solution!!

def minimumBribes(q):
    bribes = 0
    total_steps = 0
    too_chaotic = False
    for idx, itm in enumerate(q):
        steps = 0
        if itm > (idx+1):
            steps = q.index(itm-1) - q.index(itm)
            total_steps += steps
            if steps > 2:
                too_chaotic = True
                print("Too chaotic")
                break
    if too_chaotic == False:
        print(total_steps)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
