class node:
    def __init__(self,val):
        self.val=val
        self.next=None
node1=node(5)
node2=node(6)
node3=node(7)
node4=node(8)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=None

print(node1)
print(node1.next)
print(node2.next)
print(node3.next)
print(node4.next)