class Solution(object):
    def threeSumClosest(self, nums, target):
        ans=nums[0]+nums[1]+nums[2]
        nums.sort()
        n=len(nums)
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:continue
            l,r=i+1,n-1
            while l<r:
                sum3=nums[i]+nums[l]+nums[r]
                if sum3==target: return sum3
                if abs(sum3-target)<abs(ans-target):
                    ans=sum3
                if sum3<target:l+=1
                else: r-=1
        return ans
    
obj=Solution()
# nums = [-1,2,1,-4]; target = 1
# nums = [0,0,0]; target = 1
nums =[1,1,1,0]; target =-100 #op:2
# nums =[4,0,5,-5,3,3,0,-4,-5]; target =-2 #op:-2
print(obj.threeSumClosest(nums, target))

# a=2;b=-3
# print(abs(a-b))
# a=-2;b=-3
# print(abs(a-b))
# a=-3;b=2
# print(abs(a-b))