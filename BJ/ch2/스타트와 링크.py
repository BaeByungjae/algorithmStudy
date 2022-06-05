import sys

def input():
    return sys.stdin.readline().rstrip()

n=int(input())

# arr = [list(map(int, input().split(' '))) for _ in range(n)]

fir=[]
sec=[]

def solve():
    if len(fir)==n/2:
        print(fir)
    for i in range(n):
        if i not in fir:
            fir.append(i)
            solve()
            fir.pop()
solve()