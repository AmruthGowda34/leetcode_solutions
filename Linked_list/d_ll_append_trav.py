class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None

class DLL:
    def __init__(self):
        self.head=None
        
    def insert_at_head(self,val):
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
    
    def append(self,val):
        new_node=Node(val)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp
    
    def insert(self,val,pos):
        new_node=Node(val)
        if pos==0:
            self.insert_at_head(val)
            return
        current=self.head
        count=0
        while current and count<pos-1:
            current=current.next
            count+=1
        if current is None:
            print("Index out of bound!")
            return
        new_node.next=current.next
        new_node.prev=current
        if current.next:
            current.next.prev=new_node
        current.next=new_node
    def print_ll(self,head):
        while head:
            print(head.val,end=" ")
            head=head.next
    def print_rev(self,head):
        current=head
        while current and current.next:
            current=current.next
        tail=current
        print()
        while tail:
            print(tail.val,end=" ")
            tail=tail.prev
            
d1=DLL()
d1.insert_at_head(20)
d1.insert_at_head(10)

d1.append(40)
d1.insert(30,2)
HP=d1.head
d1.print_ll(HP)
d1.print_rev(HP)