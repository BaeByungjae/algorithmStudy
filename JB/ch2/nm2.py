import sys

n, m = map(int, sys.stdin.readline().split())

visited = [False for _ in range(n)]
result = []

def solution(num, depth) :
    if depth == m :
        print(" ".join(map(str, result)))
        return

    for j in range(num, n) :
        if visited[j] == False :
            visited[j] = True
            result.append(j+1)
            solution(j+1, depth+1)
            visited[j] = False
            result.pop()
            

solution(0, 0)