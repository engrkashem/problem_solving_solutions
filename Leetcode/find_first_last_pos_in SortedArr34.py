class Solution(object):
    def searchRange(self, nums, target):
        if not nums: return [-1,-1]
        ans=[]
        n=len(nums)-1
        lb=self.lowerBound(nums, 0, n, target)
        if nums[lb]!=target: return [-1,-1]
        ans.append(lb)
        ub=self.upperBound(nums, lb, n, target)
        ans.append(ub)
        return ans
    
    def lowerBound(self,nums,l,r,target):
        
        while l<r:
            mid = (l+r)//2
            
            if nums[mid]<target:l=mid+1
            else:r=mid
        return l
        
    def upperBound(self, nums, l, r, target):
        while l<r:
            mid=(l+r)//2
            if nums[mid]<=target:l=mid+1
            else: r=mid-1
        if nums[l]!= target: return l-1
        return l
                

obj=Solution()
# nums = [5,7,7,8,8,10]; target = 6
nums = [5,7,7,8,8,10]; target = 8
# nums = []; target = 0
# nums=[1,2,3]; target=2
print(obj.searchRange(nums,target))