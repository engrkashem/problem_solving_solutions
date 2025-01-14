class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # isExists={}
        visited=set()

        for num in nums:
            if num in visited:
                return True
            visited.add(num)
       
        return False

        

obj=Solution()
inp=[1,2,3,1]
# inp=[1,2,3,4]
# inp=[1,1,1,3,3,4,3,2,4,2]

print(obj.containsDuplicate(inp))