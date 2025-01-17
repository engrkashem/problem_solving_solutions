class Solution(object):
    def maxProduct(self, nums):
        result=minProduct=maxProduct=nums[0]

        for num in nums[1:]:
            if num<0:
                minProduct,maxProduct = maxProduct, minProduct

            maxProduct=max(num, maxProduct*num)
            minProduct=min(num, minProduct*num)


            result=max(result, maxProduct)

        return result
    
obj=Solution();
# inp=[2,3,-2,4]
# inp=[-2,0,-1]
inp=[-4,-3,-2]
print(obj.maxProduct(inp))