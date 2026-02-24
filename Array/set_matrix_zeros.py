class Solution:
    def zero(self,nums):
        r=len(nums)
        c=len(nums[0])
        row_trace=[0]*r
        col_trace=[0]*c
        for i in range(r):
            for j in range(c):
                if nums[i][j]==0:
                    row_trace[i]=-1
                    col_trace[j]=-1
        for i in range(r):
            for j in range(c):
                if row_trace[i]==-1 or col_trace[j]==-1:
                    nums[i][j]=0
        for i in nums:
            print(i)
        # return nums

s1=Solution()
nums=[[7,9,2,3],
[20,8,0,1],
[9,0,-10,5],
[1,4,6,7]]
print(s1.zero(nums))