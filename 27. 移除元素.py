'''
思路1：因为不用考虑元素顺序，可以把等于val的元素与最后面不等于val的数兑换
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left=0
        right=len(nums)-1
        while left < right:
            if nums[left]==val and nums[right] != val:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                right -= 1
            elif nums[left] != val:
                left += 1
            elif nums[right] == val:
                right -= 1
        res = 0
        for i in range(len(nums)):
            if nums[i] == val:
                return res
            res += 1
 
'''
思路2：直接覆盖也行,此方法比思路1运行速度更快
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[res] = nums[i]
                res += 1
        return res

'''
思路3：使用python的remove方法直接得出结果,此为最快速度的方法。
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while True:
            if val in nums:
                nums.remove(val)
            else:
                break
        return len(nums)
