class Solution(object):
    def reverseList(self, head):
        cur, prv=head,None
        while cur:
            tem=cur.next
            cur.next=prv
            prv=cur
            cur=tem
        return prv
            