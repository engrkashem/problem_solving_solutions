class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        n=len(nums)
        ans=set()
        for i in range(n):
            for j in range(i+1,n):
                left, right = j+1, n-1
                check_num=target-nums[i]-nums[j]
                while left<right:
                    if nums[left]+nums[right]==check_num:
                        ans.add((nums[i], nums[j], nums[left], nums[right]))
                        left+=1
                        right-=1
                    elif nums[left]+nums[right]>check_num:
                        right-=1
                    else:
                        left+=1
        res=[]
        for numTuple in ans:
            res.append(list(numTuple))
        return res
                    
    
obj=Solution()
nums = [1, 0, -1, 0, -2, 2]; target = 0
# nums = [2,2,2,2,2]; target = 8
print(obj.fourSum(nums,target))