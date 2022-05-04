import sys

n, m = map(int, sys.stdin.readline().split())

totalSet = {}
cnt = 0

for i in range(n) :
    word = sys.stdin.readline().rstrip()
    totalSet[word] = 1

for j in range(m) :
    check = sys.stdin.readline().rstrip()
    if totalSet.get(check) :
        cnt += 1

print(cnt)

