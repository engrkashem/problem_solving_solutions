from collections import Counter

def topKFrequent( nums, k):
    countFreq={}
    for num in nums:
        countFreq[num]=1+countFreq.get(num,0)
        
    ascendingFreqList=[[] for i in range(len(nums)+1)]
    for key,val in countFreq.items():
        ascendingFreqList[val].append(key)
    
    result=[]
    for i in range(len(ascendingFreqList)-1, 0, -1):
        for n in ascendingFreqList[i]:
            result.append(n)
            if len(result)==k:
                return result
            
        
    # print(ascendingFreqList)
                       
nums = [1,1,1,2,2,3,4,4,4,6,6,6,6,6]
k = 2
res=topKFrequent(nums, k)
print(res)