class Solution:
    def trailingZeroes(self, n: int) -> int:
        '''
        能产生零的只有末尾为2和5的倍数的数
        2的倍数总是比5的倍数多，所以此题可转为阶乘内能找到多少个5
        '''
        res=0
        while n > 1:
            n = n // 5
            res += n
        return res
