import sys

n = int(sys.stdin.readline().rstrip())

visited = [False] * n
result = []

def solution() :
    if len(result) == n :
        print(" ".join(map(str, result)))
        return

    for i in range(n) :
        if visited[i] == False :
            visited[i] = True
            result.append(i+1)
            solution()
            visited[i] = False
            result.pop()
    
solution()