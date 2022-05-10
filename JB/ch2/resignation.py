import sys

n = int(sys.stdin.readline().rstrip())

table = []
result = [0]

for i in range(n) :
    t, p = map(int, sys.stdin.readline().split())
    table.append((t,p))

def bf(day, pay) :
    global result
    for j in range(day, n) :
        if j + table[j][0] < n + 1 :
            result.append(bf(j+table[j][0], pay+table[j][1]))
    return pay

bf(0, 0)
print(max(result)) 


