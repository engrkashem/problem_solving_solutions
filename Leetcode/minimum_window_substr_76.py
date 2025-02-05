from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        if not s or not t:
            return ""
    
        t_counter = Counter(t)
        s_counter = Counter()
        
        left, right = 0, 0
        min_len = float("inf")
        min_substr = ""
        required_chars = len(t_counter)
        formed_chars = 0
        
        while right < len(s):
            char = s[right]
            s_counter[char] += 1
            
            if char in t_counter and s_counter[char] == t_counter[char]:
                formed_chars += 1
            
            while left <= right and formed_chars == required_chars:
                window_size = right - left + 1
                if window_size < min_len:
                    min_len = window_size
                    min_substr = s[left:right+1]
                
                s_counter[s[left]] -= 1
                if s[left] in t_counter and s_counter[s[left]] < t_counter[s[left]]:
                    formed_chars -= 1
                
                left += 1
            
            right += 1
        
        return min_substr


obj=Solution()
s = "ADOBECODEBANC"; t = "ABC"
# s = "a"; t = "a"
# s = "a"; t = "aa"
print(obj.minWindow(s,t))