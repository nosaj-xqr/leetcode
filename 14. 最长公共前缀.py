'''
思路：
python zip函数：1、对可迭代的变量，按位进行打包，这样就实现了每个字符串都按照位置一一进行比对；
                2、返回列表长度与最短的对象相同，对不同长度的字符串实现正确比对
例：
a=[1,2,3],b=[4,5,6]
zipped=zip(a,b)  ==> [(1,4),(2,5),(3,6)]
zip(*zipped)  ==>[(1,2,3),(4,5,6)]

python集合：set方法可实现去重，在经过zip后的元组，去重后只剩一个元素，则此为公共元素，否则不是
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result=''
        for i in zip(*strs):
            i_set=set(i)
            if len(i_set) == 1:
                result += i[0]
            else:
                break
        return result
