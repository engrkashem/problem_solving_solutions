class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        if nums[l] < nums[r]:
            return nums[l]

        while (l < r):
            if l == r-1:
                return min(nums[l], nums[r])

            mid_index = (l+r)//2
            left_val = nums[l]
            right_val = nums[r]
            mid_val = nums[mid_index]

            if left_val < mid_val:
                if mid_val > right_val:
                    l = mid_index+1
                else:
                    r = mid_index-1
            elif right_val > mid_val:
                r = mid_index
                l += 1
            else:
                if left_val == right_val:
                    l += 1
                    r -= 1
                elif right_val < mid_val:
                    l = mid_index
                elif left_val > mid_val:
                    r = mid_index

        return nums[l]


obj = Solution()
nums = [1, 3, 5]
# nums = [2, 2, 2, 0, 1]
# nums = [2, 3, 4, 0, 1]
# nums = [4, 0, 1, 2, 3]
# nums = [1, 2, 3, 4, 0]
# nums = [100]
# nums = [10, 1, 10, 10, 10]
# nums = [10, 10, 10, 1, 10]
# nums = [10, 10, 10, 10, 1]
# nums = [1, 10, 10, 10, 10]
# nums = [100, 1, 1, 1, 1, 1, 1]
# nums = [1, 1, 1, 1, 1, 1, 100]
print(obj.findMin(nums))
