class Solution:
    def convert_s_i(self,s):
        s=s.strip()
        sign=1
        i=0
        num=0
        if s[0]=="-":
            sign=-1
            i=1
        while i<len(s) and s[i].isdigit():
            digit=ord(s[i])-ord('0')
            num=(num*10)+digit
            i+=1
        
        return sign*num

s1=Solution()

print(s1.convert_s_i("   -1947abcd"))