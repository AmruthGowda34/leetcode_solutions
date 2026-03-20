class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
    
class SLL:
    def odd_even(self,head):
        if head==None or head.next==None:
            return head
        odd=head
        even=head.next
        even_head=even
        while even!=None and even.next!=None:
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next
        odd.next=even_head
        return head
s1=SLL()
values=[2,1,3,5,6,4,7]
head=Node(values[0])
current=head

for i in values[1:]:
    current.next=Node(i)
    current=current.next

result=s1.odd_even(head)

while result:
    print(result.val,end=" ")
    result=result.next