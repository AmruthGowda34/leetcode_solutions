class Soltuion:
    def binary(self,n,tar):
        low=0
        high=len(n)-1
        while low<=high:
            mid=(low+high)//2
            if n[mid]==tar:
                return mid
            elif n[mid]<tar:
                low=mid+1
            else:
                high=mid-1
        return -1
s1=Soltuion()
n=[2,4,6,7,9,11,18,19]
print(s1.binary(n,91))
