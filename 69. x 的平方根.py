'''
思路1：暴力解法，结果为整数，当某数的平方小于目标数，但其加1后的平方大于目标数，则此为结果
但会超过时间限制
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        i=0
        while i <= x:
            if i*i <= x and (i+1)*(i+1) > x:
                break
            i += 1
        return i
'''
思路1：考虑使用二分法缩减时间，解（a的一半）的平方 >= a，可以得知对于非负数a，当a>=4时，此不等式成立，那么特殊情况就是0、1、2、3，但考虑到a为整数，
这四个特殊值同样可以适用于二分法，因此使用二分法是可以的
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        left=0
        right=x
        while left < right:
            mid = (left + right)//2
            if x >= mid**2 and x < (mid+1)**2:
                return mid
            elif x > mid**2:
                left=mid+1
            else:
                right=mid-1
        return left
