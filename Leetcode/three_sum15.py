
def threeSum( nums):
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


# nums = [-1,0,1,2,-1,-4]
# nums = [0,1,1]
nums = [0,0,0]

res=threeSum(nums)
print(res)