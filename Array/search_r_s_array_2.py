class Solution(object):
    def search(self, nums, target):
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return True
            if nums[low]==nums[mid]==nums[high]:
                low+=1
                high-=1
                continue
            if  nums[mid]<=nums[high]:
                if nums[mid]<=target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
            else:
                if nums[low]<=target<=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
        return False
s1=Solution()
nums=[7,8,9,9,9,9,9,1,7,2,2,3,3,3,4,5,7,7,7]
print(s1.search(nums,2))