import sys

n, p = map(int, sys.stdin.readline().split())

guitar = [[] for i in range(n)]

cnt = 0 # pop이나 push가 생기면 1씩 증가

for i in range(n) :
    melody, pret = map(int, sys.stdin.readline().split())

    if len(guitar[melody]) == 0 :
        guitar[melody].append(pret)
        cnt += 1

    else :
        if pret > guitar[melody][-1] :
            guitar[melody].append(pret)
            cnt += 1
        
        elif pret < guitar[melody][-1] :
            while guitar[melody] :
                if pret > guitar[melody][-1] or pret == guitar[melody][-1] :
                    break
                guitar[melody].pop()
                cnt += 1
            
            if len(guitar[melody]) and pret == guitar[melody][-1] :
                continue

            guitar[melody].append(pret)
            cnt += 1

        elif pret == guitar[melody][-1] : 
            continue
   
print(cnt)

    