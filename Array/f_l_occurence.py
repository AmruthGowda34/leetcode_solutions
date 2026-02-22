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

# n=[1,2,3,3,3,3,3,5,6,8,9,9,10]
# tar=3
# f_o=-1
# l_o=-1
# for i in range(len(n)):
#     if n[i]==tar:
#         if f_o==-1:
#             f_o=i
#         l_o=i
# print(f_o,l_o)