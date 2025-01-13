class Solution:
    def combinationSum(self, candidates, target):
        result = []
        currentSubset = []

        def backTrack(i,  total):
            if total == target:
                result.append(currentSubset.copy())
                return
            if i >= len(candidates) or total > target:
                return

            currentSubset.append(candidates[i])
            backTrack(i,  total + candidates[i])
            currentSubset.pop()
            backTrack(i + 1, total)

        backTrack(0,  0)
        return result


obj = Solution()
candidates = [2, 3, 6, 7]
target = 7

print(obj.combinationSum(candidates, target))
