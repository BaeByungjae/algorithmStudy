import sys

def input():
    return sys.stdin.readline().rstrip()

N,M,B=map(int,input().split(' '))

arr=[[int(x) for x in input().split(' ')] for i in range(N)]

ans_t=1000000000000000000000000000000
ans_h=0

for i in range(257):
    time=0
    b=B
    for n in range(N):
        for m in range(M):
            if arr[n][m]==i:
                continue
            elif arr[n][m]>i:
                cnt=arr[n][m]-i
                time+=(cnt*2)
                b+=cnt
            else:
                cnt=i-arr[n][m]
                time+=cnt
                b-=cnt
            if b<0:
                continue
    if b<0:
        break
    if ans_t>=time:
        ans_t=time
        ans_h=i

print(ans_t,ans_h)