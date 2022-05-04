import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

melody,prep=map(int,input().split(" "))

stack=deque([] for i in range(melody))

ans=0


for i in range(melody):
    n,m=map(int,input().split())
    if len(stack[n-1]) == 0:
        stack[n - 1].append(m)
        ans += 1
    else:
        top=stack[n-1].pop()
        if top<m:
            stack[n-1].append(top)
            stack[n-1].append(m)
            ans+=1
        elif top==m:
            stack[n-1].append(top)
        else:
            while top>m and len(stack[n-1]):
                ans+=1
                top=stack[n-1].pop()
            if len(stack[n-1])==0 and top>m:
                ans+=1
            elif len(stack[n-1])==0:
                stack[n-1].append(top)
            else:
                stack[n-1].append(top)
            if top!=m:
                stack[n-1].append(m)
                ans+=1


print(ans)
