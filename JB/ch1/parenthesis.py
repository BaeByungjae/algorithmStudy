n = int(input())
answer = [1 for i in range(n)]

for i in range(n) :
    que = input()
    res = []
    for x in que :
        if x == "(" :
            res.append("(")
        elif x == ")" :
            if "(" in res :
                res.pop()
            else :
                answer[i] = 0
                break
    if (len(res) != 0) :
        answer[i] = 0
    
    if answer[i] == 0 :
        print("NO")
    
    if answer[i] == 1 :
        print("YES")
      
