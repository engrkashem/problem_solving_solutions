
def productExceptSelf(nums):
    result=[-1]*len(nums)
    prefixProduct=1
    postfixProduct=1
    
    for i in range(len(nums)):
        result[i]=prefixProduct
        prefixProduct *=nums[i]
    
    for j in range(len(nums)-1, -1, -1):
        result[j] *=postfixProduct
        postfixProduct *= nums[j]
        
    return result

nums = [1,2,3,4]
result=productExceptSelf(nums)
# print(result)