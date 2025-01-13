class Solution:
    def search(self, nums, target):
        low,high=0,len(nums)-1
        
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            
            if nums[low]<=nums[mid]:
                if nums[low] <= target and  nums[mid]>target:
                    high=mid-1
                else: low=mid+1
                
            else:
                if nums[mid]<target and nums[high]>=target:
                    low=mid+1
                else: 
                    high=mid-1
                
        return -1
                
    
obj=Solution()
# nums = [4,5,6,7,0,1,2]; target = 0 #4
# nums = [4,5,6,7,0,1,2]; target = 3 #-1
# nums = [1]; target = 0 #-1
nums=[5,1,3]; target=3 #2
print(obj.search(nums,target))