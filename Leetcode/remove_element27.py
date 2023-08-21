
def removeElement( nums, val):
    
    # nums[:]=[num for num in nums if num!=val]
    new_num=[]
    for n in nums:
        if n!=val:
            new_num.append(n)
    nums[:]=new_num
    # print(nums)
    return len(nums)


# nums = [3,2,2,3]; val = 3
nums = [0,1,2,2,3,0,4,2]; val = 2

res=removeElement(nums, val)
print(res)