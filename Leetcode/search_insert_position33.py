class Solution:
    def searchInsert(self, nums, target):
        n=len(nums)
        if nums[0]>target: return 0
        elif nums[n-1]<target: return n
        low,high=0,n-1
        
        while low<high:
            mid=(low+high)//2
            if(nums[mid]==target): return mid
            
            if nums[mid]<target:
                low=mid+1
            else: high=mid
        
        return low
    
obj=Solution()
# nums = [1,3,5,6]; target = 5
nums = [1,3,5,6]; target = 2
# nums = [1,3,5,6]; target = 7
# nums=[1,3]; target=2
print(obj.searchInsert(nums,target))