import sys

def input():
    return sys.stdin.readline().rstrip()

n,m=map(int,input().split(' '))

checkDict={}
ans=0

for i in range(n):
    s=input()
    checkDict[s]=1

for i in range(m):
    s=input()
    if s in checkDict:
        ans+=1
print(ans)
