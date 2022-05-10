import sys

n, m = map(int, sys.stdin.readline().split())

result = []

def solution(depth) :
    if depth == m :
        print(" ".join(map(str, result)))
        return

    for j in range(n) :
        result.append(j+1)
        solution(depth+1)
        result.pop()
            
solution(0)