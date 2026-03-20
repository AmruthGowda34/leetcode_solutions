class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None

class DLL:
    def pair(self,head,tar):
        # temp1=head
        # result=[]
        # while temp1!=None:
        #     temp2=temp1.next
        #     while temp2!=None:    Brute_force T_C=O(n^2)
        #         if temp1.val+temp2.val==tar:  S_C=O(1)
        #             result.append([temp1.val,temp2.val])
        #         temp2=temp2.next
        #     temp1=temp1.next
        # return result
        
        #Better
        # d=set()
        # result=[]
        # temp=head
        # i=0
        # while temp!=None:   T_C=O(n)
        #     a=tar-temp.val  S_C=O(n)
        #     if a in d:
        #         result.append([a,temp.val])
        #     d.add(temp.val)
        #     temp=temp.next
        # return result
        
        #Optimal
        result=[]
        left=head
        right=head
        while right.next!=None:
            right=right.next
        while left!=None and right!=None and right.next!=left:
            if left.val+right.val==tar:
                result.append([left.val,right.val])
                left=left.next
                right=right.prev
            elif left.val+right.val>tar:
                right=right.prev
            else:
                left=left.next
        return result
s1=DLL()
values=[1,2,4,5,6,8,9]
head=Node(values[0])
current=head

for i in values[1:]:
    new_node=Node(i)
    current.next=new_node
    new_node.prev=current
    current=new_node

print(s1.pair(head,7))