import sys

def input():
    return sys.stdin.readline().rstrip()

n=int(input())

arr=[0 for _ in range(n)]
ans=0

def check(level) :
    for i in range(level) :
        if arr[i] == arr[level] or abs(arr[level] - arr[i]) == abs(level - i) :
            return False

    return True

def solve(chess):
    global ans
    if chess==n:
        ans+=1
        return
    for i in range(n):
        arr[chess]=i
        if check(chess):
            solve(chess+1)

solve(0)

print (ans)        
    