class Solution(object):
    def productExceptSelf(self, nums):
        result=[0]*len(nums)
        leftProduct=1
        rightProduct=1
        
        for i,n in enumerate(nums):
            result[i]=leftProduct
            leftProduct *=n
        
        for j in range(len(nums)-1, -1, -1):
            result[j] *=rightProduct
            rightProduct *=nums[j]

        return result

obj=Solution()
# inp=[1,2,3,4]
inp=[-1,1,0,-3,3]
print(obj.productExceptSelf(inp))

# def productExceptSelf(nums):
#     result=[-1]*len(nums)
#     prefixProduct=1
#     postfixProduct=1
    
#     for i in range(len(nums)):
#         result[i]=prefixProduct
#         prefixProduct *=nums[i]
    
#     for j in range(len(nums)-1, -1, -1):
#         result[j] *=postfixProduct
#         postfixProduct *= nums[j]
        
#     return result

# nums = [1,2,3,4]
# result=productExceptSelf(nums)
# print(result)