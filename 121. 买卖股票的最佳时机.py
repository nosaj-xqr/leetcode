'''
思路1：暴力解法，超过了时间限制
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        profit=[]
        for i in range(len(prices)):
            buy=prices[i]
            for j in range(i+1,len(prices)):
                profit.append(prices[j] - buy)
        profit = sorted(profit)
        result = profit[len(profit)-1] if profit[len(profit)-1] > 0 else 0
        return result
        
'''
思路2：
实现利润最大化，即买入价最低，卖出价最高
设定两个标志，一个最小值，一个最大值
最小值通过遍历与上一个值对比得出
最大值=今天的价格减去最小值，再拿来和上一个最大值对比
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        min_num = prices[0]
        max_num = 0
        for i in range(len(prices)):
            min_num = min(min_num,prices[i])
            max_num = max(max_num,prices[i] - min_num)
        return max_num
