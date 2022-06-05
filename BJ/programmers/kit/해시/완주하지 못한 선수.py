# 일반적인 딕셔너리 풀이
import collections

def solution(participant, completion):
    dict={}
    for person in participant:
        if person not in dict:
            dict[person]=1
        else:
            dict[person]+=1
    for person in completion:
        dict[person]-=1
    for person in dict:
        if dict[person]:
            return person

# default Dict 활용

def solution_defaultDict(participant, completion):
    dict=collections.defaultdict(int)
    for char in participant:
        dict[char]+=1
        
    for char in completion:
        dict[char]-=1
        
    for person in dict:
        if dict[person]:
            return person


# 카운터 활용        
def solution_counter(participant, completion):
    dict=collections.Counter(participant)
    comp=collections.Counter(completion)
    
    for person in dict:
        if dict[person]!=comp[person]:
            return person