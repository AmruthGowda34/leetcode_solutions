class Solution:
    def longest_conse(self,nums):
        my_set=set()
        for i in range(len(nums)):
            my_set.add(nums[i])
        maxi=0
        for i in my_set:
            if i-1 not in my_set:
                a=i
                length=1
                while a+1 in my_set:
                    length+=1
                    a+=1
                maxi=max(maxi,length)
        return maxi

s1=Solution()
nums=[1,99,101,98,2,5,3,1,1,100,0,4]
print(s1.longest_conse(nums))