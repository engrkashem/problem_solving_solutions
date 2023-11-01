class Solution:
    def subsets(self, nums):
        ans = []
        subset = []

        def backtrack(i):
            if i >= len(nums):
                print(subset.copy(), subset)
                ans.append(subset.copy())
                return

            subset.append(nums[i])
            backtrack(i + 1)

            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return ans


obj = Solution()
nums = [1, 2, 3]
print(obj.subsets(nums))
