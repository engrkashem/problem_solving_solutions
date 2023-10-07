class Solution:
    priority_queue = []

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        median = 0
        if not nums1 and not nums2:
            median = float(median)
            return median

        for num in nums1:
            self.insert(num)

        for num in nums2:
            self.insert(num)

        n = len(self.priority_queue)

        if n % 2 == 0:
            mid = n//2
            mid_val1 = self.priority_queue[mid]
            mid_val2 = self.priority_queue[mid-1]
            median = float((mid_val1+mid_val2)/2)
        else:
            mid = n//2
            median = float(self.priority_queue[mid])

        # print(type(median))
        return median

    def insert(self, num: int) -> None:
        if self.is_empty():
            self.priority_queue.append(num)
            return
        lb = self.left_bound(num)
        # print('lb', lb)
        self.priority_queue.insert(lb, num)

    def is_empty(self) -> bool:
        if len(self.priority_queue) == 0:
            return True
        return False

    def left_bound(self, num: int) -> int:
        l, r = 0, len(self.priority_queue)-1
        while l <= r:
            mid = (l+r)//2
            if self.priority_queue[mid] < num:
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
# print(obj.findMedianSortedArrays([2], [1]))
