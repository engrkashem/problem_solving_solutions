class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        n = len(nums)
        # built in solve fpr python or js. not applicable for c/c++
        # if target in nums:
        #     return True
        # return False
        l, r = 0, n-1
        while l < r:
            mid_index = (l+r)//2
            mid_val = nums[mid_index]

            if nums[mid_index] == target or nums[l] == target or nums[r] == target:
                return True

            if nums[l] < nums[mid_index]:
                if nums[mid_index] > target:
                    r = mid_index-1
                else:
                    r = mid_index-1
            elif nums[r] > nums[mid_index]:
                if nums[mid_index] < target:
                    l = mid_index+1
                else:
                    r = mid_index-1


obj = Solution()
# nums = [2, 5, 6, 0, 0, 1, 2]
# target = 0
nums = [2, 5, 6, 0, 0, 1, 2]
target = 3
# nums = [2, 2, 2, 0, 1]
# target = 0
# nums = [2, 3, 4, 0, 1]
# target = 0
# nums = [4, 0, 1, 2, 3]
# target = 0
# nums = [1, 2, 3, 4, 0]
# target = 0
# nums = [100]
# target = 3
# nums = [10, 1, 10, 10, 10]
# target = 1
# nums = [10, 10, 10, 1, 10]
# target = 1
# nums = [10, 10, 10, 10, 1]
# target = 1
# nums = [1, 10, 10, 10, 10]
# target = 1
# nums = [100, 1, 1, 1, 1, 1, 1]
# target = 1
# nums = [1, 1, 1, 1, 1, 1, 100]
# target = 1
print(obj.search(nums, target))
