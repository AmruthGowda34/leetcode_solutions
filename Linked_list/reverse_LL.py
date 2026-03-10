    # Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reverseList(self, head):
        temp=head
        prev=None
        while temp!=None:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        return prev
    def printList(self,head):
        while head:
            print(head.val,end=" ")
            head=head.next
s1=Solution()
values=[1,2,3,4,5,6]
head=ListNode(values[0])
current=head

for i in values[1:]:
    current.next=ListNode(i)
    current=current.next
reversed_head = s1.reverseList(head)

# Print
s1.printList(reversed_head)