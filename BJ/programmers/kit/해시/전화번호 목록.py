import collections

def solution(phone_book):
    dict=collections.defaultdict(int)
    
    for phone in phone_book:
        dict[phone]+=1
    
    for phone in phone_book:
        for idx in range(len(phone)):
            if dict[phone[:idx]]:
                return False
    
    return True
    