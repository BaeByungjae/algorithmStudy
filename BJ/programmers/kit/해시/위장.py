import collections

def solution(clothes):
    ans=1
    dict=collections.defaultdict(int)
    for cloth in clothes:
        type=cloth[1]
        dict[type]+=1
    for type in dict:
        ans*=(dict[type]+1)
    
    return ans-1
