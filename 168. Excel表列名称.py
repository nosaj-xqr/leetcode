'''
chr()：用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符
不过使用过程中返回的是\u字符，用encode().decode()也没转换回来，后续想象解决方案
此处改为字典形式，此题为26进制的取余问题，注意26这个边界即可
'''
class Solution:
    def convertToTitle(self, n: int) -> str:
        dict_num={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',
                 14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z',}
        result=''
        while n // 26 > 0:
            if n%26 == 0:
                result = dict_num[26] + result
                n = n-1
            else:
                result = dict_num[n%26] + result
            n = n // 26
        if n != 0:
            result = dict_num[n] + result
        return result
