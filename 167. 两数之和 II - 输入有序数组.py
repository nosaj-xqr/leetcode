'''
常规的双指针法
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        len1=len(numbers)
        left=0
        right=len1-1
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            if numbers[left] + numbers[right] < target:
                left += 1
            if numbers[left] + numbers[right] == target:
                return [left+1,right+1]
