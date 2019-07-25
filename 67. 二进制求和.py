'''
1、对短位补齐
2、倒叙相加，二进制下，满2就进一
3、最后一次相加后，进位如果为1，说明首位还有位数增加：‘1’
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            a,b = b,a
        a='0'*(len(b)-len(a))+a
        res=''
        add1=0
        for i in range(len(a)-1,-1,-1):
            a1=int(a[i])
            b1=int(b[i])
            res=str((a1+b1+add1)%2)+res
            add1=(a1+b1+add1)//2
        if add1 == 1:
            return '1'+res
        return res
