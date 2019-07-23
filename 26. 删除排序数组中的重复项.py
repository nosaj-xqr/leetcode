'''
1、不允许添加新数组，可对旧数组进行重复数覆盖操作
2、数组已经排过序，所以一次比对即可
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num=0
        for i in range(0,len(nums)-1):
            if nums[i]!=nums[i+1]:
                num += 1
            nums[num]=nums[i+1]
        if not nums:
            return 0
        else:
            return num+1
