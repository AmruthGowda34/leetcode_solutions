# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False

s1=Solution()

n1=ListNode(1)
n2=ListNode(2)
n3=ListNode(3)
n4=ListNode(4)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n1

print(s1.hasCycle(n1))