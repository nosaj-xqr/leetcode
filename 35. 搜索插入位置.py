'''
思路1：暴力解法
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[len(nums)-1] < target:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
'''
思路2：二分法
'''    
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left <= right:
            mid=(left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left += 1
            else:
                right -= 1
        return left
