import sys

def input():
    return sys.stdin.readline().rstrip()

n,m=map(int,input().split(' '))

def solve(arr,length,now):
    if(length==m):
        for i in arr:
            print(i,end=' ')
        print()
        return
    if(now>n):
        return
    newArr=arr[:]
    newArr.append(now)
    solve(newArr,length+1,now+1)
    solve(arr,length,now+1)
    
solve([],0,1)