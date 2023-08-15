class Node:
    def __init__(self, val):
        self.data=val
        self.next=None
    
class SLL:
    def __init__(self) -> None:
        self.val=None
        
    def listprint(self):
        printval = self.val
        while printval is not None:
            print (printval.data)
            printval = printval.next

head=SLL()
head.val=Node(1)
n1=head.val.next=Node(2)
n2=n1.next=Node(3)
n3=n2.next=Node(4)
head.listprint()
