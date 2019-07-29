# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
.append和.extend:
a=[1,2,3],b=[4,5]
a.append(b)==>[1,2,3,[4,5]]
a.extend(b)==>[1,2,3,4,5]

此题思路：逐层遍历，cur_val存的是当前层所有数值的列表，最后添加到result中；next_val存的是当前层所有数，用于下一次的遍历
'''
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result=[]
        cur=[root]
        while cur:
            cur_val=[]
            next_val=[]
            for nums in cur:
                if nums:
                    cur_val.append(nums.val)
                    next_val.extend([nums.left,nums.right])
            if cur_val:
                result.insert(0,cur_val)
            cur = next_val
        return result
