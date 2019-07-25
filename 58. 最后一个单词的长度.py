'''
倒序遍历即可
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res=0
        for i in s[::-1]:
            if i != ' ':
                res+=1
            else:
                break
        return res
