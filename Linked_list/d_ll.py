class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
# s1=Node()
values=[1,2,3,4,5]
head=Node(values[0])
current=head

for i in values[1:]:
    new_node=Node(i)
    current.next=new_node
    new_node.prev=current
    current=new_node

temp=head
print("Forward :",end=" ")
while temp:
    print(temp.val,end=" ")
    temp=temp.next
# print()
print("\nBackward :",end=" ")
tail=current
while tail:
    print(tail.val,end=" ")
    tail=tail.prev
