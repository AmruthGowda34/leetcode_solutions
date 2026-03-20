class Listnode:
    def __init__(self,x):
        self.val=x
        self.next=None
        
class SLL:
    def ret_node(self,head):
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                slow=head
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                return slow
        return None
    
s1=SLL()
n1=Listnode(1)
n2=Listnode(2)
n3=Listnode(3)
n4=Listnode(4)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n2

print(s1.ret_node(n1).val)