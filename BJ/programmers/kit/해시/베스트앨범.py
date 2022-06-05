import collections

def solution(genres, plays):
    answer = collections.deque()
    sumDict=collections.defaultdict(int)
    countDict={}
    for index,genre in enumerate(genres):
        sumDict[genre]+=plays[index]
        if genre not in countDict:
            countDict[genre]=collections.deque()
            countDict[genre].append((plays[index],index))
        else:
            countDict[genre].append((plays[index],index))
    for genre in (sorted(sumDict,key=lambda x:sumDict[x],reverse=True)):
        li=sorted(countDict[genre],key=lambda x:(-x[0],x[1]))
        for idx,item in enumerate(li):
            if idx>=2:
                break
            answer.append(item[1])
    return list(answer)