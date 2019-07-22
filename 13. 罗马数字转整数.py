'''
罗马数字个数有限，可采用字典来列举出来
根据其特性可发现，当左边数小于右边数时，结果为右边数减去左边数，反之则相加
例：IV=5-1,IVX=10-5-1
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        answer=0
        for i in range(0,len(s)-1):
            if roman[s[i]] >= roman[s[i+1]]:
                answer += roman[s[i]]
            else:
                answer -= roman[s[i]]
        answer += roman[s[len(s)-1]]
        return answer
