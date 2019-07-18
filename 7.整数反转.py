'''
取余的数学公式：r=a-n*[a/n] -->r为余数，a为被除数，n为除数
在python中，除法取整是向负无穷取整，即-9//7 = -2，不同于其他语言的向零取整，即-9//7 = -1
因此取余的方式不一样
'''
class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        while x != 0:
            if x < 0:
                num = x%-10
            else:
                num = x%10
            if ((result*10 + num)<-(2**31) or (result*10 + num)>(2**31 - 1)):
                return 0
            result = result*10 + num
            x = x/10
            x = int(x)
        return result
