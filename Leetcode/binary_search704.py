class Solution(object):
    def search(self, nums, target):
        left,right=0,len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                left=mid+1
            else: right=mid-1
        return -1
        
    #     return ans
        
    # def binerySearch(self,nums, left, right, target):
    #     mid=0
    #     if left==right:
    #         mid=left
    #     else: mid=left+(right-left)//2
        
    #     if nums[mid]==target:
    #         return mid
        
    #     if nums[mid]>target:
    #         self.binerySearch(nums=nums,left=left,right=mid-1, target=target)
    #     else: self.binerySearch(nums=nums,left=mid+1,right=right, target=target)
    
    
obj=Solution()
# nums = [-1,0,3,5,9,12]; target = 9
nums = [-1,0,3,5,9,12]; target = 2
print(obj.search(nums,target))