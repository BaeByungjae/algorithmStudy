import sys

n, m = map(int, sys.stdin.readline().split())

result = []

def solution(depth) :
    if depth == m :
        print(" ".join(map(str, result)))
        return  

    for j in range(n) :
        if len(result) == 0 or j+1 >= result[-1]:
            result.append(j+1)
            solution(depth+1)
            result.pop()
        
solution(0)