'''
思路1、暴力法
往往这种方法都会超时。
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%len(nums)
        for i in range(k):
            last = nums[len(nums)-1]
            for j in range(0,len(nums)):
                temp = nums[j]
                nums[j] = last
                last = temp
