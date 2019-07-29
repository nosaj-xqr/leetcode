# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
此题依旧采用递归的方法，每访问一个节点就减去其值，直至小于或者等于0
'''
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        sum = sum - root.val
        if not root.left and not root.right:
            return sum == 0
        return (self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum))
