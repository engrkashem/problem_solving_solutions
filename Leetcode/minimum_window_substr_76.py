from collections import Counter, deque

class Solution(object):
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_counter = Counter(t)
        s_counter = Counter()
        required_chars = len(t_counter)
        formed_chars = 0

        min_len = float("inf")
        res_left, res_right = 0, 0

        window = deque()  # Stores valid character indices
        for right, char in enumerate(s):
            if char in t_counter:
                s_counter[char] += 1
                window.append(right)

                if s_counter[char] == t_counter[char]:
                    formed_chars += 1

            while window and formed_chars == required_chars:
                left = window[0]  # Get the leftmost valid index

                # Update result if we found a smaller window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res_left, res_right = left, right

                # Remove leftmost character from the window
                removed_char = s[left]
                s_counter[removed_char] -= 1
                window.popleft()

                if s_counter[removed_char] < t_counter[removed_char]:
                    formed_chars -= 1

        return s[res_left:res_right+1] if min_len != float("inf") else ""


obj=Solution()
s = "ADOBECODEBANC"; t = "ABC"
# s = "a"; t = "a"
# s = "a"; t = "aa"
print(obj.minWindow(s,t))

"""

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

"""