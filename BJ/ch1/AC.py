import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


cnt = int(input())

for i in range(cnt):
    cmd = input()
    initialLen = int(input())
    arrData = input()
    reverseFlag = False
    error=False

    if initialLen == 0:
        deq = []
    else:
        deq = deque(list(map(int, arrData.strip()[1:-1].split(','))))
    for i in cmd:
        if i == 'R':
            reverseFlag = not reverseFlag
        elif i == 'D':
            if len(deq) == 0:
                error=True
                break

            if reverseFlag is True:
                deq.pop()
            else:
                deq.popleft()

    if len(deq) > 0:
        if reverseFlag == True:
            deq.reverse()
        print("[",end="")
        for idx,num in enumerate(deq):
            if(idx is not len(deq)-1):
                print(num,end=",")
            else:
                print(num,end="")
        print("]")

    elif error is True:
        print("error")

    else:
        print("[]")