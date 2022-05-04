import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n=int(input())

q=deque([i+1 for i in range(n)])

while len(q)>1:
    q.popleft()
    if len(q)==1:
        break
    tmp=q.popleft()
    q.append(tmp)

print(q.popleft())