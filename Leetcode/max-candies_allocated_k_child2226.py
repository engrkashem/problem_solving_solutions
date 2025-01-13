class Solution:
    def maximumCandies(self, candies, k):
        l, r = 0, sum(candies) // k
        while l < r:
            mid = (l + r + 1) // 2
            if k > sum(candy // mid for candy in candies):
                r = mid - 1
            else:
                l = mid
        return l
    
obj=Solution()
candies = [5,8,6]; k = 3
# candies = [2,5]; k = 11
print(obj.maximumCandies(candies,k))