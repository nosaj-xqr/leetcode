'''
思路1：如果没在数组里，则添加进来，反之，将其移除
因涉及到两层遍历，耗时较长
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        same_num=[]
        for i in nums:
            if i in same_num:
                same_num.remove(i)
            else:
                same_num.append(i)
        return same_num[0]
        
'''
思路2：讨论区的思路，数学方法，2*(a+b+c)-(a+a+b+b+c) = c
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)
        
'''
思路3：讨论区的思路，哈希表，在python中即用字典的方法
测试结果此方法耗时最短
popitem()：返回并删除字典中的最后一对键和值
popitem()[0]：得到键值，即结果
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table={}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]
