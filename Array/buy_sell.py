class Solution:
    def buy_sell(self,nums):
        min_price=float("inf")
        max_profit=0
        for i in range(len(nums)):
            min_price=min(nums[i],min_price)
            max_profit=max(max_profit,nums[i]-min_price)
        return max_profit
s1=Solution()
nums=[7,1,0,5,3,6,4]
print(s1.buy_sell(nums))