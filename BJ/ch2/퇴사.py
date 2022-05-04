import sys

def input():
    return sys.stdin.readline().rstrip()

n=int(input())

arr=[[] for i in range(n+1)]


for i in range(1,n+1):
    t,p=map(int,input().split(' '))
    arr[i]=(t,p)

def solve(day,remain,money):
    if day==n:
        if remain>0:
            return 0
        return money
    
    result=solve(day+1,remain-1,money)
    if remain<=0:
        result=max(result,solve(day+1,arr[day+1][0]-1,money+arr[day+1][1]))
    return result

print(solve(0,0,0))