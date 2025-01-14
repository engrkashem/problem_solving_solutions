class Solution(object):
    def solve(self, heights):
        """
        :type height: List[int]
        :rtype: int
        """
        if not heights:
            return 0

        left, right = 0, len(heights)-1
        maxL, maxR = heights[left], heights[right]

        while left < right:
            if maxL < maxR:
                if left+1 < right:
                    left += 1
                    maxL = max(maxL, heights[left])
                else:
                    break
            else:
                if right-1 > left:
                    right -= 1
                    maxR = max(maxR, heights[right])
                else:
                    break
        return maxL, maxR


obj = Solution()

test = int(input())
for _ in range(test):
    n = int(input())
    h = list(map(int, input().split(" ")))
    ans = obj.solve(h)
    l = h.index(ans[0])
    r = h.index(ans[1])
    print(l, r)
