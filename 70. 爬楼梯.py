'''
思路1：暴力解法，每一步要么走1，要么走2，两种情况相加即得结果，因此进行递归
结果正确，但会超时
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)
'''
思路2：斐波那契数列
走完n步有f(n)种走法，那么：
   第一步走1，则剩下f(n-1)种走法
   第一步走2，则剩下f(n-2)种走法
所以：f(n)=f(n-1)+f(n-2)
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        a=1
        b=1
        for _ in range(n-1):
            a,b = a+b,a
        return a
