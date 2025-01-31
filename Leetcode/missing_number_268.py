class Solution(object):
    def missingNumber(self, nums):
        result=len(nums)

        for i,num in enumerate(nums):
            result ^= i^num
        
        return result


obj=Solution()
# nums = [3,0,1]
# nums = [0,1]
nums = [9,6,4,2,3,5,7,0,1]
print(obj.missingNumber(nums))

"""
def missingNumber(self, nums):
        n=len(nums)
        sumOfNNaturalNum=n*(n+1)//2
        return sumOfNNaturalNum-sum(nums)


def missingNumber(self, nums):
        visited=[0]*(len(nums)+1)
       
        for num in nums:
            visited[num]=1
        
        for num,isVisited in enumerate(visited):
            if isVisited==0:
                return num

"""