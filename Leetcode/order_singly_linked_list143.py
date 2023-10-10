# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        prv, cur = None, slow.next
        while cur:
            tem = cur.next
            cur.next = prv
            prv = cur
            cur = tem
        slow.next = None

        temp = head
        while prv:
            tem = temp.next
            temp.next = prv
            temp = prv
            prv = tem

        return
