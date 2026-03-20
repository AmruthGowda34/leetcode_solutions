class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class SLL:
    def last_del(self,head,n):
        slow=head
        fast=head
        for _ in range(n):
            fast=fast.next
        if fast==None:
            return head.next
        while fast.next!=None:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next    
        return head
    def print_ll(self,head):
        while head:
            print(head.val,end=" ")
            head=head.next

s1=SLL()

values=[1,2,3,4,5,6]
head=Node(values[0])
current=head

for i in values[1:]:
    current.next=Node(i)
    current=current.next

dis=s1.last_del(head,4)

s1.print_ll(dis)