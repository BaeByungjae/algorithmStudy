import sys

table = []

for _ in range(19) :
    table.append(list(map(int, sys.stdin.readline().split())))

# 갈 수 있는 방향이 4가지 -> r, b, rb, rt
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for x in range(19):
    for y in range(19):
        if table[x][y] != 0:
            winner = table[x][y]

            for d in range(4) :
                cnt = 1
                nx = x + dx[d]
                ny = y + dy[d]

                while 0 <= nx < 19 and 0 <= ny < 19 and table[nx][ny] == winner:
                    cnt += 1

                    if cnt == 5:
                        if 0 <= x - dx[d] < 19 and 0 <= y - dy[d] < 19 and table[x - dx[d]][y - dy[d]] == winner :
                            break
                        if 0 <= nx + dx[d] < 19 and 0 <= ny + dy[d] < 19 and table[nx + dx[d]][ny +dy[d]] == winner:
                            break
                        
                        print(winner)
                        print(x+1 , y+1)
                        sys.exit(0)

                    nx += dx[d]
                    ny += dy[d]

print(0)
        

            
    
