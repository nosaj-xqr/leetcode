'''
分析：
1、负数是不可能为回文数的
2、为正数时，第一位与最后一位对比，第二位与倒数第二位对比，防止整数溢出
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            len1=len(str(x))
            for i in range(0,len1//2):
                num1 = x//(10**(len1 - 1 - 2*i))
                num2 = x%10
                if num1 == num2:
                    x = (x - num1*(10**(len1 - 1 - 2*i)) - num2)//10
                else:
                    return False
            return True
