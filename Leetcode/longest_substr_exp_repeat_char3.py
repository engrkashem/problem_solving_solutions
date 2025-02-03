class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left=0
        maxLength=0
        strMap={}

        for right in range(len(s)):
            if s[right] in strMap:
                left=max(left, strMap[s[right]] + 1)
            
            strMap[s[right]]=right
            maxLength = max(maxLength, right-left+1)

        return maxLength
                    
    
# s = "abcabcbb"
# s = "bbbbb"
s = "pwwkew"
obj=Solution()
print(obj.lengthOfLongestSubstring(s))

"""

def lengthOfLongestSubstring(self, s):
        left=0
        maxLength=0
        subStrSet=set()

        for right in range(len(s)):
            while s[right] in subStrSet:
                subStrSet.remove(s[left])
                left +=1
            
            subStrSet.add(s[right])
            maxLength = max(maxLength, right-left+1)

        return maxLength

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

"""