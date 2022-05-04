import sys

def input():
    return sys.stdin.readline().rstrip()

count=int(input())

stack=[]

for i in range(count):
    num=int(input())
    if num!=0:
        stack.append(num)
    else:
        stack.pop()
        
print(sum(stack))