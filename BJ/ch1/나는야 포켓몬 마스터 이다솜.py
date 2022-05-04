import sys

def input():
    return sys.stdin.readline().rstrip()

n,m=map(int,input().split(' '))

dict={}

for i in range(n):
    pock=input()
    dict[pock]=str(i+1)
    dict[str(i+1)]=pock

for i in range(m):
    print(dict[input()])