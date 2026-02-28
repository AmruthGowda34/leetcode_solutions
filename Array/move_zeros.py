class Solution(object):
    def move(self,nums):
        i=0
        while i<len(nums):
            if nums[i]==0:
                break
            i+=1
        j=i+1
        while j<len(nums):
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            j+=1
        return nums
s1=Solution()
nums=[1,0,2,4,3,0,0,3,5,1]
print(s1.move(nums))