# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
讨论区题解分析：
1、使用self.res创建全局变量
2、之所以要新定义一个函数，是因为此函数要用来返回最大值，保证递归的正常执行，而最终结果为布尔值，要根据递归过程中的结果来判定，
这也是为什么设置全局变量的用意
'''

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.res = True
        def compare(root):
            if not root:
                return 0
            left=compare(root.left) + 1
            right=compare(root.right) + 1
            if abs(left-right) > 1:
                self.res = False
            return max(left,right)
        compare(root)
        return self.res
