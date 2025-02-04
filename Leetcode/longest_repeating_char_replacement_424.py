class Solution(object):
    def characterReplacement(self, s, k):
        left= maxCount = maxLength = 0
        freq={}
        

        for right in range(len(s)):
            freq[s[right]]=freq.get(s[right], 0) + 1
            maxCount=max(maxCount, freq[s[right]])

            if (right -left + 1) - maxCount > k:
                freq[s[left]] -= 1
                left += 1
            
            maxLength=max(maxLength, right - left + 1 )
        
        return maxLength


obj=Solution()
s = "ABAB"; k = 2
# s = "AABABBA"; k = 1
print(obj.characterReplacement(s,k))