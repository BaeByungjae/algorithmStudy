import sys

def input():
    return sys.stdin.readline().rstrip()

n=int(input())

cnt=666

ans=1

while True:
    if n==ans:
        print(cnt)
        break
    cnt+=1
    if '666'in str(cnt):
        ans+=1


