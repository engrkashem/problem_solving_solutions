class Solution(object):
    def longestPalindrome(self, s):
        # print(s[2:6])
        ans=''
        for i in range(len(s)):
            ans=max(ans, self.solve(s,i,i), self.solve(s,i,i+1), key=len)
        return ans
    
    def solve(self,s,i,j):
        while i>=0 and j<len(s) and s[i]==s[j]:
            i-=1
            j+=1
        return s[i+1:j]
    

obj=Solution()
s = "babadghjkl"
# s = "cbbd"
print(obj.longestPalindrome(s))