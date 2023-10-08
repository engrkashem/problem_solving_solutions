class Solution:
    sorted_merged_array = []

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        median = 0
        if not nums1 and not nums2:
            median = float(median)
            return median

        for num in nums1:
            self.insert(num)

        for num in nums2:
            self.insert(num)

        n = len(self.sorted_merged_array)

        if n % 2 == 0:
            mid = n//2
            mid_val1 = self.sorted_merged_array[mid]
            mid_val2 = self.sorted_merged_array[mid-1]
            median = float((mid_val1+mid_val2)/2)
        else:
            mid = n//2
            median = float(self.sorted_merged_array[mid])

        # print(type(median))
        return median

    def insert(self, num: int) -> None:
        if self.is_empty():
            self.sorted_merged_array.append(num)
            return
        lb = self.left_bound(num)
        # print('lb', lb)
        self.sorted_merged_array.insert(lb, num)

    def is_empty(self) -> bool:
        if len(self.sorted_merged_array) == 0:
            return True
        return False

    def left_bound(self, num: int) -> int:
        l, r = 0, len(self.sorted_merged_array)-1
        while l <= r:
            mid = (l+r)//2
            if self.sorted_merged_array[mid] < num:
                l = mid+1
            else:
                r = mid-1
        return l


obj = Solution()
# nums1 = [1, 3]
# nums2 = [2]
nums1 = [1, 2]
nums2 = [3, 4]
print(obj.findMedianSortedArrays(nums1, nums2))
# print(obj.findMedianSortedArrays([], []))
