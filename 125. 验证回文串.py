'''
思路：
1、采用双指针向中间逼近
2、碰到非数字和字母，则往中间进一步
3、碰到数字和字母，就进行比对

isalnum()方法:检测字符串是否由字母和数字组成
upper()方法:将字符串中的小写字母转为大写字母
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            while left < len(s) and not s[left].isalnum():
                left += 1
            while right > -1 and not s[right].isalnum():
                right -= 1
            #当左指针已经超过右指针，则返回True
            if left > right:
                return True
            if s[left].upper() != s[right].upper():
                return False
            else:
                left += 1
                right -= 1
        return True
