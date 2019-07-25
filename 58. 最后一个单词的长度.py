'''
倒序遍历即可
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res=0
        for i in s[::-1]:
            if i != ' ':
                res+=1
            elif res > 0 and i == ' ':
                break
            elif res == 0 and i == ' ':
                continue
        return res
        
