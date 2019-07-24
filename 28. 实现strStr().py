'''
思路1：使用python find函数即可
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
'''
思路2：把needle看成一个整体，对haystack进行切片操作
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0,len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1
