class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None

class d_ll:
    # def rev(self,head):
    #     stack=[]
    #     temp=head
    #     while temp is not None:
    #         stack.append(temp.val)
    #         temp=temp.next
    #     temp=head
    #     while temp is not None:
    #         e=stack.pop()
    #         temp.val=e
    #         temp=temp.next
    #     return head
    def rev(self,head):
        current=head
        prev=None
        while current!=None:
            front=current.next
            current.next=prev
            current.prev=front
            prev=current
            current=front
        return prev
    def print__dll(self,head):
        while head:
            print(head.val,end=" ")
            head=head.next

s1=d_ll()
values=[1,2,3,4,5]
head=Node(values[0])

current=head
for i in values[1:]:
    new_node=Node(i)
    current.next=new_node
    new_node.prev=current
    current=new_node
result=s1.rev(head)
s1.print__dll(result)

# while result:
#     print(result.val,end=" ")
#     result=result.next