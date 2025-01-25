import copy

def threeSum( nums):
    
    nums.sort()
    result=[]

    for i,n in enumerate(nums):
        if n>0:
            break

        if i>0 and n== nums[i-1]:
            continue

        low, high=i+1, len(nums)-1
        while low<high:
            threeSum=nums[low]+n+nums[high]
            if threeSum>0:
                high -=1
            elif threeSum<0:
                low +=1
            else:
                result.append([nums[low],n,nums[high]])
                low +=1
                high -=1

                while low<high and nums[low]==nums[low-1] :
                    low +=1
        
    return result



nums = [-1,0,1,2,-1,-4]
# nums = [0,1,1]
# nums = [0,0,0]


res=threeSum(nums)
print(res)


"""
nums.sort()
    ans=[]
    
    for i,n in enumerate(nums):
        if n>0:
            break
        if i>0 and n==nums[i-1]:
            continue
        
        left, right=i+1,len(nums)-1
        while left<right:
            threeSum=nums[left]+n+nums[right]
            if threeSum>0:
                right-=1
            elif threeSum<0:
                left+=1
            else:
                ans.append([n,nums[left],nums[right]])
                left+=1
                right-=1
                while nums[left]==nums[left-1] and left<right:
                    left+=1
    
    return ans
"""