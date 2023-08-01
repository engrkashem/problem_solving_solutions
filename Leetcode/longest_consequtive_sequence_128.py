
def longestConsecutive(nums):
    numsSet=set(nums)    
    print(numsSet)
    longestSeq=0
    
    for num in numsSet:
        
        if (num-1) not in numsSet:
            seqLength=1
            
            while (num+seqLength) in numsSet:
                seqLength+=1
            
            longestSeq=max(seqLength,longestSeq)
    
    return longestSeq
            
    
# nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]
res=longestConsecutive(nums)
print(res)