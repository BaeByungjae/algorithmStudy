import sys
import itertools

def input():
    return sys.stdin.readline().rstrip()

n=int(input())

num=''.join([str(i) for i in range(1,n+1)])

iter=itertools.permutations(num,n)

for data in iter:
    for num in data:
        print(num,end=' ')
    print()
