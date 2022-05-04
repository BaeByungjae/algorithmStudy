from collections import deque
import sys

t = int(sys.stdin.readline())

for i in range(t) :
    cmd = sys.stdin.readline()
    n = int(sys.stdin.readline())
    nums = deque(sys.stdin.readline().strip()[1:-1].split(","))  

    flag = 1
    r_flag = 0

    if n == 0 :
        nums = deque()
    
    for f in cmd :  
        if f == "R" :
            r_flag = not r_flag

        elif f == "D" :
            if len(nums) > 0 :
                if r_flag == 0 :
                    nums.popleft()
                elif r_flag == 1 :
                    nums.pop()
            else :
                flag = 0
                break 

    if flag == 1 :
        if len(nums) == 0:
            result = "[]" 
        if r_flag == 1 :
            nums.reverse()
        result = f'[{",".join(nums)}]'
    else :
        result = "error"
    
    print(result)

    
