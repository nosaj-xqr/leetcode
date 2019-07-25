'''
对数组进行遍历相加，如之前的数列之和已经为负，后面无论加什么，都小于重新开始遍历相加的结果
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp=nums[0]
        max1=temp
        for i in range(1,len(nums)):
            if temp > 0:
                temp += nums[i]
            else:
                temp = nums[i]
            max1=max(max1,temp)
        return max1
