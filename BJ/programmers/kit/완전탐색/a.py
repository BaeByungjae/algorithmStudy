import collections

def solution(nums,k):
    arr=[]
    dict=collections.Counter(nums)
    
    for num in dict.most_common(n=k):
        arr.append(num[0])
        
    return arr