class Solution:
    def convert_D_B(self,num):
        result=" "
        while num>0:
            if num%2==1:
                result+="1"
            else:
                result+="0"
            num//=2
        return result[::-1]
    def convert_B_D(self,num1):
        re=0
        j=0
        for i in range(len(num1)-1,-1,-1):
            a=int(num1[i])*2**j
            j+=1
            re+=a
        return re

s1=Solution()
num=4
num1="111"
print(s1.convert_D_B(num))
print(s1.convert_B_D(num1))