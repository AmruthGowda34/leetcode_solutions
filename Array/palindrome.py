class Solution(object):
    def isPalindrome(self, x):
        num=x
        result=0
        while num>0:
            last=num%10
            result=(result*10)+last
            num//=10
        if result==x:
            return True
        else:
            return False
s1=Solution()
x=int(input("Enter n:"))
print(s1.isPalindrome(x))