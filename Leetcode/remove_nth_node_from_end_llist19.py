class Node:
    def __init__(self,value) -> None:
        self.val=value
        self.next=None
class SLList:
    def __init__(self) -> None:
        self.head=None
        
def lstPrint(head):
    if not head:
        return []
    while head!=None:
        print(head.val, end=" ")
        head=head.next
    print()

class Solution(object):
    def removeNthFromEnd(self, head, n):
        slow,fast=head,head
        for _ in range(n):
            fast=fast.next
        if not fast:
            head=head.next
        else:
            while fast.next:
                slow,fast=slow.next, fast.next
            slow.next=slow.next.next
        return head
    
# [1,2,3,4,5]; [1]
l=[2,3,4,5]
# l=[2]
lst=SLList()
head=lst.head
head=Node(1)
tem=head
for i in l:
    n=Node(i)
    tem.next=n
    # print(tem.val)
    tem=tem.next
lstPrint(head)
obj=Solution()
ans=obj.removeNthFromEnd(head,2)
lstPrint(ans)

