class Solution:
    def maximum_subarray(self,nums):
        maxi=float("-inf")
        total=0
        for i in range(len(nums)):
            total+=nums[i]
            maxi=max(maxi,total)
            if total<0:
                total=0
        return maxi
s1=Solution()            
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(s1.maximum_subarray(nums))
