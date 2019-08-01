'''
思路1：哈希表，即字典
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_num={}
        for i in nums:
            dict_num[i] = dict_num.get(i,0) + 1
            if dict_num.get(i) > len(nums)//2:
                return i
'''
思路2：数学，既然众数的个数超过一半，则排完序后，不管众数值是多少，最中间的数一定是众数,测试结果没有思路1快
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return nums[len(nums)//2]
