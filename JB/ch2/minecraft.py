import sys

table = []
n, m, b = map(int, sys.stdin.readline().split())

for _ in range(n) :
    table.append(list(map(int, sys.stdin.readline().split())))

minTime = 256 * 2 * 500 * 500
finalHeight = 0

for i in range(min(min(table)), max(max(table))+1) :
    plus = 0
    minus = 0
    for x in range(n) :
        for y in range(m) :
            diff = i - table[x][y] # 목표 높이 - 현재 높이
            # 블록 추가
            if diff > 0 :
                plus += diff
            
            # 블록 제거
            else :
                minus += abs(diff)

    if plus > minus + b :
        continue

    time = plus + minus * 2        
    if time <= minTime : 
        minTime = time
        finalHeight = i
            
print(minTime, finalHeight)
