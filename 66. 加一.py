'''
思路1：
1、只有9、99、999...这种才会加位，且都只需要首位变为1，末位加个0即可
2、碰到9统一变0，非9就加1,直接结束循环
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        digits[0] = 1
        digits.append(0)
        return digits
        
'''
思路2：把数组变为数字，运算后在把结果存入数组,没有上面思路速度快
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum1=0
        for i in range(len(digits)):
            sum1 += 10 ** (len(digits)-1-i) * digits[i]
        sum1 += 1
        result=[]
        sum1_str=str(sum1)
        for j in sum1_str:
            result.append(int(j))
        return result
