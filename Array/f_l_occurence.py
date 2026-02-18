class Solution(object):
    def searchRange(self, nums, target):
        n = len(nums)
        low, high = 0, n-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        first = low
        
        if first == n or nums[first] != target:
            return [-1, -1]

        low, high = 0, n-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        last = high

        return [first, last]
s1=Solution()
nums=[5,7,7,8,8,10]
target=7
print(s1.searchRange(nums,target))