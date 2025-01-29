class Solution(object):
    def getSum(self, a, b):

        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b!=0:
            carry=(a&b)&MASK
            a=(a^b)&MASK
            b=carry<<1

        return a if a<=MAX_INT else ~(a^MASK)
    

obj=Solution()
# a,b = 1,  2
a,b = 2, 3
a,b = -1, 1
print(obj.getSum(a,b))