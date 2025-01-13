class Solution:
    def strStr(self, haystack, needle):
        if needle in haystack:
            ans = haystack.find(needle)
            return ans
        else:
            return -1


obj = Solution()
# haystack = "sadbutsad"; needle = "sad"
# haystack = "leetcode"; needle = "leeto"
haystack = "leetcode"
needle = "code"
print(obj.strStr(haystack, needle))
