class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n=len(s)
        l,maxLen=0,0
        subStrSet=set()
        for r in range(n):
            if s[r] not in subStrSet:
                subStrSet.add(s[r])
                maxLen=max(maxLen, r-l+1)
            else:
                while s[r] in subStrSet:
                    subStrSet.remove(s[l])
                    l+=1
                subStrSet.add(s[r])
        return maxLen
                    
    
# s = "abcabcbb"
# s = "bbbbb"
s = "pwwkew"
obj=Solution()
print(obj.lengthOfLongestSubstring(s))