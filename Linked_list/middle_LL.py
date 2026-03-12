class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
        
class Solution(object):
    def middleNode(self, head):
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow
    
s1=Solution()
values = [1,2,3,4,5,6]
head = Node(values[0])
current = head

for v in values[1:]:
    current.next = Node(v)
    current = current.next
print(s1.middleNode(head).val)