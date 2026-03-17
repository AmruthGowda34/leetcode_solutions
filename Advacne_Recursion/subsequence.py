class Solution:
    def fun(self,index,subset,nums,result):
        if index==len(nums):
            result.append(subset.copy())
            return
        subset.append(nums[index])
        self.fun(index+1,subset,nums,result)
        subset.pop()
        self.fun(index+1,subset,nums,result)

s1=Solution()
nums=[5,9,7]
result=[]
s1.fun(0,[],nums,result)
print(result)