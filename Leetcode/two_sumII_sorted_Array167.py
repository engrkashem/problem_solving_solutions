
def twoSum(numbers, target):
    res=[]
    sidx=0
    eidx=len(numbers)-1
    
    while True:
        if numbers[sidx]+numbers[eidx]==target:
            res.append(sidx+1)
            res.append(eidx+1)
            break
        
        if numbers[sidx]+numbers[eidx]<target:
            sidx+=1
        else:
            eidx-=1
            
    return res

numbers = [2,7,11,15]
target = 9
# numbers = [2,3,4]
# target = 6
# numbers = [-1,0]
# target = -1
# numbers = [2,3,6,15]
# target = 17

res=twoSum(numbers, target)
print(res)