class Solution(object):
    # Divide and Conquer Algorithm
    def maxSubArray(self, nums):
        result = self.divideAndConquer(nums, 0, len(nums)-1)
        return result
    
    def findMaxCrossingSum(self,nums, left, mid, right):
        left_sum = float('-inf')
        right_sum = float('-inf')
        
        # Calculate the maximum sum in the left half (from mid to left)
        current_sum = 0
        for i in range(mid, left - 1, -1):
            current_sum += nums[i]
            left_sum = max(left_sum, current_sum)
        
        # Calculate the maximum sum in the right half (from mid+1 to right)
        current_sum = 0
        for i in range(mid + 1, right + 1):
            current_sum += nums[i]
            right_sum = max(right_sum, current_sum)
        
        # The maximum crossing sum is the sum of both parts
        return left_sum + right_sum
    
    def divideAndConquer(self,nums, left, right):
        if left == right:
            return nums[left]  # Base case: single element

        mid = (left + right) // 2
        left_max = self.divideAndConquer(nums, left, mid)  # Maximum sum in the left half
        right_max = self.divideAndConquer(nums, mid + 1, right)  # Maximum sum in the right half
        cross_max = self.findMaxCrossingSum(nums, left, mid, right)  # Maximum sum that crosses the midpoint
        
        # Return the maximum of the three values
        return max(left_max, right_max, cross_max)
    

    
obj=Solution()
# inp=[-2,1,-3,4,-1,2,1,-5,4]
# inp=[1]
inp=[5,4,-1,7,8]

print(obj.maxSubArray(inp))

"""
# Kadane's Algorithm
    def maxSubArray(self, nums):
        maxSum=nums[0]
        projectedMaxSum=nums[0]

        for i in range(1,len(nums),1):
            if nums[i]>=projectedMaxSum+nums[i]:
                projectedMaxSum=nums[i]
            else:
                projectedMaxSum +=nums[i]

            if projectedMaxSum>maxSum:
                maxSum=projectedMaxSum

        return maxSum

        # with a bit change
        def maxSubArray(self, nums):
        maxSum=nums[0]
        projectedMaxSum=nums[0]

        for i in range(1,len(nums)):
            if nums[i]>projectedMaxSum+nums[i]:
                projectedMaxSum=nums[i]
            else:
                projectedMaxSum +=nums[i]

            if projectedMaxSum>maxSum:
                maxSum=projectedMaxSum

        return maxSum

"""