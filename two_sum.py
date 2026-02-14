class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            d[num] = i
s1=Solution()
nums=[2,7,11,15]
target=9
print(s1.twoSum(nums,target))