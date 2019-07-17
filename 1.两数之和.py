'''
使用常用的暴力拆解即得答案
两层for循环
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    answer=[i,j]
                    return answer
