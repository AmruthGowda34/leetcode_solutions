class Solution(object):
    def reverse(self, x):
        sign=-1 if x<0 else 1
        num=abs(x)
        re=0
        while num>0:
            last=num%10
            re=(re*10)+last
            num//=10
        if re < -2**31 or re > 2**31 - 1:
            return 0
        return sign*re
s1=Solution()
x=7491
print(s1.reverse(x))