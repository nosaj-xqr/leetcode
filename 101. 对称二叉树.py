# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
根据100题思路衍生而来
'''
class Solution:
    def isSame(self,p,q):
        if not p and not q:
            return True
        elif p and q:
            return p.val == q.val and self.isSame(p.left,q.right) and self.isSame(p.right,q.left)
        else:
            return False
    
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            return self.isSame(root.left,root.right)
