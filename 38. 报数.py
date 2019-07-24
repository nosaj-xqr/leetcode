'''
题目意思应可理解为对上一个数的报数，因此，可采用递归的思想，比如：
1. 1 ==>固定初始值
2. 11==>上一个有一个1，因此为11
3. 21==>上一个有两个1，因此为21
4. 1211==>上一个有一个2，一个1，因此为1211
5. 111221==>上一个有一个1（‘11’），一个2（‘12’），两个1（‘21’）
...

'''
class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'
        else:
            last_str=self.countAndSay(n-1)
            new_str=''
            len1=0
            while len1 < len(last_str) :
                count=1
                while len1 < len(last_str) - 1 and last_str[len1] == last_str[len1 + 1]:
                    count += 1
                    len1 += 1
                new_str += (str(count) + last_str[len1])
                len1 += 1
        return new_str
