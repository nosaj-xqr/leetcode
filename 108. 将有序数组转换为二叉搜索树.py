# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
思路：递归方法，根据对二叉搜索树的描述，只要每一轮的左边和右边高度相差不大于1即可，那就对数组进行对半分，左半边画左树，右半边画右数
'''
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        n = len(nums)
        if n == 0:
            return None
        mid = n//2
        root=TreeNode(nums[mid])
        root.left=self.sortedArrayToBST(nums[0:mid])
        root.right=self.sortedArrayToBST(nums[mid+1:n])
        return root
