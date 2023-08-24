class Solution:
    def longestCommonPrefix(self, strs):
        ans=''
        strs.sort()
        for i in range(len(strs[0])):
            if strs[0][i]!= strs[-1][i]:
                return ans
            ans+=strs[0][i]
        return ans
        

obj=Solution()
# strs = ["flower","flow","flight"]
strs = ["dog","racecar","car"]
print(obj.longestCommonPrefix(strs))