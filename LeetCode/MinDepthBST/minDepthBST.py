# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        minLeft = self.minDepth(root.left)
        minRight = self.minDepth(root.right)
        if minLeft==0 or minRight==0:
            return 1+ max(minLeft,minRight)
        return 1+ min(minLeft,minRight)