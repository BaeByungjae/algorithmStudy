import sys

n = int(sys.stdin.readline().rstrip())

table = [0 for _ in range(n)]
result = 0

def check(level) :
    for i in range(level) :
        if table[i] == table[level] or abs(table[level] - table[i]) == abs(level - i) :
            return False

    return True

def nqueen(depth) :
    global result
    if depth == n :
        result += 1
        return
    
    for i in range(n) :
        table[depth] = i
        if check(depth) :
            nqueen(depth+1)

nqueen(0)
print(result)