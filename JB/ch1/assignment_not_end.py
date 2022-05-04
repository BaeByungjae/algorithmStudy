from collections import deque
import sys

n = int(input())

scores = deque()
times = deque()
total = 0

for i in range(n) :
    tf = list(map(int, sys.stdin.readline().split()))

    if tf[0] == 1 :
        scores.append(tf[1])
        times.append(tf[2])
    
    if len(times) > 0 :
        times[-1] -= 1
        if times[-1] == 0 :
            times.pop()
            score = scores.pop()
            total += score

print(total)