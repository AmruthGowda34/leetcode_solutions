# n=[1,2,3,3,3,3,3,5,6,8,9,9,10]
# tar=77
# count=0
# for i in range(len(n)):
#     if n[i]==tar:
#         count+=1
# print(count)

class Solution:
    def lower_b(self,n,tar):
        low=0
        high=len(n)-1
        l_b=-1
        while low<=high:
            mid=(low+high)//2
            if n[mid]>=tar:
                l_b=mid
                high=mid-1
            else:
                low=mid+1
        return l_b
    def upper_b(self,n,tar):
        low=0
        high=len(n)-1
        u_b=len(n)
        while low<=high:
            mid=(low+high)//2
            if n[mid]>tar:
                u_b=mid
                high=mid-1
            else:
                low=mid+1
        return u_b
    def count_occurrence(self,n,tar):
        l_b=self.lower_b(n,tar)
        if l_b==-1:
            return 0
        u_b=self.upper_b(n,tar)
        return u_b-l_b
s1=Solution()
n=[1,2,3,3,3,3,3,5,6,8,9,9,10]
print(s1.count_occurrence(n,3))