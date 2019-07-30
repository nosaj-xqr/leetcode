'''
根据题意，发现获取到所有正利润，它们的和即为解
例：[1，2，3，4，5]
1、按示例说明，第一天买入，第五天卖出，得最大利润为4
2、但也可这么理解，第一天买入，第二天卖出，得利润1，再第二天买入，第三天卖出，又得利润1，最终得最大利润4
3、因此，可发现，只要当前数比上一个数大，就可加入结果当中
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        result=0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                result += prices[i] - prices[i-1]
        return result
